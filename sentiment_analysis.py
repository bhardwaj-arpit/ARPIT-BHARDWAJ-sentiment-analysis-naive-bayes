import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Set up directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
EDA_DIR = os.path.join(BASE_DIR, 'eda_plots')
BACKEND_DIR = os.path.join(BASE_DIR, 'backend/app')
os.makedirs(EDA_DIR, exist_ok=True)
os.makedirs(BACKEND_DIR, exist_ok=True)

# Load dataset
print("Loading dataset...")
df = pd.read_csv(os.path.join(DATA_DIR, 'product_reviews.csv'))
print(f"Original dataset size: {len(df)}")

# Deduplicate dataset
df = df.drop_duplicates(subset=['reviewText'])
print(f"Dataset size after deduplication: {len(df)}")

# EDA: Class Distribution
print("\nPerforming EDA: Class Distribution")
plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment', hue='Sentiment', data=df, palette='viridis', legend=False)
plt.title('Sentiment Class Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig(os.path.join(EDA_DIR, 'class_distribution.png'))
plt.close()
print("Class distribution saved to eda_plots/class_distribution.png")
print(df['Sentiment'].value_counts())

# EDA: Review Length Analysis
print("\nPerforming EDA: Review Length Analysis")
df['ReviewLength'] = df['reviewText'].apply(len)
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='ReviewLength', hue='Sentiment', multiple='stack', bins=20)
plt.title('Review Length Distribution by Sentiment')
plt.xlabel('Review Length (Characters)')
plt.ylabel('Count')
plt.savefig(os.path.join(EDA_DIR, 'review_length_distribution.png'))
plt.close()
print("Review length distribution saved to eda_plots/review_length_distribution.png")
print(df.groupby('Sentiment')['ReviewLength'].describe())

# EDA: Word Cloud for Each Sentiment
print("\nPerforming EDA: Word Clouds")
for sentiment in df['Sentiment'].unique():
    text = ' '.join(df[df['Sentiment'] == sentiment]['reviewText'].values)
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Word Cloud for {sentiment} Reviews')
    plt.axis('off')
    plt.savefig(os.path.join(EDA_DIR, f'wordcloud_{sentiment.lower()}.png'))
    plt.close()
    print(f"Word cloud for {sentiment} saved to eda_plots/wordcloud_{sentiment.lower()}.png")

# Preprocess Text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

print("\nPreprocessing text...")
df['CleanedText'] = df['reviewText'].apply(preprocess_text)
print("Text preprocessing completed.")

# Train Naive Bayes Model
print("\nTraining Naive Bayes model...")
X = df['CleanedText']
y = df['Sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=10000)  # Increased for better performance
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluate model
y_pred = model.predict(X_test_tfidf)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model and vectorizer
with open(os.path.join(BACKEND_DIR, 'sentiment_model.pkl'), 'wb') as f:
    pickle.dump(model, f)
with open(os.path.join(BACKEND_DIR, 'tfidf_vectorizer.pkl'), 'wb') as f:
    pickle.dump(vectorizer, f)
print(f"Model and vectorizer saved to {BACKEND_DIR}/")