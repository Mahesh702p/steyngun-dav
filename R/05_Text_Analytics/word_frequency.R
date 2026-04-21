# Text Analytics - Variant 1: Word Frequency in R
# Uses tm package for text mining

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

# --- Text Preprocessing ---
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stripWhitespace)

# --- Term-Document Matrix ---
tdm <- TermDocumentMatrix(corpus)
freq <- sort(rowSums(as.matrix(tdm)), decreasing = TRUE)

# --- Top 20 Words ---
cat("\n--- Top 20 Most Frequent Words ---\n")
top20 <- head(freq, 20)
for (i in seq_along(top20)) {
  cat(" ", names(top20)[i], ":", top20[i], "\n")
}
