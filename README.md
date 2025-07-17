# CareerLens AI – Resume Analyzer and Career Recommender

CareerLens is a lightweight AI-powered web app that analyzes a resume and recommends career alternatives based on the skills and technologies it detects. It’s designed to give quick, meaningful insights to users who want to explore potential job roles that align with their experience and interests.

I built this project as a student passionate about AI and machine learning, aiming to create something that feels useful, intentional, and actually works — not just another static portfolio piece.

## Features

- Upload a PDF resume and extract its content using PyMuPDF
- Analyze the text and detect relevant keywords using TF-IDF
- Match skills against a custom-built role-skill database
- Recommend top 3 suitable job roles based on the resume content
- Explain the reason for each recommendation using matched skills
- Simple, clean user interface with a touch of modern styling
- 
## Tech Stack

- **Language**: Python
- **Libraries**: PyMuPDF, scikit-learn, pandas, Streamlit
- **Frontend**: Built using Streamlit with embedded HTML and CSS
- **Deployment**: GitHub, Streamlit Cloud (planned)

## Why I Built It

As a computer science student studying AI and ML, I wanted to create something that blends what I've learned with a real-world use case. Most resume analyzers either feel generic or overloaded with features. My goal was to keep it minimal, clean, and clear — while still using core AI concepts.

This project also helped me understand how to bring together different areas I’ve been learning: text processing, machine learning logic, user interface design, and deployment.

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/Sivasaithanmai/CareerLens.git
cd CareerLens

Install the dependencies:

Make sure Python is installed, then run:
pip install -r requirements.txt

Launch the app:
streamlit run app.py

The app will open in your browser where you can upload your resume and see the recommendations.

Creating requirements.txt:

If you're editing or extending the project, you can regenerate the dependencies file:
pip freeze > requirements.txt

Future Improvements:
Use NLP libraries like spaCy or BERT for more intelligent text understanding

Build a recommendation engine using real job market data

Store and compare multiple resumes in a user dashboard

Add authentication and history tracking

Deploy the live version publicly for free use

About Me:
I’m a student of Computer Science with a focus on AI and ML.
I enjoy building tools that solve real problems, experimenting with design, and bringing ideas to life with code.
This project reflects the skills I’ve learned and where I’m headed next.

Contact
If you'd like to connect, suggest feedback, or collaborate, feel free to reach out.

GitHub: Sivasaithanmai
LinkedIn: LinkedIn: [thanmai-c](https://www.linkedin.com/in/thanmai-c-84b49927b)
Email: thanmaichandrahas86@gmail.com
