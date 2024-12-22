import tkinter as tK

root = tK.Tk()
root.title("Tkinter")

# Using grid() for all widgets
button1 = tK.Button(root, text="Button1")
button2 = tK.Button(root, text="Button2")
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)

name = tK.Label(root, text="Name")
name.grid(row=0, column=0)
e1 = tK.Entry(root)
e1.grid(row=0, column=1)

submit = tK.Button(root, text="Submit")
submit.grid(row=2, column=0, columnspan=2)

root.mainloop()
