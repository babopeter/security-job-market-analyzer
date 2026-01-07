# Security Job Market Analyzer

A Python-based tool designed to analyze public cybersecurity job postings. It extracts trends in required skills, tools, and compliance frameworks to provide structured insights for security practitioners and organizations.

## Features

- **Ingestion:** Load job descriptions from local text files.
- **Extraction:** Identify key terms using regex-based pattern matching:
  - **Languages:** Python, Go, SQL, etc.
  - **Cloud Infrastructure:** AWS, Kubernetes, Docker, etc.
  - **Security Tools:** Splunk, Burp Suite, Wireshark, etc.
  - **Compliance Frameworks:** NIST, ISO 27001, SOC2, etc.
  - **Certifications:** CISSP, OSCP, CISM, etc.
- **Aggregation:** specific logic to count and rank extracted terms across multiple job postings.
- **Reporting:** Export analysis results to Text (summary), JSON, or CSV formats.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/security-job-market-analyzer.git
    cd security-job-market-analyzer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The tool is run via the command line using `main.py`.

### Basic Usage
Run the analyzer on the default sample data:
```bash
python3 main.py
```

### Specify Input Directory
Analyze job postings from a specific directory:
```bash
python3 main.py --dir /path/to/job_files
```

### Output Formats

**JSON Output:**
```bash
python3 main.py --format json
```

**CSV Output:**
```bash
python3 main.py --format csv
```

**Save to File:**
You can save the output to a file using the `--output` flag:
```bash
python3 main.py --format csv --output market_analysis.csv
```

## Project Structure

- `src/`: Source code for the application.
  - `ingestion.py`: Handles file loading.
  - `extraction.py`: Contains the logic for extracting keywords.
  - `analysis.py`: Aggregates and counts terms.
  - `reporting.py`: Generates formatted output (JSON, CSV).
- `data/`: Directory for storing job posting text files.
  - `samples/`: Contains sample job descriptions.
- `tests/`: Unit tests for the project.

## Development

To run the unit tests:
```bash
python3 -m unittest discover tests
```

## TODO / Future Enhancements
- [ ] **Web Scraper:** Implement a scraper to automatically collect job postings from public boards and feed them into the analyzer.
- [ ] **Advanced NLP:** Integrate spaCy for better entity recognition and context-aware extraction.

## License

[MIT License](LICENSE)
