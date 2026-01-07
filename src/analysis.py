from collections import Counter, defaultdict

class MarketAnalyzer:
    def __init__(self):
        # Dictionary mapping category -> Counter object
        self.stats = defaultdict(Counter)
        self.total_postings = 0

    def add_extraction_result(self, extraction_result):
        """
        Ingest a single dictionary of extraction results.
        extraction_result: { 'category': ['term1', 'term2'], ... }
        """
        self.total_postings += 1
        for category, terms in extraction_result.items():
            # Update the counter for this category
            # terms is a list of unique terms found in one posting
            self.stats[category].update(terms)

    def get_top_terms(self, category, top_n=10):
        """
        Returns a list of (term, count) tuples for the specified category.
        """
        if category not in self.stats:
            return []
        return self.stats[category].most_common(top_n)

    def get_summary_report(self):
        """
        Returns a text summary of the current statistics.
        """
        report = []
        report.append(f"Analysis Summary (N={self.total_postings} postings)")
        report.append("=" * 40)
        
        # Sort categories to ensure consistent order
        for category in sorted(self.stats.keys()):
            title = category.replace("_", " ").title()
            report.append(f"\nTop {title}:")
            top_terms = self.get_top_terms(category, 5)
            if not top_terms:
                report.append("  (No data found)")
            else:
                for term, count in top_terms:
                    # Calculate percentage
                    pct = (count / self.total_postings) * 100
                    report.append(f"  - {term}: {count} ({pct:.1f}%)")
        
        return "\n".join(report)
