# Graphical User Interface (GUI)
import tkinter as tk 

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bicep-Curl Counter")
        self.window.geometry("400x400")

        print("Tkinter is working!")

        self.label = tk.Label(self.window, text="Bicep-Curl Counter", font=("Arial", 14), bg="black", fg="white")
        self.label.pack(pady=10)

        self.btn = tk.Button(self.window, text="Click here", command=self.on_click, bg="lightblue", font=("Arial", 12))
        self.btn.pack(pady=20)

        self.window.mainloop()

    def on_click(self):
        print("Tkinter button clicked!")

if __name__ == "__main__":
    App()