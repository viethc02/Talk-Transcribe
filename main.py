import time
import tkinter
import pygame
import keyboard

import TTNM.speechToText
from GUI1 import *
from GUI2 import *
from tkVideoPlayer import TkinterVideo
from playsound import playsound

root = tkinter.Tk()
root.title("Talk Transcribe")

def playSound():
    sound = 'question.mp3'
    pygame.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)
    time.sleep(0)

def playVideo():
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.place(x=200, y=100)
    videoplayer.load(r"Video/seeme.mp4")
    videoplayer.set_resampling_method(1)
    videoplayer.play()

def replay():
    playSound()
    playVideo()

if __name__ == '__main__':
    # root = tkinter.Tk()
    # root.title("Talk Transcribe")

    canvas = Canvas(root, width=640, height=360)
    canvas.pack(fill="both", expand=True)

    playSound()
    playVideo()

    text = Text(root, wrap=WORD, height=1, width=22, font="ARIAL", bg="#000000", fg="white")
    text.place(x=150, y=250)
    text.insert(INSERT, "Bạn có nhìn thấy tôi không?")

    playIcon = PhotoImage(file="Icon/play.png")
    Button(root, image=playIcon, command=lambda : replay()).place(x=100, y=100)

    catIcon = PhotoImage(file="Icon/cat.png")
    #catButton = tkinter.Button(root, image=catIcon, command=lambda : TTNM.speechToText.magic()).invoke()
    #tkinter.Button(catButton).invoke()
    Button(root, image=catIcon).place(x=30, y=225)

    keyboard.add_hotkey("Z", lambda : TTNM.speechToText.magic())

    upIcon = PhotoImage(file="Icon/volume_up.png")
    Button(root, image=upIcon).place(x=400, y=75)

    downIcon = PhotoImage(file="Icon/volume_down.png")
    Button(root, image=downIcon).place(x=400, y=150)

    img = PhotoImage(file="Icon/cute.png")
    canvas.create_image(0, 0, image=img, anchor="nw")

    yesIcon = PhotoImage(file="Icon/yes.png")
    Button(root, image=yesIcon, command=lambda: cam()).pack(padx=15, pady=10, side=tk.LEFT)

    noIcon = PhotoImage(file="Icon/no.png")
    Button(root, image=noIcon, command=lambda : open(root)).pack(padx=15, pady=10, side=tk.RIGHT)

    root.eval('tk::PlaceWindow . center')
    root.mainloop()

    #App(root)