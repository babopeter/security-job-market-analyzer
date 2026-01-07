# Project Plan: Security Job Market Analyzer

## 1. Project Overview
**Goal:** Analyze public cybersecurity job postings to extract trends in required skills, tools, and compliance frameworks, producing structured signals relevant to security practitioners and organizations.

## 2. Scope
### In-Scope
- **Data Source:** Public job postings only.
- **Methodology:** Textual analysis (NLP) to identify key terms.
- **Focus:** Trend extraction (e.g., "Rise in Kubernetes security requirements") rather than prediction.
- **Domain:** Security-related roles only (e.g., SOC Analyst, Penetration Tester, Security Engineer).

### Out-of-Scope
- Salary inference or estimation.
- Company ranking or reputation scoring.
- Candidate/Resume matching.
- Real-time/Live monitoring of individual companies (snapshot analysis preferred).
- Scraping content behind authentication/logins.

## 3. High-Level Architecture
1.  **Ingestion Module:**
    -  Accepts raw text or URLs of public job postings.
    -  Standardizes format for analysis.
2.  **Analysis Engine (Core):**
    -  **Keyword Extraction:** Identifies specific tools (e.g., Splunk, Burp Suite), languages (Python, Go), and frameworks (NIST, ISO 27001).
    -  **Classification:** Categorizes roles (Blue Team, Red Team, GRC).
3.  **Reporting Module:**
    -  Aggregates data to show frequencies and co-occurrences.
    -  Outputs structured data (JSON/CSV) and summary reports.

## 4. Proposed Technology Stack
- **Language:** Python 3.10+
- **Data Handling:** Pandas
- **NLP/Text Processing:** Spacy or NLTK, Regular Expressions
- **Interface:** CLI (Command Line Interface) for initial prototype.

## 5. Roadmap
- [x] **Phase 1: Setup & Ingestion** - Initialize project, create basic script to read dummy job descriptions.
- [x] **Phase 2: Extraction Logic** - Implement regex/NLP logic to find skills and tools.
- [x] **Phase 3: Aggregation** - specific logic to count and rank extracted terms.
- [x] **Phase 4: CLI & Reporting** - Build the user interface to run the analysis and view results.
