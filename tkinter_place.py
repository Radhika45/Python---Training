import tkinter as tK

root = tK.Tk()
root.title("Tkinter")
root.geometry("300x200")  # Set window size for better layout control

# Positioning widgets using place()
button1 = tK.Button(root, text="Button1")
button1.place(x=50, y=100)

button2 = tK.Button(root, text="Button2")
button2.place(x=150, y=100)

name = tK.Label(root, text="Name")
name.place(x=20, y=20)

e1 = tK.Entry(root)
e1.place(x=80, y=20)

submit = tK.Button(root, text="Submit")
submit.place(x=100, y=150)

root.mainloop()
