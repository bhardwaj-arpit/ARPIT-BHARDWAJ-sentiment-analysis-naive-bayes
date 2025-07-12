// src/App.js
import React, { useState } from "react";
import SentimentForm from "./components/SentimentForm";
import ResultDisplay from "./components/ResultDisplay";
import "./index.css";

function App() {
  const [results, setResults] = useState([]);
  const [singleResult, setSingleResult] = useState(null);

  return (
    <div className="container">
      <h1>🎯 Sentiment Analysis</h1>
      <SentimentForm setResults={setResults} setSingleResult={setSingleResult} />
      <ResultDisplay results={results} singleResult={singleResult} />
    </div>
  );
}

export default App;
