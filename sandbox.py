from tkinter import Canvas, PhotoImage, mainloop
import tkinter as tk
from math import sin
from multiprocessing import  process

# from PIL import Image
# im = Image.open("render.ppm")
# im.show()

def start_snadbox(img):
	WIDTH, HEIGHT = 640, 480

	window = tk.Tk()
	canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#ffffff")
	canvas.pack()
	canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")

	mainloop()

def set_pixel(x,y,color):
	img = PhotoImage()
	img.put('red', (x, y))
	return img
