# AI Usage Log (`AI_LOG.md`)

## 1. Overview
This log documents the usage of Artificial Intelligence (AI) assistants during the development of the **Engineering Data Processor & Visualizer** application for EGN-321 Assignment 8.1 (The Silent Handoff Challenge).

---

## 2. AI Tools Utilized
- **AI Model:** OpenAI ChatGPT / Claude / Gemini
- **Primary Use Cases:** 
  - Designing project structure and architecture for the Streamlit application.
  - Writing boilerplate code for data validation, unit safety boundaries, and logging.
  - Writing `pytest` unit test fixtures and test cases.
  - Generating synthetic engineering sample datasets (100 records).
  - Formatting documentation according to the 16 required README sections.

---

## 3. Prompts & Contributions

### Prompt 1: Application Architecture & Logic
- **User Intent:** Request for a complete Streamlit-based Python application (`app.py`) with input range validation, system health state tracking (`HEALTHY`, `DEGRADED`, `FAILED`), logging capability, and interactive charts.
- **AI Contribution:** Provided the code structure for `app.py` including `pandas` CSV parsing, validation bounds (-40.0 to 120.0 °C and 0.0 to 500.0 kPa), session state health management, and diagnostic log displays.
- **Verification:** Manually tested data uploads with both valid datasets and out-of-bound/malformed files to confirm refusal logic operated as expected.

### Prompt 2: Unit Testing Suite
- **User Intent:** Request for a `pytest` test suite (`test_app.py`) to validate core rules independently.
- **AI Contribution:** Generated test functions covering column checks, temperature boundary conditions, and file system logging writes.
- **Verification:** Ran `python -m pytest` in terminal, identified a filesystem path issue during execution, and updated the test logic to ensure 100% test pass rate (`3 passed`).

### Prompt 3: Sample Dataset Generation
- **User Intent:** Request for an extended sample dataset (`data/sample_input.csv`) containing at least 100 realistic engineering records.
- **AI Contribution:** Generated 100 formatted CSV rows with 5-minute time increments, fluctuating temperature values within safe ranges (19°C to 33°C), and normal pressure readings (~100 to 105 kPa).
- **Verification:** Uploaded dataset directly into `app.py` to verify metric cards and time-series line chart rendering.

---

## 4. Human Verification & Audit
All AI-generated code, tests, and documentation were reviewed, edited, and validated manually:
1. **Code Execution:** Ran `streamlit run app.py` locally to test user interaction and error popups.
2. **Automated Testing:** Verified test execution via `pytest` to confirm zero regression failures.
3. **Accuracy Check:** Confirmed all technical limits and units matched assignment requirements before finalizing repository files.