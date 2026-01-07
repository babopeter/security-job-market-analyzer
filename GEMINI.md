# Project Overview

The **Security Job Market Analyzer** is a Python-based CLI tool designed to analyze public cybersecurity job postings. It ingests job descriptions from text files, extracts key terms (skills, tools, certifications, compliance frameworks) using regular expressions, aggregates the data to calculate frequencies, and generates reports in Text, JSON, or CSV formats.

**Main Technologies:**
*   **Python 3:** Core language.
*   **Regex (`re`):** Primary method for entity extraction (currently replacing planned NLP/spaCy logic).
*   **Collections (`Counter`):** Used for statistical aggregation.
*   **Unittest:** Testing framework.

**Architecture:**
*   **Ingestion (`src/ingestion.py`):** Loads raw text files from a directory.
*   **Extraction (`src/extraction.py`):** `JobExtractor` class uses pre-defined regex patterns to identify keywords.
*   **Analysis (`src/analysis.py`):** `MarketAnalyzer` class aggregates extraction results using counters.
*   **Reporting (`src/reporting.py`):** `Reporter` class formats the aggregated data into the desired output (JSON/CSV).
*   **CLI (`main.py`):** Entry point handling argument parsing and workflow orchestration.

# Building and Running

**Dependencies:**
Install the required Python packages (though currently the core logic is standard library, `pandas` and `spacy` are listed for future expansion):
```bash
pip install -r requirements.txt
```

**Running the Application:**
The entry point is `main.py`.

*   **Standard Run (Text Summary):**
    ```bash
    python3 main.py
    ```
    *Defaults to looking in `data/samples`.*

*   **Specify Input Directory:**
    ```bash
    python3 main.py --dir path/to/job_files
    ```

*   **JSON Output:**
    ```bash
    python3 main.py --format json
    ```

*   **CSV Output to File:**
    ```bash
    python3 main.py --format csv --output results.csv
    ```

**Running Tests:**
Execute the unit test suite:
```bash
python3 -m unittest discover tests
```

# Development Conventions

*   **Modular Design:** Logic is separated into distinct modules within `src/` (Ingestion, Extraction, Analysis, Reporting).
*   **Pattern-Based Extraction:** New skills or tools should be added to the `self.patterns` dictionary in `src/extraction.py`.
*   **Testing:** New features must include corresponding unit tests in the `tests/` directory, using the `unittest` framework.
*   **Data Handling:** The system operates on lists of strings (job descriptions) and dictionaries of extracted lists.
*   **Future Scope:** The project plan (`PROJECT_PLAN.md`) includes a roadmap for adding a web scraper and advanced NLP capabilities.
