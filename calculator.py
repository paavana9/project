import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root)
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", height=2, width=5)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
    frame.pack()

root.mainloop()
