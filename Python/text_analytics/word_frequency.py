# Text Analytics - Variant 1: Word Frequency Analysis
# Tokenize text, remove stopwords, find most common words

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# ============ CHANGE THESE ============
FILENAME = "data.csv"
TEXT_COL = "text"  # column containing text data
# ======================================

# --- Load ---
df = pd.read_csv(FILENAME)
print(f"Loaded {len(df)} rows")
print(df[TEXT_COL].head())

# --- Word Frequency ---
vectorizer = CountVectorizer(stop_words='english', max_features=20)
word_matrix = vectorizer.fit_transform(df[TEXT_COL].dropna())

# --- Top Words ---
word_counts = word_matrix.toarray().sum(axis=0)
words = vectorizer.get_feature_names_out()

word_freq = sorted(zip(words, word_counts), key=lambda x: x[1], reverse=True)
print("\n--- Top 20 Most Frequent Words ---")
for word, count in word_freq:
    print(f"  {word}: {count}")

"""
# --- CLEAN & PERFECT WORD FREQUENCY ---
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("data.csv")
cv = CountVectorizer(stop_words='english')
matrix = cv.fit_transform(df["text"].dropna())

# Sum occurrences of each word
counts = matrix.toarray().sum(axis=0)
words = cv.get_feature_names_out()

# Print top 10
print(sorted(zip(words, counts), key=lambda x: x[1], reverse=True)[:10])
"""
