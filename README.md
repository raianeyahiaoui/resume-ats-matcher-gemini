# 🤖 Resume ATS Matcher with Gemini Pro Vision

An **AI-powered Applicant Tracking System (ATS) Matcher** that helps candidates and recruiters evaluate resume–job description compatibility.  
Built with **Gemini Pro Vision**, it parses resumes, extracts job requirements, and provides a **match score** with detailed feedback.

---

## 📸 Demo Screenshot
![Automatic Applicant Tracking System (ATS)](assets/Automatic%20Applicant%20Tracking%20System%20(ATS).png)

---

## 🚀 Problem
Applying to jobs is stressful:  
- Recruiters get thousands of resumes.  
- Candidates don’t know why their resumes fail.  
- Traditional ATS tools are rigid and keyword-based.  

---

## 💡 Approach
- Parse resumes (PDF/DOCX) and extract structured information.  
- Parse job descriptions for key skills and requirements.  
- Apply **Gemini Pro Vision** to semantically match candidate profiles with job requirements.  
- Provide scoring + actionable feedback to improve resumes.  

---

## ✨ Innovation
- Uses **multimodal AI (Gemini Pro Vision)** to analyze both text & structured data.  
- Context-aware matching, not just keyword counting.  
- Transparent scoring with feedback to help candidates **optimize resumes**.  
- Interactive **Streamlit app** for easy usage.  

---

## 🛠️ Tech Stack
- Python  
- Streamlit  
- Google Gemini Pro Vision  
- spaCy / NLTK (text preprocessing)  
- Pandas & Regex (resume parsing)  

---

## 📂 Project Structure
utils/ # Core utilities
│ ├── resume_parser.py # Extract text & structure from resumes
│ ├── jd_parser.py # Extract keywords from Job Descriptions
│ ├── matcher_engine.py # Gemini Pro Vision pipeline for ATS scoring
│ └── text_processing.py # Cleaning & preprocessing
│
├── app.py # Streamlit app entry point
├── requirements.txt # Dependencies


---

## ▶️ Run Locally


# Clone the repository
git clone https://github.com/raianeyahiaoui/resume-ats-matcher-gemini.git
cd resume-ats-matcher-gemini

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


📬 Contact

For more details or collaboration, feel free to reach out:

📧 Email: ikba.kin2015@gmail.com

🔗 LinkedIn: Yahiaoui Raiane
