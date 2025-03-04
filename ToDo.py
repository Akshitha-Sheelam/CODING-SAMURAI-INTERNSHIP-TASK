import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found!")

# creates a frame with the given title
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#f4f4f4")

# this code will be giving the title label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# it shows the text feilds of the application
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=5)

# all the operations are written in button formats
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", font=("Arial", 12), command=add_task, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Delete Task", font=("Arial", 12), command=delete_task, bg="#FF5733", fg="white").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Clear All", font=("Arial", 12), command=clear_tasks, bg="#FFC300", fg="black").grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Save Tasks", font=("Arial", 12), command=save_tasks, bg="#3498DB", fg="white").grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Load Tasks", font=("Arial", 12), command=load_tasks, bg="#9B59B6", fg="white").grid(row=0, column=4, padx=5)

# the outline of the listed tasks
task_listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=15, bd=2, relief=tk.RIDGE)
task_listbox.pack(pady=10)

# runs the appliaction
root.mainloop()
