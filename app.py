# Graphical User Interface (GUI)
import tkinter as tk 


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bicep-Curl Counter")
        self.window.geometry("600x400")
        self.window.configure(bg="white")

        print("Tkinter is working!")

        self.label = tk.Label(self.window, text="Tkinter is working!", font=("Arial", 16), bg="white")
        self.label.pack(pady=20)

        self.window.mainloop()

if __name__ == "__main__":
    App()