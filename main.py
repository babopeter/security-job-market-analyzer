import sys
import argparse
from src.ingestion import load_job_postings
from src.extraction import JobExtractor
from src.analysis import MarketAnalyzer
from src.reporting import Reporter

def main():
    parser = argparse.ArgumentParser(description="Security Job Market Analyzer")
    parser.add_argument("--dir", default="data/samples", help="Directory containing job posting text files")
    parser.add_argument("--format", choices=["text", "json", "csv"], default="text", help="Output format")
    parser.add_argument("--output", help="Output file path (optional). If not specified, prints to stdout.")
    args = parser.parse_args()

    # print("Security Job Market Analyzer")
    # print("Phase 4: CLI & Reporting\n")
    # Only print status messages if output is text or to a file, to avoid messing up stdout JSON/CSV redirection
    if args.format == "text" and not args.output:
         print(f"Loading jobs from: {args.dir}...\n")
    
    sample_dir = args.dir
    postings = load_job_postings(sample_dir)
    
    if not postings:
        print("No job postings found.")
        return

    # Initialize Components
    extractor = JobExtractor()
    analyzer = MarketAnalyzer()
    
    for post in postings:
        results = extractor.extract(post)
        analyzer.add_extraction_result(results)

    # Reporting
    reporter = Reporter(analyzer)
    
    output_content = ""
    
    if args.format == "json":
        output_content = reporter.generate_json()
    elif args.format == "csv":
        # CSV handling is slightly different because it writes to a stream
        if args.output:
            with open(args.output, 'w', newline='') as f:
                reporter.generate_csv(f)
            print(f"CSV report saved to {args.output}")
            return
        else:
            reporter.generate_csv(sys.stdout)
            return
    else: # text
        output_content = analyzer.get_summary_report()

    # Handle Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_content)
        print(f"Report saved to {args.output}")
    else:
        print(output_content)

if __name__ == "__main__":
    main()

