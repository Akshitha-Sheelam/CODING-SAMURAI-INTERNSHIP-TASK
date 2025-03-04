import tkinter as tk
from tkinter import messagebox

#it indicates the click operations of the buttons
def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

#this code will be indicating the title of the frame
root = tk.Tk()
root.title("Simple Calculator")

#this snippet will stating that the input field of the output
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

#it shows the button arrangements
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                  command=lambda t=text: on_click(t)).grid(row=r, column=c)

#this line indicates the running of the appliaction
root.mainloop()
