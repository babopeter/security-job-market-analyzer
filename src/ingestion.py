import os

def load_job_postings(directory_path):
    """
    Loads all text files from the specified directory.
    Returns a list of strings, each representing a job posting.
    """
    postings = []
    if not os.path.exists(directory_path):
        print(f"Error: Directory {directory_path} does not exist.")
        return postings

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                postings.append(f.read())
    
    return postings

if __name__ == "__main__":
    # Test the ingestion
    sample_dir = "data/samples"
    jobs = load_job_postings(sample_dir)
    print(f"Loaded {len(jobs)} job postings from {sample_dir}:")
    for i, job in enumerate(jobs, 1):
        print(f"--- Job {i} ---")
        print(job[:100] + "...")
