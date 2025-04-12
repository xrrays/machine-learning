## 🎮 Steam Review Sentiment Analysis with Metacritic Comparison | Machine Learning
This notebook performs sentiment analysis on Steam game reviews using three machine learning models:
- Multinomial Naive Bayes (Linear)
- Random Forest (Non-linear)
- SVM with RBF kernel (Non-linear)

It uses two datasets:
- **Steam Reviews Dataset**: A dataset containing raw reviews with language, game title, and a "recommended" label.
   - https://www.kaggle.com/datasets/najzeko/steam-reviews-2021/data
- **Metacritic Dataset**: A dataset with critic and user scores per game.
   - https://www.kaggle.com/datasets/thedevastator/video-game-ratings-and-reviews-dataset

### 🔄 Workflow Overview:
1. Load and input data from datasets using `config.json`
2. Clean and pre-process reviews (balance and filter reviews for model evaluation)
2. Vectorize text using TF-IDF
3. Train/test split + model training
4. Evaluate models (accuracy, precision, recall, F1, confusion matrix)
5. Compare model-predicted sentiment vs actual Metacritic scores (correlation + graphs)
6. Bonus insights:
   - Most common positive/negative words
   - Random review samples (with model correctness for error analysis)

### ⚙️ How to Use:
- No setup needed beyond having `config.json` and the datasets in **your** right file path
- Simply run each cell in order
