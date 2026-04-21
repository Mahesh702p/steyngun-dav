# Text Analytics — R

## What It Is
Three text analysis variants using R packages.

### 1. Word Frequency (`word_frequency.R`) — uses `tm`
### 2. Sentiment Analysis (`sentiment_analysis.R`) — uses `syuzhet`
### 3. TF-IDF (`tfidf_analysis.R`) — uses `tm`

## Libraries Needed
```r
install.packages("tm")
install.packages("syuzhet")
```

## How to Adapt
Change `FILENAME` and `TEXT_COL` in whichever script you use.

## After Internet
- Install packages and run
- For word frequency, add a bar plot:
```r
barplot(head(freq, 10), las=2, main="Top 10 Words", col="steelblue")
```

## Tip
`tm` is R's standard text mining library. If sir asks why `tm`: "It provides a standardized pipeline — corpus creation, preprocessing, and term-document matrices."
