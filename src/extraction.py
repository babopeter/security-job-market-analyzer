import re

class JobExtractor:
    def __init__(self):
        self.patterns = {
            "languages": [
                r"Python", r"C\+\+", r"\bC\b", r"Java\b", r"Go\b", r"Rust", r"Ruby", 
                r"Perl", r"Bash", r"Shell", r"PowerShell", r"SQL", 
                r"JavaScript", r"TypeScript", r"Assembly"
            ],
            "cloud_infra": [
                r"AWS", r"Amazon Web Services", r"Azure", r"GCP", r"Google Cloud", 
                r"Kubernetes", r"K8s", r"Docker", r"Terraform", r"Ansible", 
                r"Jenkins", r"Git", r"Linux", r"Windows"
            ],
            "security_tools": [
                r"Splunk", r"SIEM", r"Burp Suite", r"Metasploit", r"Wireshark", 
                r"Nmap", r"Nessus", r"Qualys", r"CrowdStrike", r"SentinelOne", 
                r"Snort", r"Zeek", r"ELK", r"Elastic Stack"
            ],
            "frameworks_compliance": [
                r"NIST", r"ISO\s?27001", r"SOC2", r"PCI[- ]?DSS", r"HIPAA", 
                r"GDPR", r"CIS Controls", r"MITRE ATT&CK"
            ],
            "certifications": [
                r"CISSP", r"OSCP", r"CEH", r"CISM", r"CompTIA Security\+", 
                r"AWS Security", r"GSEC", r"GCIH"
            ]
        }
        # Compile patterns for efficiency
        self.compiled_patterns = {}
        for category, regex_list in self.patterns.items():
            # Create a single pattern for the category: (\bPattern1\b|\bPattern2\b)
            # Use word boundaries \b to avoid partial matches (e.g. "Go" in "Google")
            # But handle special characters like C++ or .NET carefully
            
            cleaned_patterns = []
            for p in regex_list:
                # If pattern starts with \b or similar, leave it. Else add \b if it starts/ends with word char.
                # Simplified approach: Wrap in \b unless it contains non-word boundary chars at ends
                # Actually, simpler to let specific regexes handle their boundaries or default to \b
                
                # For this prototype, strict word boundaries for most
                if p.startswith(r"\b") or p.startswith("^"):
                    cleaned_patterns.append(p)
                elif p in [r"C\+\+", r"C#", r".NET"]:
                    cleaned_patterns.append(re.escape(p) if "\\" not in p else p)
                else:
                    cleaned_patterns.append(rf"\b{p}\b")
            
            combined_pattern = "|".join(cleaned_patterns)
            self.compiled_patterns[category] = re.compile(combined_pattern, re.IGNORECASE)

    def extract(self, text):
        """
        Extracts key terms from the job description text.
        """
        results = {}
        for category, pattern in self.compiled_patterns.items():
            # findall returns a list of strings
            matches = pattern.findall(text)
            # Normalize matches (to lower case or keep original?)
            # Better to return unique matches.
            # For counting, we might want all, but for "present/not present" we want set.
            # Let's return a list of unique found terms (normalized to Title Case or similar if possible, 
            # but regex matches might vary in case).
            
            # Let's deduplicate while preserving case from the text, or normalize.
            # Normalizing to the key in our list would be ideal but hard with regex "OR".
            # For now, unique strings found.
            results[category] = list(set(matches))
        
        return results
