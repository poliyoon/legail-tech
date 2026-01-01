"""
test_model_init.py
Created: 2026-01-01T12:26:00+09:00
Independently test LegalAdvisorModel initialization with Gemini.
"""
import os
import sys
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.getcwd())

def test_init():
    load_dotenv()
    print("Starting LegalAdvisorModel (Gemini) initialization test...")
    
    try:
        from models.legal_advisor_model import LegalAdvisorModel
        
        # Ensure API KEY is set
        if not os.getenv("GOOGLE_API_KEY"):
            print("[!] GOOGLE_API_KEY not set.")
            return

        model = LegalAdvisorModel()
        print("[v] Model initialized successfully.")
        
        # Test a full advice generation (including LLM call)
        print("Testing full advice generation (this will call Gemini API)...")
        question = "층간소음 해결 방법이 뭐야?"
        advice = model.get_advice(question)
        print(f"[v] Advice generated successfully:\n{advice[:200]}...")
        
    except Exception as e:
        print(f"[X] Critical Error during test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_init()
