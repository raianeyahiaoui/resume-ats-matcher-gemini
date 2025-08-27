import re

def parse_job_description(jd_text: str) -> dict:
    """
    Extracts keywords and required skills from a job description.
    """
    keywords = re.findall(r"\b[A-Za-z]+\b", jd_text.lower())
    return {
        "keywords": list(set(keywords))
    }
