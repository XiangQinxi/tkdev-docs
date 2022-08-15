from tkdev import DevWindow, window_move
from tkinter import Frame

Root = DevWindow()
TitleBar = Frame(Root, background="#000000")
TitleBar.pack(fill="x", ipady=30)
window_move(TitleBar, Root)
Root.mainloop()