import unittest
from src.extraction import JobExtractor

class TestJobExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = JobExtractor()

    def test_extract_basic(self):
        text = "We need a Python developer with AWS and Kubernetes experience."
        results = self.extractor.extract(text)
        self.assertIn("Python", results["languages"])
        self.assertIn("AWS", results["cloud_infra"])
        self.assertIn("Kubernetes", results["cloud_infra"])

    def test_extract_case_insensitive(self):
        text = "experience with python, aws, and kubernetes."
        results = self.extractor.extract(text)
        # Matches are currently returned as found in text or normalized? 
        # My implementation returns matches as found in text.
        # But regex with IGNORECASE usually returns the string from the text, not the pattern.
        # So "python" should be found.
        # Let's check my implementation: `matches = pattern.findall(text)`
        # Yes, it returns text segments.
        found_languages = [x.lower() for x in results["languages"]]
        self.assertIn("python", found_languages)

    def test_extract_word_boundaries(self):
        text = "I like crawling websites." # Contains 'awl' but shouldn't match AWS if I had that (bad example)
        # Better example: "Go"
        text = "Let's Go to the park." # Should not match language "Go" ideally, but "Go" is hard.
        # "Experience with Go language." -> Should match.
        # My regex for Go was `r"Go\b"`.
        # "Go" in "Google" -> `\bGo\b` shouldn't match.
        
        text_google = "We use Google Cloud."
        results = self.extractor.extract(text_google)
        # Should match "Google Cloud" but NOT "Go" separately if logic works.
        self.assertIn("Google Cloud", results["cloud_infra"])
        self.assertNotIn("Go", results["languages"])

    def test_extract_complex_security_tools(self):
        text = "Proficiency in Burp Suite and Metasploit."
        results = self.extractor.extract(text)
        self.assertIn("Burp Suite", results["security_tools"])
        self.assertIn("Metasploit", results["security_tools"])

if __name__ == '__main__':
    unittest.main()
