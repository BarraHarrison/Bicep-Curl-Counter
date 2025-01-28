# Graphical User Interface (GUI)
import tkinter as tk 
import os 
import PIL.Image, PIL.ImageTk
import cv2 
import camera

class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Bicep-Curl Counter"