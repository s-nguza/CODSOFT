from tkinter import *
from tkinter import messagebox



def add_task():
    """ this function adds a task to the to-do list displayed in the table Listbox widget if the user has entered a task. Otherwise, it displays a warning message."""

    task = TaskField.get()
    if task:
        table.insert(END, task.upper())
        TaskField.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = table.curselection()[0]
        table.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    selected_task_index = table.curselection()
    if selected_task_index:
        selected_task = table.get(selected_task_index)
        TaskField.delete(0, END)
        TaskField.insert(0, selected_task)
        table.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning","Please select a task to edit")

def mark_completed():
    try:
        index = table.curselection()[0]
        table.itemconfig(index, bg="light gray")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = table.get(0, END)
        for task in tasks:
            file.write(task + "\n")


root = Tk()
root.configure(bg='light blue')  
root.title("To-Do-List")

# Frame for entry field and add button
frame_entry = Frame(root)
frame_entry.pack(pady=10)

TaskField = Entry(frame_entry)
TaskField.pack(side=LEFT)

button = Button(frame_entry, text="Add Task", font="lucida 13", fg="white", bg="black", command=add_task)
button.pack(side=LEFT)

# Table
label_heading = Label(root, text="TO-DO-LIST", font=('arial', 14, 'bold'), bg='light blue')
label_heading.pack()
frame_table = Frame(root, bd=3, width=600, height=18)
frame_table.pack(pady=(5, 0))
table = Listbox(frame_table, font=('arial', 12), width=40, height=16, cursor="hand2", selectbackground="Yellow")
table.pack(side="left", fill=BOTH, padx=2)
table.configure(bg='silver')  


scrollbar = Scrollbar(frame_table)
scrollbar.pack(side="right", fill=Y)

table.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=table.yview)

# Delete button
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

delete_Button = Button(frame_buttons, text="Delete Task", font="lucida 13", fg="white", bg="red", command=delete_task)
delete_Button.pack(side=LEFT)

editing_Button = Button(frame_buttons, text="Edit Task", font="lucida 13", fg="white", bg="blue", command=edit_task)
editing_Button.pack(side=LEFT)

root.mainloop()