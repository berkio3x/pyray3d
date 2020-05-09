#!python3
#cython: language_level=3


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

    WIDTH, HEIGHT = 850, 480
    window = tk.Tk()



    frame_create_objects = tk.Frame(window,background="red")
    frame_render_window = tk.Frame(window, background="bisque")

    frame_render_window.grid(column=0,columnspan=4)
    frame_create_objects.grid(column=5, columnspan=2)

    img = PhotoImage()
    w = tk.Label(frame_render_window, text="Time elasped: ")
    w.pack()


    render_button = tk.Button(frame_create_objects, text="▶️", command=render)
    render_button.pack()

    canvas = Canvas(frame_render_window, width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()

    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")
    startt = time.time()
    window.after(1, set_pixel)
    window.mainloop()

queue = multiprocessing.Queue()

demo_world = World(width=320, height=200)

sphere_1 = Sphere(center=Vec3(0, -0.5, 5), radius=1.7, color = Vec3(1,0,0))
sphere_2 = Sphere(center=Vec3(2, -0.5, 5), radius=1.7, color = Vec3(1,1,0))
sphere_3 = Sphere(center=Vec3(0, 5001, 3), radius=5000, color = Vec3(1,0,1))

light_1 = PointLight(type='point', position=Vec3(0,0,0), intensity=0.4)
light_2 = AmbientLight(type='ambient', position=Vec3(0,-0.6,0.5), intensity=0.3)
# light_2 = DirectionalLight(type='directional', direction=Vec3(0,-0.6,0.5), intensity=0.3)

demo_world.add_object(sphere_1)
demo_world.add_object(sphere_2)
demo_world.add_object(sphere_3)



demo_world.add_light(light_1)
demo_world.add_light(light_2)


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
    p = multiprocessing.Process(target=start_sandbox, args=(queue,))
    p.start()
    render()
    p.join()

    # render_to_image()