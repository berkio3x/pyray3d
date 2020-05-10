from tkinter import Canvas, PhotoImage, mainloop
import tkinter as tk
import matplotlib
from tkinter import  ttk
def make_sphere_object_widget(root, spheres):
	# icon = tk.PhotoImage('./icons/sphere.png')
	frame = tk.Frame(root,)

	for index, sphere in enumerate(spheres):
		button = tk.Button(frame,text='⦾',bg=matplotlib.colors.to_hex([
			sphere.color.x,
			sphere.color.y,
			sphere.color.z,
			]
		))

		# Coordinates
		coordinat_x = tk.Entry(frame, width=4, foreground='white', background='#483D41')
		coordinat_x.insert(0,sphere.center.x)
		coordinat_y = tk.Entry(frame,width=4, foreground='white',  background='#483D41')
		coordinat_y.insert(0,sphere.center.y)

		coordinat_z = tk.Entry(frame,width=4, foreground='white',  background='#483D41')
		coordinat_z.insert(0,sphere.center.z)

		button.grid(row=index,column=0)
		coordinat_x.grid(row=index,column=1)
		coordinat_y.grid(row=index,column=2)
		coordinat_z.grid(row=index,column=3)



		# Color


		# Coordinates
		color_x = tk.Entry(frame, width=3,foreground='white',background='#797979')
		color_x.insert(0,sphere.color.x)
		color_y = tk.Entry(frame,width=3,foreground='white',background='#797979')
		color_y.insert(0,sphere.color.y)

		color_z = tk.Entry(frame,width=3,foreground='white',background='#797979')
		color_z.insert(0,sphere.color.z)

		color_x.grid(row=index,column=4)
		color_y.grid(row=index,column=5)
		color_z.grid(row=index,column=6)

	return frame
