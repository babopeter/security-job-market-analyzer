from src.ingestion import load_job_postings

def main():
    print("Security Job Market Analyzer")
    print("Phase 1: Ingestion\n")
    
    sample_dir = "data/samples"
    postings = load_job_postings(sample_dir)
    
    print(f"Total postings loaded: {len(postings)}")
    for i, post in enumerate(postings, 1):
        print(f"\nPosting {i}:")
        print("-" * 20)
        print(post.strip())

if __name__ == "__main__":
    main()

