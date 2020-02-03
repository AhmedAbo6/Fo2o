from tkinter import *

root = Tk()
root.title("Focus")


frame1 = LabelFrame(root,text="GUI", padx=20, pady=20)
frame1.pack(padx=30, pady=30)

var = IntVar()

c1 = Checkbutton(frame1,text="ToDo GUI", variable=var).pack()
c2 = Checkbutton(frame1,text="Pray Follow Up", variable=var).pack()
c3 = Checkbutton(frame1,text="Food Follow UP", variable=var).pack()
c4 = Checkbutton(frame1,text="What i am doing Follow Up", variable=var).pack()
c5 = Checkbutton(frame1,text="weather follow Up", variable=var).pack()
c6 = Checkbutton(frame1,text="Time Waste Follow Up", variable=var).pack()
c7 = Checkbutton(frame1,text="Mood Follow Up", variable=var).pack()
c8 = Checkbutton(frame1,text="Renaming files to nums and count them", variable=var).pack()
c9 = Checkbutton(frame1,text="Card Game", variable=var).pack()
c10 = Checkbutton(frame1,text="Voice Assistant", variable=var).pack()
c11 = Checkbutton(frame1,text="Recommend Books-Animes-Movies-... by websites", variable=var).pack()
c12 = Checkbutton(frame1,text="World & Egypt Trends", variable=var).pack()
c13 = Checkbutton(frame1,text="All iz Well", variable=var).pack()
c14 = Checkbutton(frame1,text="Download All", variable=var).pack()
c15 = Checkbutton(frame1,text="MP3 player with a good visualization", variable=var).pack()
c16 = Checkbutton(frame1,text="Password Keeper", variable=var).pack()


root.mainloop()
