# Welcome to Fake News Detector!!

A simple full-stack web application that detects whether a news article is real or fake using a pretrained BERT-based model from Hugging Face.

# Features

- 🧠 NLP model powered by jy46604790/Fake-News-Bert-Detect

- 💬 Paste any article snippet and get instant predictions

- 🌐 Flask backend + HTML/CSS/JS frontend

- ☁️ Fully deployable (Render for backend, Vercel for frontend)

# Demo

🟢 Live App

📽 [Optional: Add demo video or screenshot GIF]

# Model

This project uses a Hugging Face Transformers pipeline based on a fine-tuned BERT model:

Model: jy46604790/Fake-News-Bert-Detect"

Frameworks: PyTorch + Transformers

No training required — the model is loaded directly via API

# 🔬 Custom Model in Progress
I'm actively working on developing a custom-trained model for fake news detection using real-world datasets like Fake and Real News Dataset from Kaggle. This version of the project will involve:
- Data preprocessing (tokenization, stopword removal, etc.)
- Training a lightweight model (e.g., TF-IDF + Logistic Regression or fine-tuned DistilBERT)
- Comparing its performance against the pretrained BERT model currently deployed

# Tech Stack
- Layer	Tool/Tech
- Frontend	HTML, CSS, JavaScript
- Backend	Flask + Flask-CORS + FASTAPI
- ML Inference	Hugging Face Transformers
- Deployment	Render (backend), Vercel (frontend)
 
# 📂 Project Structure
fake-news-detector<br>
<pre>
├── backend/
│   ├── app.py             ← FAST API
│   ├── model.py           ← Hugging Face classifier
│   ├── requirements.txt   ← Dependencies
│   └── Procfile           ← For Render deployment
├── frontend/<br>
│   ├── index.html         ← Web UI + API call logic
│   ├── style.css          ← Styling
├── README.md
└── .gitignore
</pre>

# Local Setup
🔹 Clone the repository
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector

🔹 Set up virtual environment
cd backend
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt

🔹 Run Flask backend
python app.py

🔹 Open frontend

Open frontend/index.html in your browser

## Deployment Guide
🔹 Backend on Render

Push backend/ folder to GitHub

Go to Render

Create new Web Service → Connect GitHub → Pick Python

Set:

Start Command: python app.py

Build Command: pip install -r requirements.txt

🔹 Frontend on Vercel

Push frontend/ to a repo

Go to Vercel

Create project → Import GitHub → Auto deploys static site

Update script.js to point to your backend URL

## Example Input/Output
Input:
NASA confirms presence of alien life on Mars.

Output:
{
  "label": "FAKE",
  "score": 96.82
}

# Future Improvements

Allow scraping from URLs

Provide model confidence visualization

Add explanations via LIME or SHAP

Log predictions for analytics

# Author

Shrish Vishnu Rajesh Kumar
- [GitHub]([url](https://github.com/shrish346))
- [ LinkedIn]([url](https://www.linkedin.com/in/shrish-vishnu-rajesh-kumar-709b9a211/))
