import React from "react";

const emojiMap = {
  Positive: "😊👍",
  Negative: "😡👎",
  Neutral: "😐",
  Critical: "⚠️",
  Friendly: "🤝",
};

const ResultDisplay = ({ result, results }) => {
  const renderSingle = () => {
    if (!result) return null;
    return (
      <div className="result-block">
        <h2>Analysis Results</h2>
        <p>
          <strong>Sentiment:</strong> {result}{" "}
          <span className="emoji">{emojiMap[result] || "🤔"}</span>
        </p>
      </div>
    );
  };

  const renderFileResults = () => {
    if (!Array.isArray(results) || results.length === 0) return null;

    return (
      <div className="result-block">
        <h2>Analysis Results</h2>
        {results.map((item, index) => (
          <div key={index} className="result-item">
            <p>
              <strong>Review:</strong> {item.reviewText}
            </p>
            <p>
              <strong>Sentiment:</strong> {item.PredictedSentiment}{" "}
              <span className="emoji">{emojiMap[item.PredictedSentiment] || "🤔"}</span>
            </p>
            <hr />
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="container">
      {renderSingle()}
      {renderFileResults()}
    </div>
  );
};

export default ResultDisplay;
