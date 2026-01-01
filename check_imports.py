"""
check_imports.py
Created: 2026-01-01T11:29:00+09:00
Test LangChain imports one by one.
"""
import sys

def test_import(module_name):
    try:
        __import__(module_name)
        print(f"[v] {module_name} imported successfully.")
    except ImportError as e:
        print(f"[!] {module_name} import failed: {e}")

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    modules = [
        "langchain",
        "langchain.chains",
        "langchain.prompts",
        "langchain_community",
        "langchain_google_genai",
        "langchain_text_splitters"
    ]
    for mod in modules:
        test_import(mod)
