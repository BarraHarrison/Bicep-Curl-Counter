# Graphical User Interface (GUI)
import tkinter as tk 
import os 
import PIL.Image, PIL.ImageTk
import cv2 
import camera
import model

class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bicep-Curl Counter")
        self.window.geometry("800x600")
        self.window.configure(bg="gray")

        self.counters = [1, 1]
        self.rep_counter = 0

        self.extended = False
        self.contracted = False
        self.last_prediction = 0

        self.model = model.Model()

        self.counting_enabled = False
        self.camera = camera.Camera()

        self.init_gui()

        self.delay = 15
        self.update()

        self.window.attributes("-topmost", True)
        self.window.update_idletasks()
        self.window.mainloop()

    def init_gui(self):
        print("Initializing GUI...")

        button_style = {"width": 50, "bg": "lightblue", "fg": "black", "font": ("Arial", 12)}

        self.window.configure(bg="gray")

        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=int(self.camera.height * 0.7), bg="red", highlightbackground="black", highlightthickness=3)
        self.canvas.pack(side="top", fill="x")
        print("Canvas created.")

        frame_buttons = tk.Frame(self.window, bg="yellow", height=int(self.camera.height * 0.3), highlightbackground="blue", highlightthickness=3)
        frame_buttons.pack(side="bottom", fill="x", pady=10)

        self.btn_toggleauto = tk.Button(frame_buttons, text="Toggle Counting", command=self.counting_toggle, **button_style)
        self.btn_toggleauto.pack(pady=5)
        print("Toggle button created.")

        self.btn_class_one = tk.Button(frame_buttons, text="Extended", command=lambda: self.save_for_class(1), **button_style)
        self.btn_class_one.pack(pady=5)
        print("Extended button created.")

        self.btn_class_two = tk.Button(frame_buttons, text="Contracted", command=lambda: self.save_for_class(2), **button_style)
        self.btn_class_two.pack(pady=5)
        print("Contracted button created.")

        self.btn_train = tk.Button(frame_buttons, text="Train Model", command=lambda: self.model.train_model(self.counters), **button_style)
        self.btn_train.pack(pady=5)
        print("Train_model button created.")

        self.btn_reset = tk.Button(frame_buttons, text="Reset", command=self.reset, **button_style)
        self.btn_reset.pack(pady=5)
        print("Reset button created.")

        self.counter_label = tk.Label(frame_buttons, text=f"{self.rep_counter}", font=("Arial", 24), bg="white", highlightbackground="black", highlightthickness=3)
        self.counter_label.pack(pady=5)
        print("Counter label created.")

        self.window.update()

    def counting_toggle(self):
        self.counting_enabled = not self.counting_enabled

    def save_for_class(self, class_num):
        ret, frame = self.camera.get_frame()
        if not os.path.exists("1"):
            os.mkdir("1")
        if not os.path.exists("2"):
            os.mkdir("2")

        cv2.imwrite(f"{class_num}/frame{self.counters[class_num-1]}.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
        img = PIL.Image.open(f"{class_num}/frame{self.counters[class_num-1]}.jpg")
        img.thumbnail((150, 150), PIL.Image.ANTIALIAS)
        img.save(f"{class_num}/frame{self.counters[class_num-1]}.jpg")

        self.counters[class_num-1] += 1

    def update(self):
        if hasattr(self, "window") and self.window.winfo_exists():
            if self.counting_enabled:
                self.predict()

            if self.extended and self.contracted:
                self.extended, self.contracted = False, False
                self.rep_counter += 1
            
            # Checking counter_label exists before updating
            if hasattr(self, "counter_label") and self.counter_label.winfo_exists():
                self.counter_label.config(text=f"{self.rep_counter}")
            else:
                print("Warning: counter_label does not exist.")

            ret, frame = self.camera.get_frame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            
            self.window.after(self.delay, self.update)
        else:
            print("Window has been closed. Stopping the update loop.")
    
    def predict(self):
        frame = self.camera.get_frame()
        prediction = self.model.predict(frame)

        if prediction != self.last_prediction:
            if prediction == 1:
                self.extended = True
                self.last_prediction = 1
            if prediction == 2:
                self.contracted = True
                self.last_prediction = 2

    def reset(self):
        self.rep_counter = 0