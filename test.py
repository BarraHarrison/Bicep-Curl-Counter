# Tkinter test code to see if it works on my MacOS
import tkinter as tk

def on_click():
    print("Tkinter Button Clicked!")

root = tk.Tk()
root.title("Tkinter MacOS Test")
root.geometry("400x400")

btn = tk.Button(root, text="Click me", command=on_click, bg="lightblue", font=("Arial", 12))
btn.pack(pady=20)

root.mainloop()