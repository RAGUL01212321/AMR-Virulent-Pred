import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

# === Load dataset ===
df = pd.read_excel(r"C:\Users\uragu\OneDrive\Desktop\AMR_Bio\Data\Protein v1.1.xlsx")
df = df.dropna(subset=["Sequence", "Class"])
df["Sequence"] = df["Sequence"].astype(str)
sequences = df["Sequence"]
labels = df["Class"].astype(int)

# === k-mer extraction ===
def generate_kmers(seq, k=3):
    return ' '.join([seq[i:i+k] for i in range(len(seq)-k+1)])

df["kmers"] = df["Sequence"].apply(lambda x: generate_kmers(x, k=3))

# === TF-IDF vectorization ===
tfidf = TfidfVectorizer(ngram_range=(1, 2), max_features=8000)
X = tfidf.fit_transform(df["kmers"])
y = labels.values

# === Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# === Train Model ===
model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

# === Predict & Evaluate ===
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"✅ Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test,y_pred))