import tkinter as tk

def add():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text="Result: " + str(a + b))

def subtract():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text="Result: " + str(a - b))

def multiply():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text="Result: " + str(a * b))

def divide():
    a = float(entry1.get())
    b = float(entry2.get())
    if b != 0:
        result_label.config(text="Result: " + str(a / b))
    else:
        result_label.config(text="Cannot divide by zero")

# Create window
root = tk.Tk()
root.title("Calculator")

# Input fields
entry1 = tk.Entry(root, width=20)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Subtract", command=subtract).pack()
tk.Button(root, text="Multiply", command=multiply).pack()
tk.Button(root, text="Divide", command=divide).pack()

# Result
result_label = tk.Label(root, text="Result:")
result_label.pack()

# Run app
root.mainloop()