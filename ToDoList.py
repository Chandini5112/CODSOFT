from tkinter import *
import tkinter.messagebox

def entertask():
    #A new window to pop up to take input
    input_text = ""
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title = "Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1 = Tk()
    root1.title("Add Task")
    #Entry widget to take input
    entry_task = Text(root1, height = 5,width = 30)
    entry_task.pack(pady=20)
    #Button widget
    add_button=Button(root1,text="Add", command = add)
    add_button.pack(pady=10)
    root1.mainloop()

def deletetask():
    try:
        task_index=listbox_task.curselection()
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="No Task Selected")

def markcompleted():
    try:
        task_index=listbox_task.curselection()
        task=listbox_task.get(task_index)
        file=open("done.txt","a")
        file.write(task+"\n")
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="No Task Selected")

#creating the initial window
window=Tk()
#giving a title
window.title("DataFlair Python To-Do List APP")

#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()

#to hold items in a listbox
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font = "Helvetica")
listbox_task.pack(side = LEFT)

#creating a scrollbar
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side = RIGHT,fill = Y)

#linking the scrollbar with the listbox
listbox_task.config(yscrollcommand = scrollbar_task.set)
scrollbar_task.config(command = listbox_task.yview)

#Button widget
entry_button=Button(window,text = "Add task", width = 50, command = entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete selected task",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as completed ",width=50,command=markcompleted)
mark_button.packpady=3


window.mainloop()