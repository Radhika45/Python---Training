import tkinter as tk

# Function to change colors
def change_to_red():
    root.config(bg="red")
    label.config(fg="white", bg="red")

def change_to_green():
    root.config(bg="green")
    label.config(fg="black", bg="green")

def change_to_blue():
    root.config(bg="blue")
    label.config(fg="yellow", bg="blue")

# Create the main window
root = tk.Tk()
root.title("Color Changer")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Click a button to change colors", font=("Arial", 14))
label.pack(pady=20)

# Create buttons
button_red = tk.Button(root, text="Red", command=change_to_red, bg="red", fg="white")
button_red.pack(pady=5)

button_green = tk.Button(root, text="Green", command=change_to_green, bg="green", fg="black")
button_green.pack(pady=5)

button_blue = tk.Button(root, text="Blue", command=change_to_blue, bg="blue", fg="yellow")
button_blue.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()