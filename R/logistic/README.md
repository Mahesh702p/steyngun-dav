# Logistic Regression — R

## What It Is
Binary classification using `glm()` with `family = binomial`. Predicts probability (0-1) and classifies based on 0.5 threshold.

## Key Concepts
- `glm()` = generalized linear model; `family = binomial` makes it logistic
- `type = "response"` in predict gives probabilities, not log-odds
- Confusion matrix: rows = predicted, columns = actual

## Libraries Needed
**NONE** — `glm()` is base R.

## How to Adapt
1. Change `FILENAME` and `TARGET`
2. Target must be binary (0/1). If text labels, convert first:
   ```r
   df$target <- ifelse(df$target == "Yes", 1, 0)
   ```

## After Internet
- Install `caret` for a more detailed confusion matrix:
```r
install.packages("caret")
library(caret)
confusionMatrix(factor(y_pred), factor(y_actual))
```
