from world import World
from primitive import Sphere
from renderer import Renderer
from vector import Vec3
from ray import Ray
from sandbox import  start_snadbox, set_pixel
from camera import Camera
import matplotlib
import multiprocessing

from tkinter import Canvas, PhotoImage, mainloop
import tkinter as tk
from light import  PointLight, AmbientLight, DirectionalLight
import os
import threading
import time
from tkinter.ttk import  Style





def start_sandbox(queue):

    def rgb2hex(r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def set_pixel():
        pixels = queue.get()
        if pixels == 'DONE':
            endt = time.time()
            elapsed = endt - startt
            w.config(text=f'{elapsed} sec.')
        else:
            # print(pixels)
            for pixel in pixels:
                # print(f'getting pixel yo {pixel}')
                # cc=rgb2hex(pixel[2].x, pixel[2].y, pixel[2].z)
                # print(pixel[2].x)
                color =  matplotlib.colors.to_hex([
                    pixel[2].x,
                    pixel[2].y,
                    pixel[2].z
                ])

                img.put(color, (pixel[0], pixel[1]))
            window.after(1, set_pixel)

    WIDTH, HEIGHT = 640, 480
    window = tk.Tk()
    img = PhotoImage()
    w = tk.Label(window, text="Time elasped: ")
    w.pack()
    window.style = Style()
    window.style.theme_use("classic")

    # render_button = tk.Button(window, text="▶️", command=render)
    # render_button.pack()

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#ffffff")
    canvas.pack()
    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")
    startt = time.time()
    window.after(1, set_pixel)
    window.mainloop()

queue = multiprocessing.Queue()

demo_world = World(width=320, height=200)

sphere_1 = Sphere(center=Vec3(0, -0.2, -2), radius=0.3, color = Vec3(1,0,0))
sphere_2 = Sphere(center=Vec3(0.3, 0.2, -2), radius=0.2, color = Vec3(1,1,0))

light_1 = PointLight(type='point', position=Vec3(0,-0.5,1.9), intensity=0.8)
# light_2 = AmbientLight(type='point', position=Vec3(-1,1,0), intensity=0.6)

demo_world.add_object(sphere_1)
demo_world.add_object(sphere_2)
demo_world.add_light(light_1)
# demo_world.add_light(light_2)


camera = Camera(Vec3(0, 0, -1))
demo_world.add_camera(camera)


def render():

    # we are done at this point, Render !! :)
    _render = Renderer(demo_world).render(mode='stream')


    bucket = []
    for pixel in _render:
        bucket.append(pixel)
        if len(bucket) == 1000:
            queue.put(bucket)
            bucket = []

    queue.put('DONE')

def render_to_image():
    Renderer(demo_world).render(mode='stream')


if __name__ == '__main__':
    p = multiprocessing.Process(target=start_sandbox, args=(queue,))
    p.start()
    render()
    p.join()

    # render_to_image()