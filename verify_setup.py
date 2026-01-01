"""
verify_setup.py
Created: 2026-01-01T11:25:00+09:00
Diagnostic script to check environment and model initialization.
"""
import os
import sys
from dotenv import load_dotenv

def verify():
    print("--- Diagnostic Report ---")
    
    # 1. Check .env and API Key
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("[!] GEMINI_API_KEY is missing or not set in .env")
    else:
        print("[v] GEMINI_API_KEY is present.")

    # 2. Check Directory Structure
    for folder in ["models", "data", "utils"]:
        if os.path.isdir(folder):
            print(f"[v] Directory '{folder}/' exists.")
        else:
            print(f"[!] Directory '{folder}/' is missing.")

    # 3. Test Imports and Model Initialization
    try:
        from models.legal_advisor_model import LegalAdvisorModel
        print("[v] Successfully imported LegalAdvisorModel.")
        
        # Test initialization (this will download embeddings if not present)
        print("Initializing LegalAdvisorModel (this may take a moment)...")
        # model = LegalAdvisorModel() # Uncomment to test full initialization if API key is valid
        # print("[v] LegalAdvisorModel initialized successfully.")
    except ImportError as e:
        print(f"[!] Import error: {e}")
    except Exception as e:
        print(f"[!] Error during initialization: {e}")

if __name__ == "__main__":
    verify()
