# AI Job Assistant

AI Job Assistant is a practical Python and Streamlit application that analyzes a candidate's resume against a job description.

## Features

- Upload a resume in PDF format
- Extract skills from the resume
- Analyze a job description
- Calculate a Job Match Score
- Identify matched skills
- Identify missing skills
- Recommend skills to learn
- Provide resume improvement suggestions

## Tech Stack

- Python
- Streamlit
- PyPDF
- PDF text extraction
- Rule-based skill matching

## How It Works

1. Upload your resume in PDF format.
2. Paste the job description.
3. Click *Analyze Resume*.
4. The application compares skills found in the resume with skills required in the job description.
5. It displays the match score, matched skills, missing skills, and recommendations.

## Run Locally

Install the required packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Project Structure

AI_Job_Assistant/
- app.py
- requirements.txt
- README.md

## Future Improvements

- AI-powered resume recommendations
- More advanced NLP-based skill extraction
- Resume ranking
- Job-specific interview question generation
- Integration with job-search APIs

## Author

Kartikey