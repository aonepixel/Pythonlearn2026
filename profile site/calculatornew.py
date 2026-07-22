import tkinter as tk

# Function to update the entry
def press(value):
    entry.insert(tk.END, value)

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, str(result))
    except Exception:
        clear()
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

# Create number/operator buttons
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for button in row:
        if button == "=":
            cmd = calculate
        else:
            cmd = lambda b=button: press(b)

        tk.Button(
            row_frame,
            text=button,
            font=("Arial", 18),
            command=cmd
        ).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    bg="tomato",
    fg="white",
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()