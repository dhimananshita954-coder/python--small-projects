import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------------- ML MODEL ----------------

# Training data (Hours studied vs Marks)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([35, 40, 50, 55, 65, 70, 80, 90])

model = LinearRegression()
model.fit(X, y)

# ---------------- GUI FUNCTION ----------------

def predict_marks():
    try:
        hours = float(hours_entry.get())
        prediction = model.predict([[hours]])
        result_label.config(text=f"Predicted Marks: {prediction[0]:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# ---------------- GUI WINDOW ----------------

root = tk.Tk()
root.title("ML Marks Prediction System")
root.geometry("400x300")

# Title
title_label = tk.Label(root, text="Marks Prediction using ML", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input
hours_label = tk.Label(root, text="Enter Hours Studied:")
hours_label.pack()

hours_entry = tk.Entry(root)
hours_entry.pack(pady=5)

# Button
predict_button = tk.Button(root, text="Predict Marks", command=predict_marks)
predict_button.pack(pady=10)

# Output
result_label = tk.Label(root, text="Predicted Marks: ")
result_label.pack(pady=10)

root.mainloop()
