from util.generate_docs import generate_docs
from pathlib import Path

if __name__ == "__main__":
    print("Generating docs...")
    generate_docs()
    print(f"README.md file created in directory {Path.cwd()}.")
