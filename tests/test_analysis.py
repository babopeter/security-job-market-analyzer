import unittest
from src.analysis import MarketAnalyzer

class TestMarketAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = MarketAnalyzer()

    def test_add_and_count(self):
        # Simulate results from 3 jobs
        job1 = {"languages": ["Python", "Go"], "tools": ["Splunk"]}
        job2 = {"languages": ["Python"], "tools": ["Burp Suite"]}
        job3 = {"languages": ["Java"], "tools": ["Splunk"]}

        self.analyzer.add_extraction_result(job1)
        self.analyzer.add_extraction_result(job2)
        self.analyzer.add_extraction_result(job3)

        self.assertEqual(self.analyzer.total_postings, 3)
        
        # Check counts
        top_langs = self.analyzer.get_top_terms("languages")
        # Python: 2, Go: 1, Java: 1
        # Convert to dict for easier assertion
        lang_dict = dict(top_langs)
        self.assertEqual(lang_dict["Python"], 2)
        self.assertEqual(lang_dict["Go"], 1)
        self.assertEqual(lang_dict["Java"], 1)

        top_tools = self.analyzer.get_top_terms("tools")
        tool_dict = dict(top_tools)
        self.assertEqual(tool_dict["Splunk"], 2)
        self.assertEqual(tool_dict["Burp Suite"], 1)

    def test_empty_results(self):
        self.analyzer.add_extraction_result({})
        self.assertEqual(self.analyzer.total_postings, 1)
        self.assertEqual(self.analyzer.get_top_terms("languages"), [])

    def test_report_generation(self):
        job1 = {"languages": ["Python"]}
        self.analyzer.add_extraction_result(job1)
        report = self.analyzer.get_summary_report()
        self.assertIn("Analysis Summary", report)
        self.assertIn("Python: 1 (100.0%)", report)

if __name__ == '__main__':
    unittest.main()
