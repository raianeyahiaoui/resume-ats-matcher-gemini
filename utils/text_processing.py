import re

def clean_text(text: str) -> str:
    """
    Clean and preprocess text (remove special characters, newlines, etc.)
    """
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"[^A-Za-z0-9\s]", " ", text)
    return text.lower().strip()
