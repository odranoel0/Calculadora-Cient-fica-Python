import tkinter as tk
import math

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Erro')

def scientific_function(func):
    try:
        value = float(entry.get())
        if func == 'sin':
            result = math.sin(math.radians(value))
        elif func == 'cos':
            result = math.cos(math.radians(value))
        elif func == 'tan':
            result = math.tan(math.radians(value))
        elif func == 'log':
            result = math.log10(value)
        elif func == 'sqrt':
            result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Erro')
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

root = tk.Tk()
root.title("Calculadora Científica")

global entry
entry = tk.Entry(root, width=30, font=("Arial", 14), bd=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('√', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('sin', 4, 4),
    ('cos', 5, 4), ('tan', 6, 4)
]

for (text, row, col)in buttons:
     if text in {'=','C'}:
         action = clear if text == 'C' else calculate
     elif text in {'sin', 'cos', 'tan', 'log', '√'}:
         action = lambda t=text: scientific_function(t if t != '√' else 'sqrt')
     else:
         action = lambda t=text: press(t)
     tk.Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col)
root.mainloop()
