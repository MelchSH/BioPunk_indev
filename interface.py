import tkinter as tk


class Diagram_App:
    def __init__(self,root):
        self.root = root
        self.root.title("TEST INDEV")

        self.canvas = tk.Canvas(root,width=1200,height=700,bg="white")
        self.canvas.pack()