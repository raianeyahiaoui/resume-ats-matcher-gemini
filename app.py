import streamlit as st
from utils.matcher_engine import calculate_match
from utils.text_processing import clean_text

st.set_page_config(page_title="Resume ATS Matcher", page_icon="📄")

st.title("📄 Resume ATS Matcher (Gemini Pro Vision)")

resume_input = st.text_area("Paste your Resume Text", height=200)
jd_input = st.text_area("Paste Job Description", height=200)

if st.button("Match Resume"):
    if resume_input and jd_input:
        resume_text = clean_text(resume_input)
        jd_text = clean_text(jd_input)

        result = calculate_match(resume_text, jd_text)

        st.subheader(f"✅ ATS Match Score: {result['score']}%")
        st.write("**Matched Skills:**", result["matched_skills"])
        st.write("**Missing Skills:**", result["missing_skills"])
    else:
        st.warning("⚠️ Please provide both Resume and Job Description text.")
