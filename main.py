from world import World
from primitive import Sphere
from renderer import Renderer
from vector import Vec3
from ray import Ray

from camera import Camera


demo_world = World(width=320, height=200) 

sphere_1 = Sphere(center=Vec3(0, 0, 2), radius=0.5, color = Vec3(0,1,1,))

demo_world.add_object(sphere_1)

camera = Camera(Vec3(0, 0, -1))
demo_world.add_camera(camera)

# we are done at this point, Render !! :)
Renderer(demo_world).render()
