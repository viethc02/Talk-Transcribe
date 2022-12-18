import tkinter as tk

from tkinter import *
from tkinter.ttk import *
from Translator import *

import pygame
import time

class App(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.initUI()

        #self.video_source = video_source
        #self.vid = ShowVideo(video_source)

        #self.canvas = Canvas(window, width=640, height=360)
        self.canvas.pack(fill="both", expand=True)

    def initUI(self):
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill="both", expand=True)

        # yesIcon = PhotoImage(file="Icon/yes.png")
        # Button(self, image=yesIcon, command=lambda : cam()).pack(padx=15, pady=10, side=tk.LEFT)
        # #Button(self, image=yesIcon).place(x=15, y=300)
        #
        # #playsound('question.mp3')
        # noIcon = PhotoImage(file="Icon/no.png")
        # Button(self, image=noIcon).pack(padx=15, pady=10, side=tk.RIGHT)

        def clear_data():
            text.delete(1.0, END)

        def speak_data():
            text2speech = text.get(1.0, END)
            texttospeech(text2speech)

        text = Text(self, font=('Times', 5), bg="light yellow", fg="purple", height=5, width=50)
        text.place(x=150, y=250)
        # text2speech = text.get(1.0, END)

        icon1 = PhotoImage(file='Icon/erase.png')
        Button(self, image=icon1, command=clear_data).pack(padx=15, pady=10, side=tk.LEFT)

        icon = PhotoImage(file='Icon/voice.png')
        Button(self, image=icon, command=speak_data).pack(padx=15, pady=10, side=tk.RIGHT)

        self.eval('tk::PlaceWindow . center')
        self.mainloop()

        #upIcon = PhotoImage(file="Icon/volume_up.png")
        #Button(self, image=upIcon).pack(padx=15, pady=50, side=tk.LEFT)

        #downIcon = PhotoImage(file="Icon/volume_down.png")
        #Button(self, image=downIcon).pack(padx=5, pady=5, side=tk.RIGHT)

        self.window.eval('tk::PlaceWindow . center')
        #self.window.mainloop()
# def playSound():
#     sound = 'question.mp3'
#     pygame.init()
#     pygame.mixer.music.load(sound)
#     pygame.mixer.music.play(loops=0)
#     time.sleep(0)

