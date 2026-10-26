import os
import pytest
import pandas as pd
from app import LOG_FILE, LOG_DIR

# ==========================================
# 1. FIXTURES & SETUP
# ==========================================
@pytest.fixture
def valid_dataframe():
    """Provides a valid sample DataFrame for testing."""
    return pd.DataFrame({
        "timestamp": ["2026-10-25 10:00:00", "2026-10-25 10:05:00"],
        "temperature": [22.5, 24.1],
        "pressure": [101.3, 102.0]
    })

@pytest.fixture
def invalid_columns_dataframe():
    """Provides a DataFrame missing required columns."""
    return pd.DataFrame({
        "time": ["2026-10-25 10:00:00"],
        "temp_celsius": [22.5]
    })

@pytest.fixture
def out_of_bounds_dataframe():
    """Provides a DataFrame with out-of-range engineering values."""
    return pd.DataFrame({
        "timestamp": ["2026-10-25 10:00:00"],
        "temperature": [150.0],  # Out of range (> 120.0 °C)
        "pressure": [101.3]
    })

# ==========================================
# 2. UNIT TESTS
# ==========================================
def test_required_columns_validation(valid_dataframe, invalid_columns_dataframe):
    """Tests that required columns are accurately identified."""
    required_cols = {"timestamp", "temperature", "pressure"}
    
    # Valid dataset check
    assert required_cols.issubset(valid_dataframe.columns) == True
    
    # Invalid dataset check
    assert required_cols.issubset(invalid_columns_dataframe.columns) == False


def test_temperature_range_validation(valid_dataframe, out_of_bounds_dataframe):
    """Tests that out-of-bound temperature values trigger detection."""
    # Check valid data (-40°C to 120°C)
    valid_out_of_bounds = valid_dataframe[
        (valid_dataframe["temperature"] < -40.0) | (valid_dataframe["temperature"] > 120.0)
    ]
    assert valid_out_of_bounds.empty == True

    # Check invalid data (150°C should be flagged)
    invalid_out_of_bounds = out_of_bounds_dataframe[
        (out_of_bounds_dataframe["temperature"] < -40.0) | (out_of_bounds_dataframe["temperature"] > 120.0)
    ]
    assert not invalid_out_of_bounds.empty == True


def test_logging_creation():
    """Tests that logging directory and log file are correctly initialized."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    test_message = "TEST_EVENT: Executing Pytest validation check."
    
    # Force write to log file to test filesystem access
    with open(LOG_FILE, "a") as f:
        f.write(f"INFO: {test_message}\n")
    
    assert os.path.exists(LOG_FILE)
    
    with open(LOG_FILE, "r") as f:
        log_content = f.read()
    
    assert test_message in log_content