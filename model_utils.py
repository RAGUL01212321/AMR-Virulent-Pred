# model_utils.py

import joblib
from collections import Counter
from scipy.stats import entropy
from scipy.sparse import hstack

# === Load the trained model and tools ===
model = joblib.load("xgboost_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
scaler = joblib.load("scaler.pkl")

# === Utility Functions ===

def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) if len(seq) > 0 else 0

def shannon_entropy(seq):
    if len(seq) == 0: return 0
    prob = [n_x / len(seq) for x, n_x in Counter(seq).items()]
    return entropy(prob, base=2)

def generate_kmers(seq, k=6):
    return ' '.join([seq[i:i+k] for i in range(len(seq) - k + 1)]) if len(seq) >= k else seq

# === Main prediction function ===

def predict_amr(sequence):
    sequence = sequence.upper().strip()
    kmers = generate_kmers(sequence)
    tfidf_vec = tfidf.transform([kmers])
    gc = gc_content(sequence)
    length = len(sequence)
    ent = shannon_entropy(sequence)
    handcrafted_scaled = scaler.transform([[gc, length, ent]])
    combined = hstack([tfidf_vec, handcrafted_scaled])
    prediction = model.predict(combined)[0]
    label = "Resistant" if prediction == 1 else "Non-Resistant"
    return label
