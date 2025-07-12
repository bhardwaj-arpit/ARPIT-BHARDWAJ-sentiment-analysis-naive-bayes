from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import logging
import joblib
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Load NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

# CORS (React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and vectorizer
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'sentiment_model.pkl')
VEC_PATH = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.pkl')

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VEC_PATH)
except Exception as e:
    logger.error(f"Error loading model/vectorizer: {e}")
    raise RuntimeError("Model files not found. Please run sentiment_analysis.py.")

# Text preprocessing
def preprocess_text(text):
    try:
        tokens = word_tokenize(text.lower())
        filtered = [w for w in tokens if w not in stop_words and w not in string.punctuation]
        return " ".join(filtered)
    except Exception as e:
        logger.error(f"Preprocessing error: {e}")
        return ""

@app.get("/")
def root():
    return {"message": "Welcome to Sentiment Analysis API"}

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    try:
        ext = file.filename.split('.')[-1].lower()
        if ext == "csv":
            df = pd.read_csv(file.file)
        elif ext == "json":
            df = pd.read_json(file.file)
        elif ext == "txt":
            content = file.file.read().decode("utf-8").splitlines()
            df = pd.DataFrame({"reviewText": content})
        else:
            raise HTTPException(status_code=400, detail="Only CSV, JSON, or TXT files are supported")

        if "reviewText" not in df.columns:
            raise HTTPException(status_code=400, detail="Missing 'reviewText' column.")

        df["CleanedText"] = df["reviewText"].astype(str).apply(preprocess_text)
        X = vectorizer.transform(df["CleanedText"])
        df["PredictedSentiment"] = model.predict(X)

        results = df[["reviewText", "PredictedSentiment"]].to_dict(orient="records")
        return results  # ✅ Return a list, not an object

    except Exception as e:
        logger.error(f"Error in /analyze/: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")

@app.post("/analyze-text/")
async def analyze_text(review: dict):
    try:
        review_text = review.get("review")
        if not review_text or not review_text.strip():
            raise HTTPException(status_code=400, detail="Review text cannot be empty")

        cleaned = preprocess_text(review_text)
        X = vectorizer.transform([cleaned])
        prediction = model.predict(X)[0]
        return {"result": prediction}
    except Exception as e:
        logger.error(f"Error in /analyze-text/: {e}")
        raise HTTPException(status_code=500, detail=f"Error analyzing review: {e}")
