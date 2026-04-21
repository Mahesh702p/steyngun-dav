# # Text Analytics - Variant 2: Sentiment Analysis
# # Classify text as positive/negative using TextBlob

# import pandas as pd
# from textblob import TextBlob

# # ============ CHANGE THESE ============
# FILENAME = "data.csv"
# TEXT_COL = "text"
# # ======================================

# # --- Load ---
# df = pd.read_csv(FILENAME)
# print(f"Loaded {len(df)} rows")

# # --- Sentiment ---
# def get_sentiment(text):
#     if pd.isna(text):
#         return "Neutral", 0
#     blob = TextBlob(str(text))
#     polarity = blob.sentiment.polarity
#     if polarity > 0:
#         return "Positive", polarity
#     elif polarity < 0:
#         return "Negative", polarity
#     else:
#         return "Neutral", polarity

# df["Sentiment"], df["Polarity"] = zip(*df[TEXT_COL].apply(get_sentiment))

# # --- Results ---
# print("\n--- Sentiment Distribution ---")
# print(df["Sentiment"].value_counts())
# print(f"\nAverage Polarity: {df['Polarity'].mean():.4f}")

# print("\n--- Sample Results ---")
# print(df[[TEXT_COL, "Sentiment", "Polarity"]].head(10).to_string())



import pandas as pd
from textblob import TextBlob

df = pd.read_csv("data.csv")

# 1. Function to get only polarity
def get_pol(t):
    return TextBlob(str(t)).sentiment.polarity

# 2. Apply and classify
df["pol"] = df["text"].apply(get_pol)
df["sent"] = df["pol"].apply(lambda x: "Pos" if x > 0 else ("Neg" if x < 0 else "Neu"))

print(df[["text", "sent"]].head())
