from utils.resume_parser import parse_resume
from utils.jd_parser import parse_job_description

def calculate_match(resume_text: str, jd_text: str) -> dict:
    """
    Compare resume and JD to calculate ATS match percentage using Gemini Pro Vision (simulated).
    """
    resume_data = parse_resume(resume_text)
    jd_data = parse_job_description(jd_text)

    matched_skills = set(resume_data["skills"]).intersection(jd_data["keywords"])
    score = round((len(matched_skills) / len(jd_data["keywords"])) * 100, 2) if jd_data["keywords"] else 0

    return {
        "score": score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(set(jd_data["keywords"]) - set(resume_data["skills"]))
    }
