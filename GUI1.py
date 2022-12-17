import tkinter as tk

from tkinter import *
from tkinter.ttk import *
from Translator import *

class App(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.initUI()

        #self.video_source = video_source
        #self.vid = ShowVideo(video_source)

        #self.canvas = Canvas(window, width=640, height=360)
        #self.canvas.pack(fill="both", expand=True)

    def initUI(self):
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill="both", expand=True)

        yesIcon = PhotoImage(file="Icon/yes.png")
        Button(self, image=yesIcon).pack(padx=15, pady=10, side=tk.LEFT)
        #Button(self, image=yesIcon).place(x=15, y=300)

        noIcon = PhotoImage(file="Icon/no.png")
        Button(self, image=noIcon, command=lambda : cam()).pack(padx=15, pady=10, side=tk.RIGHT)

        #upIcon = PhotoImage(file="Icon/volume_up.png")
        #Button(self, image=upIcon).pack(padx=15, pady=50, side=tk.LEFT)

        #downIcon = PhotoImage(file="Icon/volume_down.png")
        #Button(self, image=downIcon).pack(padx=5, pady=5, side=tk.RIGHT)

        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()