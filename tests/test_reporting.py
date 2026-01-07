import unittest
import json
import io
import csv
from collections import Counter
from src.analysis import MarketAnalyzer
from src.reporting import Reporter

class TestReporter(unittest.TestCase):
    def setUp(self):
        self.analyzer = MarketAnalyzer()
        # Mock some data
        self.analyzer.total_postings = 2
        self.analyzer.stats["languages"] = Counter({"Python": 2, "Go": 1})
        self.analyzer.stats["tools"] = Counter({"Splunk": 1})
        self.reporter = Reporter(self.analyzer)

    def test_generate_json(self):
        json_output = self.reporter.generate_json()
        data = json.loads(json_output)
        
        self.assertEqual(data["total_postings"], 2)
        self.assertEqual(data["stats"]["languages"]["Python"], 2)
        self.assertEqual(data["stats"]["tools"]["Splunk"], 1)

    def test_generate_csv(self):
        output = io.StringIO()
        self.reporter.generate_csv(output)
        content = output.getvalue()
        
        reader = csv.reader(content.splitlines())
        rows = list(reader)
        
        # Check header
        self.assertEqual(rows[0], ["Category", "Term", "Count", "Percentage"])
        
        # Check data existence (order might vary by category iteration order, but within category is sorted)
        # We can convert rows to a list of lists or set of tuples for easier checking
        data_rows = [tuple(r) for r in rows[1:]]
        
        # Python: 2/2 = 100%
        self.assertIn(("languages", "Python", "2", "100.00%"), data_rows)
        # Go: 1/2 = 50%
        self.assertIn(("languages", "Go", "1", "50.00%"), data_rows)

if __name__ == '__main__':
    unittest.main()
