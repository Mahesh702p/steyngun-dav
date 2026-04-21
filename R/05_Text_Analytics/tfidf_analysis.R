# Text Analytics - Variant 3: TF-IDF in R

# ============ CHANGE THESE ============
FILENAME <- "data.csv"
TEXT_COL <- "text"
# ======================================

library(tm)

# --- Load ---
df <- read.csv(FILENAME, stringsAsFactors = FALSE)
cat("Loaded", nrow(df), "rows\n")

# --- Create Corpus ---
corpus <- VCorpus(VectorSource(df[[TEXT_COL]]))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stripWhitespace)

# --- TF-IDF Matrix ---
tfidf_matrix <- DocumentTermMatrix(corpus, control = list(weighting = weightTfIdf))
tfidf_scores <- sort(colMeans(as.matrix(tfidf_matrix)), decreasing = TRUE)

# --- Top 20 TF-IDF Terms ---
cat("\n--- Top 20 TF-IDF Terms ---\n")
top20 <- head(tfidf_scores, 20)
for (i in seq_along(top20)) {
  cat(" ", names(top20)[i], ":", round(top20[i], 4), "\n")
}
