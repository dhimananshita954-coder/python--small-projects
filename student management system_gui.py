import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x450")

# Labels
tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Marks").pack()
marks_entry = tk.Entry(root)
marks_entry.pack()

# Student list
student_list = tk.Listbox(root, width=40)
student_list.pack(pady=10)

# Add student function
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()

    if name == "" or roll == "" or marks == "":
        messagebox.showwarning("Error", "All fields are required")
        return

    student_list.insert(tk.END, f"Name: {name}, Roll: {roll}, Marks: {marks}")

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

# Delete student function
def delete_student():
    selected = student_list.curselection()
    if selected:
        student_list.delete(selected)
    else:
        messagebox.showwarning("Error", "Select a student to delete")

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

# Run app
root.mainloop()