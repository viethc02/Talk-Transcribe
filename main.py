import tkinter

from GUI1 import *

from tkVideoPlayer import TkinterVideo

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Talk Transcribe")

    canvas = Canvas(root, width=640, height=360)
    canvas.pack(fill="both", expand=True)

    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.place(x=200, y=100)
    videoplayer.load(r"Video/seeme.mp4")
    videoplayer.set_resampling_method(1)
    videoplayer.play()

    playIcon = PhotoImage(file="Icon/play.png")
    #Button(root, image=playIcon, command=lambda: videoplayer.play()).place(x=100, y=100)

    text = Text(root, wrap=WORD, height=1, width=22, font="ARIAL", bg="#000000", fg="white")
    text.place(x=150, y=250)
    text.insert(INSERT, "Bạn có nhìn thấy tôi không?")

    catIcon = PhotoImage(file="Icon/cat.png")
    Button(root, image=catIcon, command=lambda: videoplayer.play()).place(x=30, y=225)

    upIcon = PhotoImage(file="Icon/volume_up.png")
    Button(root, image=upIcon).place(x=400, y=75)

    downIcon = PhotoImage(file="Icon/volume_down.png")
    Button(root, image=downIcon).place(x=400, y=150)

    img = PhotoImage(file="Icon/cute.png")
    canvas.create_image(0, 0, image=img, anchor="nw")

    App(root)
