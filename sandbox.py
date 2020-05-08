from tkinter import Canvas, PhotoImage, mainloop
import tkinter as tk
from math import sin

WIDTH, HEIGHT = 640, 480

window = tk.Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#ffffff")
canvas.pack()
img = PhotoImage('render.ppm')
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")


# from PIL import Image
# im = Image.open("render.ppm")
# im.show()


for y in range(300):
    for x in range(200):
	    # y = int(HEIGHT/2 + HEIGHT/4 * sin(x/80.0))
	    img.put('red', (x,y))


mainloop()
