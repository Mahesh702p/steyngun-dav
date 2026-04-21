# Text Analytics - Variant 3: TF-IDF Analysis
# Find the most important/unique words in documents

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# ============ CHANGE THESE ============
FILENAME = "data.csv"
TEXT_COL = "text"
# ======================================

# --- Load ---
df = pd.read_csv(FILENAME)
print(f"Loaded {len(df)} rows")

# --- TF-IDF ---
tfidf = TfidfVectorizer(stop_words='english', max_features=20)
tfidf_matrix = tfidf.fit_transform(df[TEXT_COL].dropna())

# --- Top TF-IDF terms ---
feature_names = tfidf.get_feature_names_out()
avg_tfidf = tfidf_matrix.toarray().mean(axis=0)

tfidf_scores = sorted(zip(feature_names, avg_tfidf), key=lambda x: x[1], reverse=True)
print("\n--- Top 20 TF-IDF Terms ---")
for term, score in tfidf_scores:
    print(f"  {term}: {score:.4f}")

# --- Show TF-IDF for first document ---
print("\n--- TF-IDF for First Document ---")
first_doc = tfidf_matrix[0].toarray().flatten()
doc_terms = sorted(zip(feature_names, first_doc), key=lambda x: x[1], reverse=True)
for term, score in doc_terms[:10]:
    if score > 0:
        print(f"  {term}: {score:.4f}")

"""
# --- CLEAN & PERFECT TF-IDF ---
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data.csv")
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df["text"].dropna())

# Get feature names and average scores
scores = matrix.toarray().mean(axis=0)
words = tfidf.get_feature_names_out()

# Print top 10
print(sorted(zip(words, scores), key=lambda x: x[1], reverse=True)[:10])
"""
