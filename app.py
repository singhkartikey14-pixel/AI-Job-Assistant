import streamlit as st
from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

st.set_page_config(
    page_title="AI Job Assistant",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Job Assistant")
st.write("Analyze your resume against a job description and identify skill gaps.")

st.subheader("Upload Resume")
resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

st.subheader("Job Description")
job_description = st.text_area(
    "Paste the job description here",
    height=200
)
if st.button("Analyze Resume"):

    if resume is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        # Extract text from uploaded PDF
        resume_text = extract_text_from_pdf(resume)

        st.success("Resume analyzed successfully!")

        # Convert text to lowercase
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        # Skills to check
        skills = [
            "python",
            "sql",
            "machine learning",
            "deep learning",
            "nlp",
            "tensorflow",
            "pytorch",
            "scikit-learn",
            "pandas",
            "numpy",
            "git",
            "github",
            "api",
            "streamlit",
            "docker",
            "fastapi",
            "rag",
            "llm",
            "hugging face"
        ]

        # Find skills required in job description
        required_skills = [
            skill for skill in skills
            if skill in job_lower
        ]

        # Find matching skills
        matched_skills = [
            skill for skill in required_skills
            if skill in resume_lower
        ]

        # Find missing skills
        missing_skills = [
            skill for skill in required_skills
            if skill not in resume_lower
        ]

        # Calculate match score
        if required_skills:
            match_percentage = round(
                len(matched_skills) / len(required_skills) * 100
            )
        else:
            match_percentage = 0

        # Display results
        st.header("Analysis Results")

        st.metric("Job Match Score", f"{match_percentage}%")

        st.subheader("Matched Skills")
        if matched_skills:
            st.write(", ".join(matched_skills))
        else:
            st.write("No matching skills found.")

        st.subheader("Missing Skills")
        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.success("No skill gaps detected!")
        st.subheader("Recommendations")

        st.subheader("Resume Improvement Suggestions")

if missing_skills:
    st.write("To improve your resume for this role:")

    for skill in missing_skills:
        st.write(
            f"• If you have experience with {skill.title()}, "
            f"mention it clearly in your Skills or Projects section."
        )

    st.write("• Highlight projects that are most relevant to this job.")
    st.write("• Use relevant keywords from the job description.")

else:
    st.success("Your resume already contains the main skills required for this role.")