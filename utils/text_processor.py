"""
utils/text_processor.py
Created: 2026-01-01T11:21:00+09:00
"""

import re

def clean_text(text: str) -> str:
    """
    Cleans legal text by removing extra spaces, newlines, and special characters.
    """
    if not text:
        return ""
    # Replace multiple spaces/newlines with single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    return text.strip()

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    """
    Splits text into chunks of roughly chunk_size characters with some overlap.
    """
    chunks = []
    if not text:
        return chunks
        
    start = 0
    text_len = len(text)
    
    while start < text_len:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
        
    return chunks
