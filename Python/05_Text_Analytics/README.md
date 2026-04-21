# Text Analytics

## What It Is
Extracting meaningful information from text data. Three variants are provided:

### 1. Word Frequency (`word_frequency.py`)
Counts the most common words after removing stop words (the, is, a, etc.)

### 2. Sentiment Analysis (`sentiment_analysis.py`)
Classifies each text as Positive/Negative/Neutral using TextBlob's polarity score (-1 to +1)

### 3. TF-IDF (`tfidf_analysis.py`)
**Term Frequency - Inverse Document Frequency**: finds words that are important in a document but rare across all documents. Better than raw frequency for finding unique/meaningful terms.

## Key Concepts to Mention
- **Tokenization**: splitting text into individual words
- **Stop words**: common words (the, is, and) removed because they don't carry meaning
- **TF-IDF**: TF × IDF — high TF-IDF = word is frequent in this doc but rare overall
- **Polarity**: sentiment score from -1 (very negative) to +1 (very positive)
- **Bag of Words vs TF-IDF**: BoW just counts, TF-IDF weighs by importance

## Libraries Needed
```bash
pip install pandas scikit-learn textblob
python -m textblob.download_corpora   # for sentiment analysis
```

## How to Adapt
1. Change `FILENAME` and `TEXT_COL` in whichever script you need
2. Any CSV with a text column works

## After Internet
- Install libraries, run the script
- For word frequency, show a bar chart:
```python
import matplotlib.pyplot as plt
plt.barh([w for w,c in word_freq[:10]], [c for w,c in word_freq[:10]])
plt.title("Top 10 Words"); plt.show()
```

## Tip
If asked which variant: "Word frequency shows what's talked about most. TF-IDF shows what's uniquely important. Sentiment shows the overall tone."
