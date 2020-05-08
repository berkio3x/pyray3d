from world import World
from primitive import Sphere
from renderer import Renderer
from vector import Vec3
from ray import Ray
from sandbox import  start_snadbox, set_pixel
from camera import Camera

import multiprocessing

from tkinter import Canvas, PhotoImage, mainloop
import tkinter as tk

import os
import threading


def start_sandbox(queue):

    def rgb2hex(r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def set_pixel():
        pixels = queue.get()
        # print(pixels)
        for pixel in pixels:
            print(f'getting pixel yo {pixel}')
            # cc=rgb2hex(pixel[2].x, pixel[2].y, pixel[2].z)
            # print(pixel[2].x)
            img.put('red', (pixel[0], pixel[1]))
        window.after(1, set_pixel)

    WIDTH, HEIGHT = 640, 480
    window = tk.Tk()
    img = PhotoImage()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#ffffff")
    canvas.pack()
    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")
    window.after(1, set_pixel)
    window.mainloop()

queue = multiprocessing.Queue()

demo_world = World(width=320, height=200)

sphere_1 = Sphere(center=Vec3(0, 0.4, 1), radius=0.5, color = Vec3(1,0,0))

demo_world.add_object(sphere_1)

camera = Camera(Vec3(0, 0, -1))
demo_world.add_camera(camera)


if __name__ == '__main__':
    p = multiprocessing.Process(target=start_sandbox, args=(queue,))
    p.start()
    bucket  = []
    # we are done at this point, Render !! :)
    for pixel in Renderer(demo_world).render(mode='stream'):
        if len(bucket) < 300:
            bucket.append((pixel))
            # print(bucket)
            continue
        else:
            queue.put(bucket)
            bucket = []


        #print(pixel)


    p.join()
