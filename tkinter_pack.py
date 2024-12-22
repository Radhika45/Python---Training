import tkinter as tK

root = tK.Tk()
root.title("Tkinter")

button1 = tK.Button(root, text = "Button1")
button2 = tK.Button(root, text = "Button2")

button1.pack()
button2.pack()


root.mainloop()