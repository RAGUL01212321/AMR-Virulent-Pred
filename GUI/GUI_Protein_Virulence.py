import tkinter as tk
from tkinter import messagebox
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model(r"C:\Users\uragu\OneDrive\Desktop\AMR_Bio\cnn_bilstm_amr_model.h5")

# Amino acids
AA = "ARNDCQEGHILKMFPSTWYV"

def one_hot_encode(sequence, max_len=200):
    enc = np.zeros((max_len, len(AA)))
    for i, aa in enumerate(sequence[:max_len]):
        if aa in AA:
            enc[i, AA.index(aa)] = 1
    return enc

def predict_amr(sequence):
    encoded = one_hot_encode(sequence)
    encoded = encoded.reshape(1, 200, 20)  # Reshape for model input
    prediction = model.predict(encoded, verbose=0)
    return "🛑 AMR Detected (Resistant)" if prediction[0][0] > 0.5 else "✅ No AMR Detected (Non-resistant)"

# Enhanced Tkinter GUI
def run_gui():
    def on_predict():
        seq = seq_input.get("1.0", tk.END).strip().upper()
        if not seq:
            messagebox.showerror("Error", "Please enter a protein sequence.")
            return
        if any(char not in AA for char in seq):
            messagebox.showerror("Error", "Invalid characters in sequence.")
            return
        result = predict_amr(seq)
        result_label.config(text=result)

    # Main window
    root = tk.Tk()
    root.title("AMR Gene Predictor")
    root.geometry("600x400")
    root.configure(bg="#f0f4f7")

    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"+{x}+{y}")

    # Title
    tk.Label(root, text="AMR Gene Predictor", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#333").pack(pady=10)

    # Sequence label
    tk.Label(root, text="Enter Protein Sequence:", font=("Helvetica", 12), bg="#f0f4f7", fg="#333").pack()

    # Sequence input
    seq_input = tk.Text(root, height=6, width=60, font=("Courier", 11), wrap="word", bd=2, relief="groove")
    seq_input.pack(pady=10)

    # Predict button
    predict_btn = tk.Button(root, text="🔍 Predict AMR", command=on_predict,
                            font=("Helvetica", 12, "bold"), bg="#007acc", fg="white",
                            activebackground="#005f99", activeforeground="white", padx=10, pady=5, bd=0)
    predict_btn.pack(pady=5)

    # Result label
    result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f0f4f7", fg="#444")
    result_label.pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
