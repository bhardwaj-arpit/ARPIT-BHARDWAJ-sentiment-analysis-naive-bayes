import React, { useState } from "react";
import axios from "axios";
import ResultDisplay from "./ResultDisplay";

const SentimentForm = () => {
  const [file, setFile] = useState(null);
  const [review, setReview] = useState("");
  const [result, setResult] = useState(null);
  const [results, setResults] = useState([]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null); // reset
  };

  const handleUpload = async () => {
    if (!file) return alert("Please upload a file.");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:8000/analyze/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      if (Array.isArray(response.data)) {
        setResults(response.data); // 👈 expects array of { reviewText, PredictedSentiment }
        setResult(null);
      } else {
        setResults([]);
        alert("Unexpected response format from server.");
      }
    } catch (error) {
      console.error("File upload error:", error);
      alert("Failed to analyze file.");
    }
  };

  const handleReviewAnalyze = async () => {
    if (!review.trim()) {
      return alert("Please enter a review.");
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/analyze-text/", {
        review: review.trim(),
      });

      if (response.data.result) {
        setResult(response.data.result); // ✅ set single review result
        setResults([]); // clear batch results
      } else {
        alert("Unexpected response from server.");
      }
    } catch (error) {
      console.error("Text analysis error:", error);
      alert("Failed to analyze review. Ensure backend is running.");
    }
  };

  return (
    <div className="container">
      <h1>Sentiment Analysis</h1>

      <div>
        <label>
          Upload File (CSV/JSON/TXT):
          <input type="file" onChange={handleFileChange} />
        </label>
        <button onClick={handleUpload}>Analyze File</button>
      </div>

      <div>
        <h2>Or Enter a Review:</h2>
        <textarea
          placeholder="Type your review here"
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />
        <button onClick={handleReviewAnalyze}>Analyze Review</button>
      </div>

      <ResultDisplay result={result} results={results} />
    </div>
  );
};

export default SentimentForm;
