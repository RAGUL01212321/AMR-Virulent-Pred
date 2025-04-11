import tkinter as tk
from tkinter import filedialog, messagebox

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select DNA Sequence File",
        filetypes=(("Text Files", "*.txt"), ("FASTA Files", "*.fasta"), ("All Files", "*.*"))
    )
    if file_path:
        input_label.config(text=f"Selected file:\n{file_path}")
        # You can store the path or process the file here

def predict_amr():
    # Placeholder for your model prediction logic
    messagebox.showinfo("Prediction", "Prediction logic will run here.")

# GUI Window
root = tk.Tk()
root.title("AMR 1.0 - Gene Predictor")
root.geometry("400x300")
root.config(bg="#f4f4f4")

# Title
title_label = tk.Label(root, text="AMR 1.0", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Upload Button
upload_btn = tk.Button(root, text="Upload DNA Sequence", command=upload_file, width=25)
upload_btn.pack(pady=10)

# Display File Name
input_label = tk.Label(root, text="No file selected", bg="#f4f4f4")
input_label.pack(pady=5)

# Predict Button
predict_btn = tk.Button(root, text="Predict", command=predict_amr, width=20, bg="#4CAF50", fg="white")
predict_btn.pack(pady=20)

root.mainloop()
