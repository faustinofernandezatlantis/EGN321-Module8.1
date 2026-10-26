import os
import logging
from datetime import datetime
import pandas as pd
import streamlit as st

# ==========================================
# 1. LOGGING & SYSTEM HEALTH CONFIGURATION
# ==========================================
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def log_event(level: str, message: str):
    """Writes event messages to the local system log file."""
    if level == "INFO":
        logging.info(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "ERROR":
        logging.error(message)

# Initialize Session State for System Health
if "health_status" not in st.session_state:
    st.session_state.health_status = "HEALTHY"
    log_event("INFO", "Application initialized with status: HEALTHY")

# ==========================================
# 2. PAGE CONFIGURATION & HEADER
# ==========================================
st.set_page_config(
    page_title="Engineering Data Processor",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Engineering Data Processor & Visualizer")
st.caption("Module 8 — Silent Handoff Challenge Demonstration Tool")

# Display Current System Health Status
health = st.session_state.health_status
if health == "HEALTHY":
    st.success("🟢 System Health: HEALTHY — Ready for operations.")
elif health == "DEGRADED":
    st.warning("🟡 System Health: DEGRADED — Processing completed with non-critical warnings.")
elif health == "FAILED":
    st.error("🔴 System Health: FAILED — Critical error detected. Check logs.")

st.markdown("---")

# ==========================================
# 3. SIDEBAR: DATA INPUT & UNITS
# ==========================================
st.sidebar.header("📥 Input Panel")
st.sidebar.markdown("**Accepted File Format:** `.csv`")
st.sidebar.markdown("**Required Columns:** `timestamp`, `temperature`, `pressure`")

uploaded_file = st.sidebar.file_uploader("Upload CSV Dataset", type=["csv"])

st.sidebar.markdown("---")
st.sidebar.subheader("📐 Unit & Operational Bounds")
st.sidebar.info(
    "• **Temperature:** -40.0 °C to 120.0 °C\n"
    "• **Pressure:** 0.0 kPa to 500.0 kPa"
)

# ==========================================
# 4. PROCESSING & REFUSAL LOGIC
# ==========================================
if uploaded_file is not None:
    log_event("INFO", f"File uploaded: {uploaded_file.name}")
    
    try:
        df = pd.read_csv(uploaded_file)
        
        # Validation 1: Required Columns Check
        required_cols = {"timestamp", "temperature", "pressure"}
        if not required_cols.issubset(df.columns):
            st.session_state.health_status = "FAILED"
            error_msg = f"Refusal: CSV missing required columns. Expected: {list(required_cols)}"
            st.error(f"❌ **Data Refused:** {error_msg}")
            log_event("ERROR", error_msg)
            st.stop()
            
        # Validation 2: Out of Bounds Check
        temp_out_bounds = df[(df["temperature"] < -40.0) | (df["temperature"] > 120.0)]
        press_out_bounds = df[(df["pressure"] < 0.0) | (df["pressure"] > 500.0)]
        
        if not temp_out_bounds.empty or not press_out_bounds.empty:
            st.session_state.health_status = "FAILED"
            refusal_reason = "Out-of-range sensor values detected. Operations refused for physical safety."
            st.error(f"🚫 **Tool Refusal:** {refusal_reason}")
            st.warning("Ensure Temperature is between -40°C and 120°C, and Pressure is between 0 and 500 kPa.")
            log_event("ERROR", refusal_reason)
            st.stop()
            
        # Success Workflow Execution
        st.session_state.health_status = "HEALTHY"
        log_event("INFO", f"Successfully processed {len(df)} records from {uploaded_file.name}")
        
        # Display Outputs
        st.subheader("📊 Output Results")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", len(df))
        col2.metric("Avg Temperature (°C)", f"{df['temperature'].mean():.2f}")
        col3.metric("Avg Pressure (kPa)", f"{df['pressure'].mean():.2f}")
        
        st.markdown("### Processed Data Table")
        st.dataframe(df, use_container_width=True)
        
        st.markdown("### Sensor Metrics Over Time")
        chart_data = df.set_index("timestamp")[["temperature", "pressure"]]
        st.line_chart(chart_data)
        
    except Exception as e:
        st.session_state.health_status = "FAILED"
        err_details = f"Unexpected error during execution: {str(e)}"
        st.error(f"❌ {err_details}")
        log_event("ERROR", err_details)

else:
    st.info("👋 Welcome! To begin, upload a valid `.csv` file using the sidebar on the left.")

# ==========================================
# 5. DIAGNOSTIC LOGS SECTION
# ==========================================
st.markdown("---")
with st.expander("📋 View Diagnostic Logs"):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            log_contents = f.read()
        st.text_area("System Log File (`logs/app.log`)", log_contents, height=200)
    else:
        st.write("No log file generated yet.")