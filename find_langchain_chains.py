"""
find_langchain_chains.py
Created: 2026-01-01T11:35:00+09:00
Search for chains in langchain or langchain_community.
"""
import os
import pkgutil
import importlib

def find_module_in_package(package_name, target):
    try:
        package = importlib.import_module(package_name)
        print(f"Searching in {package_name}...")
        for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
            if target in module_name:
                print(f"Found: {module_name}")
    except Exception as e:
        print(f"Error searching {package_name}: {e}")

if __name__ == "__main__":
    find_module_in_package("langchain", "chains")
    find_module_in_package("langchain_community", "chains")
    
    # Also check if RetrievalQA is directly importable from any known path
    try:
        from langchain.chains import RetrievalQA
        print("Success: from langchain.chains import RetrievalQA")
    except ImportError:
        print("Failed: from langchain.chains import RetrievalQA")
        
    try:
        from langchain_community.chains import RetrievalQA
        print("Success: from langchain_community.chains import RetrievalQA")
    except ImportError:
        print("Failed: from langchain_community.chains import RetrievalQA")
