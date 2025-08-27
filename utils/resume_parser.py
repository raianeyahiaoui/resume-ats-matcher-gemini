import re

def parse_resume(resume_text: str) -> dict:
    """
    Extracts basic sections from resume text such as education, skills, and experience.
    """
    sections = {
        "education": re.findall(r"(Bachelor|Master|PhD|Degree|University).*", resume_text, re.IGNORECASE),
        "skills": re.findall(r"(Python|Java|C\+\+|SQL|AI|ML|Deep Learning|Data Science).*", resume_text, re.IGNORECASE),
        "experience": re.findall(r"(Engineer|Developer|Manager|Intern|Research).*", resume_text, re.IGNORECASE)
    }
    return sections
