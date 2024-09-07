
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete")
 
def mark_as_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, f"{task} (Completed)")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed !")

def on_select(event):
    # Reset the color of all items
    for i in range(listbox.size()):
        listbox.itemconfig(i, {'bg':'white'})
    
    # Highlight the selected item
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.itemconfig(selected_task_index, {'bg':'yellow'})
    except IndexError:
        pass

    
# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the GUI components
frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

entry = tk.Entry(frame, width=20 , font="Arial 24")
entry.pack(pady=10)



listbox = tk.Listbox(frame, width=40, height=15, bg="cyan" , font=16 , selectmode=tk.SINGLE)
listbox.pack(pady=10)

listbox.bind('<<ListboxSelect>>', on_select)


add_button = tk.Button(frame, text="Add Task", font ="lucida" , command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(frame, text="Delete Task", font="lucida", command=remove_task)
remove_button.pack(pady=5)

complete_button = tk.Button(frame, text="Mark as Completed", font="lucida" , command=mark_as_completed)
complete_button.pack(pady=5)

# Run the application
root.mainloop()
