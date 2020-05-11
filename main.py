#!python3
#cython: language_level=3

import random
from world import World
from renderer import Renderer
from vector import Vec3
from ray import Ray
from sandbox import  make_sphere_object_widget
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
from geometry import Sphere
from geometry import  Plane



def start_sandbox(queue,spheres):

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

    WIDTH, HEIGHT = 850, 480
    window = tk.Tk()



    frame_create_objects = tk.Frame(window)
    frame_render_window = tk.Frame(window, background="bisque")

    # frame_render_window.grid(column=0,columnspan=4)
    # frame_create_objects.grid(column=5, columnspan=2)
    frame_render_window.pack()
    frame_create_objects.pack()

    img = PhotoImage()
    w = tk.Label(frame_render_window, text="Time elasped: ")
    w.pack()


    render_button = tk.Button(frame_create_objects, text="▶️", command=render)
    render_button.pack()

    canvas = Canvas(frame_render_window, width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()

    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")



    # widget = make_sphere_object_widget(frame_create_objects, spheres)
    # widget.pack()

    startt = time.time()
    window.after(1, set_pixel)
    window.mainloop()

queue = multiprocessing.Queue()

demo_world = World(width=320, height=200)

sphere_1 = Sphere(center=Vec3(-1, -0.7, 5), radius=0.7, color = Vec3(1,0,0), reflective=0.6)
sphere_2 = Sphere(center=Vec3(2, -0.2, 5), radius=1, color = Vec3(1,1,0), reflective=0.5)
sphere_3 = Sphere(center=Vec3(0, 5001, 3), radius=5000, color = Vec3(1,1,1))

light_1 = PointLight(type='point', position=Vec3(0,-3,3), intensity=0.4)
light_2 = AmbientLight(type='ambient', position=Vec3(0,-3,0.5), intensity=0.3)
light_3 = DirectionalLight(type='directional', direction=Vec3(0,-3,0.5), intensity=0.3)


plane_1 = Plane(y=1, color=Vec3(0.7,0.6,0.8))

demo_world.add_object(sphere_1)
demo_world.add_object(sphere_2)
# demo_world.add_object(sphere_3)
demo_world.add_plane(plane_1)

## generate 5 random sphers
for i in range(10):
    s = Sphere(center=Vec3(
        random.uniform(-4.0,4.0),
        0.2,
        random.uniform(1.0, 6.0),
    ),
        radius=random.uniform(0.2,0.4),
        color=Vec3(
            random.uniform(0.0,1.0),
            random.uniform(0.0,1.0),
            random.uniform(0.0,1.0),
        ),
    reflective=random.uniform(0.0,0.0))
    demo_world.add_object(s)

demo_world.add_light(light_1)
demo_world.add_light(light_2)

demo_world.add_light(light_3)

camera = Camera(Vec3(0, 0, 0))
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
    p = multiprocessing.Process(target=start_sandbox, args=(queue,demo_world.objects))
    p.start()
    render()
    p.join()

    # render_to_image()