import json
import csv
import sys

class Reporter:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def generate_json(self):
        """
        Returns a JSON string representation of the analysis stats.
        """
        # Convert Counter objects to standard dicts for JSON serialization
        data = {
            "total_postings": self.analyzer.total_postings,
            "stats": {
                category: dict(counter) 
                for category, counter in self.analyzer.stats.items()
            }
        }
        return json.dumps(data, indent=4)

    def generate_csv(self, output_stream=sys.stdout):
        """
        Writes stats to a CSV format stream.
        Columns: Category, Term, Count, Percentage
        """
        writer = csv.writer(output_stream)
        writer.writerow(["Category", "Term", "Count", "Percentage"])
        
        total = self.analyzer.total_postings
        if total == 0:
            return

        for category, counter in self.analyzer.stats.items():
            # Sort by count descending
            for term, count in counter.most_common():
                pct = (count / total) * 100
                writer.writerow([category, term, count, f"{pct:.2f}%"])
