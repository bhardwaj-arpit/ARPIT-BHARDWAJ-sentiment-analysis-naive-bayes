📁 sentiment-analysis-naive-bayes/
├── backend/
│   └── app/
│       ├── main.py
│       ├── sentiment_model.pkl
│       ├── tfidf_vectorizer.pkl
│       └── utilities.py (if any)
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
├── data/
│   └── product_reviews.csv
├── generate_reviews.py
├── sentiment_analysis.py
├── README.md ✅

📄 README.md (Main Project Description)
Here's your complete README.md content — copy and paste it into the root of your repo:

markdown
Copy
Edit
# 📊 Sentiment Analysis of Product Reviews using Naive Bayes

> A complete ML + Web project for IBM & NASSCOM Internship

## 👨‍💻 Author
**Arpit Bhardwaj**  
GitHub: [bhardwaj-arpit](https://github.com/bhardwaj-arpit)

---

## 📌 Project Overview

This project performs **sentiment analysis** on customer product reviews using:
- **Machine Learning** (Multinomial Naive Bayes)
- **Natural Language Processing (NLP)**
- **FastAPI** backend
- **React.js** frontend

It classifies reviews into:
- Positive 😊  
- Negative 😡  
- Neutral 😐  
- Friendly 🤝  
- Critical 🔍  

---

## 📂 Folder Structure

| Folder        | Description                         |
|---------------|-------------------------------------|
| `backend/`    | FastAPI backend + ML model          |
| `frontend/`   | React-based user interface          |
| `data/`       | Training dataset (`product_reviews.csv`) |
| `eda_plots/`  | Optional — EDA charts (if generated) |
| `notebook/`   | Original data sources or JSON       |

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/bhardwaj-arpit/ARPIT-BHARDWAJ-sentiment-analysis-naive-bayes.git
cd ARPIT-BHARDWAJ-sentiment-analysis-naive-bayes
2️⃣ Setup & Run Backend
bash
Copy
Edit
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
FastAPI will run at: http://127.0.0.1:8000/docs

3️⃣ Setup & Run Frontend
bash
Copy
Edit
cd frontend
npm install
npm start
Frontend runs at: http://localhost:3000

🎥 Demo Video
📽️ Click to Watch Demo

💻 Features
Analyze single review texts

Upload CSV/TXT/JSON files

Auto ML classification (Naive Bayes)

Animated and styled React UI

File validation and error handling

⚙️ Technologies Used
Python 3.10+

scikit-learn

NLTK

FastAPI

ReactJS

HTML + CSS + JavaScript

Pandas, Joblib

📊 Model Details
TF-IDF vectorization

Multinomial Naive Bayes

Trained on 2500+ generated + synthetic reviews

5-class classification

Accuracy: ~87%

🧪 Example Output
Input Review:

csharp
Copy
Edit
This phone is fantastic! I love the battery life.
Predicted Sentiment:

mathematica
Copy
Edit
Positive 😊
📥 Datasets
/data/product_reviews.csv (generated using generate_reviews.py)

JSON review samples in /notebook/

✅ Project Status
✅ Frontend: Completed
✅ Backend: Completed
✅ Model Training: Done
✅ Deployment: Local
✅ GitHub: Uploaded
✅ Demo Video: Recorded

📧 Contact
📬 Email: youremail@example.com

📦 GitHub: bhardwaj-arpit

💡 This project was completed as part of the IBM & NASSCOM AICTE Virtual Internship 2025.

yaml
Copy
Edit

---

## 📦 Final Upload Checklist

| ✅ | Task                                        |
|----|---------------------------------------------|
| ✔️ | Code pushed to GitHub                       |
| ✔️ | `README.md` added                           |
| ✔️ | Working demo video uploaded to Drive        |
| ✔️ | Backend trained with dataset (`.pkl` files) |
| ✔️ | `generate_reviews.py` included              |
| ✔️ | Frontend UI styled and working              |
| ✔️ | `/analyze-text/` and `/analyze/` tested     |

---

