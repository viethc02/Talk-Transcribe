import tkinter
from tkinter import *
import texttospeech
from Translator import *

def open(root):
    windown = Toplevel(root)
    canvas = Canvas(windown, width=640, height=360)
    canvas.pack(fill="both", expand=True)

    img = PhotoImage(file="Icon/cute.png")
    canvas.create_image(0, 0, image=img, anchor="nw")

    def clear_data():
        text.delete(1.0,END)

    def speak_data():
        text2speech = text.get(1.0, END)
        texttospeech(text2speech, "vi")

    text = Text(windown,font=('Times', 13),bg = "light yellow", fg= "purple", height = 10, width =50)
    text.place(x=100, y=50)
    #text2speech = text.get(1.0, END)

    icon1 = PhotoImage(file='Icon/erase.png')
    Button(windown, image=icon1, command=clear_data).pack(padx=15, pady=10, side=tkinter.LEFT)
    #Button(windown, image=icon1, command=clear_data).place(x=30, y=300)

    icon = PhotoImage(file='Icon/voice.png')
    Button(windown, image=icon, command=speak_data).pack(padx=100, pady=10, side=tkinter.LEFT)
    #Button(windown, image=icon, command=lambda : speak_data()).place(x=400, y=300)

    sign = PhotoImage(file='Icon/sign_language.png')
    Button(windown, image=sign, command=lambda : cam()).pack(padx=15, pady=10, side=tkinter.RIGHT)
    #Button(windown, image=sign, command=lambda: cam()).place(x=250, y=300)

    #windown.eval('tk::PlaceWindow . center')
    windown.mainloop()

