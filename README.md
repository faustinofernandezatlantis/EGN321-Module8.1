
```
# Engineering Data Processor & Visualizer

## 1. Project Overview
- **What the application does:** Processes engineering time-series datasets containing temperature and pressure values, calculates summary statistics, and visualizes parameter trends over time.
- **Problem it solves:** Prevents operational errors caused by invalid engineering units, missing headers, or out-of-bound sensor readings by validating data before analysis.
- **Replaced Process:** Replaces manual spreadsheet (Excel) calculations and visual inspection of raw sensor log files.
- **Intended User:** Engineers, system operators, and data analysts who need quick, reliable data validation and visualization.

## 2. System Requirements
- **Operating System:** Windows 10/11, macOS, or Linux
- **Python Version:** Python 3.10 or higher
- **Required Libraries:** `streamlit`, `pandas`, `pytest` (specified in `requirements.txt`)
- **Required Files:** Sample CSV files located in `data/` (e.g., `data/sample_input.csv`)
- **Network Requirements:** Localhost network port access (default: `http://localhost:8501`)

## 3. Installation
Follow these exact steps to set up the environment:

1. Clone the repository:
   ```bash
   git clone [https://github.com/faustinofernandezatlantis/EGN321-Module8.1.git](https://github.com/faustinofernandezatlantis/EGN321-Module8.1.git)
   cd EGN321_Module8.1

```

2. Create a virtual environment:
* **Windows:**
```bash
python -m venv .venv

```


* **macOS/Linux:**
```bash
python3 -m venv .venv

```




3. Activate the virtual environment:
* **Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1

```


* **macOS/Linux:**
```bash
source .venv/bin/activate

```




4. Install required packages:
```bash
pip install -r requirements.txt

```



## 4. Quick Start

1. Activate your virtual environment.
2. Start the application:
```bash
streamlit run app.py

```


3. Open your browser at `http://localhost:8501`.
4. Upload `data/sample_input.csv` using the sidebar.
5. Review the summary metrics, processed table, and charts.

## 5. Normal Operation

1. **Launch App:** Execute `streamlit run app.py` in your terminal.
2. **Data Selection:** Click **Browse files** in the sidebar input panel and upload a `.csv` dataset.
3. **Automated Processing:** The application parses columns and validates numerical bounds automatically.
4. **Result Review:**
* Check the **System Health Status** banner at the top (`HEALTHY`).
* Inspect summary metrics (Total Records, Avg Temperature, Avg Pressure).
* View interactive time-series charts.


5. **Diagnostics:** Expand the **View Diagnostic Logs** panel at the bottom to inspect execution logs.

## 6. Inputs and Units

| Parameter | Required? | Accepted Format / Range | Units |
| --- | --- | --- | --- |
| `timestamp` | Yes | YYYY-MM-DD HH:MM:SS or standard ISO date string | N/A |
| `temperature` | Yes | Numeric float from -40.0 to 120.0 | Celsius (°C) |
| `pressure` | Yes | Numeric float from 0.0 to 500.0 | Kilopascals (kPa) |

## 7. What the Tool Refuses

The application safely halts execution and displays an explicit refusal notice under the following conditions:

* **Missing Required Columns:** If the uploaded CSV lacks `timestamp`, `temperature`, or `pressure`.
* **Out-of-Bound Engineering Values:** If temperature falls outside [-40.0°C, 120.0°C] or pressure falls outside [0.0 kPa, 500.0 kPa].
* **Unreadable File Structure:** Corrupted or empty CSV files.

## 8. Expected Output

When operated successfully, the main dashboard provides:

* **Status Indicator:** Green status banner confirming `HEALTHY` state.
* **Metric Cards:** Displaying average temperature and pressure values alongside total record count (e.g., 100 records).
* **Interactive Data Table:** Structured display of all input rows.
* **Trend Charts:** Interactive line charts displaying sensor readings over time.

## 9. System Health and Alerts

* `HEALTHY`: All system checks passed, file structure is valid, and sensor values are within safe bounds.
* `DEGRADED`: System operational, but processing completed with non-critical warnings.
* `FAILED`: Safe processing refused due to missing headers, invalid bounds, or corrupted data.

## 10. Logs

* **Location:** `logs/app.log`
* **Content:** Timestamped operational logs, warning events, and error details.
* **How to View:** Open `logs/app.log` in any text editor, or view directly via the UI under the **View Diagnostic Logs** expander.

## 11. Troubleshooting

| Problem | Possible Cause | What to Check / Solution |
| --- | --- | --- |
| Application fails to start | Dependencies not installed or virtual environment inactive | Activate `.venv` and run `pip install -r requirements.txt`. |
| Data upload refused | Missing required headers or out-of-bounds values | Ensure CSV headers match `timestamp`, `temperature`, `pressure` and values meet safety ranges. |
| Pytest suite fails | Missing `logs/` directory | Ensure the directory exists or run `python -m pytest` which handles directory initialization automatically. |

## 12. Recovery Procedures

If the application reaches a `FAILED` status:

1. Open the **View Diagnostic Logs** panel at the bottom of the interface.
2. Identify the refusal reason noted in the log entry.
3. Correct the input dataset file or select a valid dataset (`data/sample_input.csv`).
4. Re-upload the corrected dataset in the sidebar.

## 13. Assumptions

* All incoming temperature figures are measured in **Celsius (°C)**.
* All incoming pressure figures are measured in **Kilopascals (kPa)**.
* CSV files use standard UTF-8 encoding.

## 14. Known Limitations

* Does not automatically perform unit conversions (e.g., Fahrenheit to Celsius).
* Supports CSV file uploads up to standard browser file limit (~200 MB).

## 15. Testing

To run unit and validation tests, execute:

```bash
python -m pytest

```

## 16. AI Usage

AI assistants (such as ChatGPT / Claude) were utilized during development to assist with writing Streamlit UI boilerplate and Pytest fixtures. All generated logic, validations, and documentation were manually verified and tested. Detailed prompts and responses are recorded in `AI_LOG.md`.

```
```
## APP LINK

https://egn321-module8-1.streamlit.app/

```
