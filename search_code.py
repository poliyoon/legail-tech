"""
search_code.py
Search for specific class or function in site-packages.
"""
import os
import sys

def search_in_path(base_path, target_string):
    print(f"Searching in: {base_path}")
    matches = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        if target_string in f.read():
                            matches.append(file_path)
                            print(f"Found match: {file_path}")
                except:
                    continue
    return matches

if __name__ == "__main__":
    target = "class RetrievalQA"
    for p in sys.path:
        if "site-packages" in p and os.path.isdir(p):
            search_in_path(p, target)
