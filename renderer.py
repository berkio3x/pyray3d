from ray import Ray
from image import P3Image
from vector import Vec3
import math
import multiprocessing

class Renderer:

    def __init__(self, world):
        self.world = world
        self.IMAGE_WIDTH = world.width
        self.IMAGE_HEIGHT = world.height
        self.image = P3Image(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

    def dot(self, v1, v2):
        return v1.x* v2.x + v1.y * v2.y + v1.z * v2.z

    def compute_light(self, Point, Normal):
        i = 0.0
        P = Point
        N = Normal

        for light in self.world.lights:
            if light.type == 'ambient':
                i += light.intensity
            else:
                if light.type == 'point':
                    L = light.position - P
                    print(f'L is {L}')
                if light.type == 'directional':
                    L = light.direction

                n_dot_l = self.dot(N, L)

                if n_dot_l > 0:
                    print(f'light intensity {light.intensity}')
                    i += light.intensity * n_dot_l / (N.mag() * L.mag())

                # # specularity calculation
                # if s != -1:
                #     R = 2 * N * self.dot(N, L) - L
                #     r_dot_v = self.dot(R, V)
                #     if r_dot_v > 0:
                #         i += light.inte* ((r_dot_v / (R.mag() * V.mag())))
                #         pass

        return i

    def trace_ray(self, camera, ray, t_min, t_max):
        ''' Trace the actual ray & return the color of the object if there is some intersection with a geometry.
            Since a ray is represented by the parametric equation:
            P = O +t*D ,
            where Point P on ray / half line is defined by the parameter t and the Direction D,
            we assume the tmax is infinity in our case, why? because we want the ray to go infinitely in its direction.
        '''

        closest_t = math.inf
        closest_sphere = None
        # find the intersection with spheres in our world
        for sphere in self.world.objects:
            t1, t2 = sphere.intersect_at_point(camera, ray)

            if  (t_min < t1 < t_max) and t1 < closest_t:
                closest_t  = t1
                closest_sphere = sphere

            if (t_min < t2 < t_max) and t2 < closest_t:
                closest_t = t2

                closest_sphere = sphere

        if closest_sphere == None:
            return Vec3(173/255, 216/255, 230/255)
        else:
            P = Vec3(closest_t*ray.direction.x , closest_t*ray.direction.y, closest_t*ray.direction.z)
            N = P - closest_sphere.center
            N = N / N.mag()
            light = self.compute_light(P, N)
            print(light)
            return closest_sphere.color*light



    def render(self, mode=None):
        camera = self.world.camera
        '''calculate the aspect ratio to avoid squashing of objects bewteen world coordinates & image coordinates'''
        aspect_ratio = self.IMAGE_WIDTH / self.IMAGE_HEIGHT

        '''Our world coordinates x axis will span from -1 to 1'''
        xmin = -1
        xmax = 1

        ''' use the aspect ratio to correcly find the Y coordinate range in our world coordinate system'''
        # ymax = 1 / aspect_ratio
        # ymin = -1 * ymax


        ymax =  1 / aspect_ratio
        ymin = -1*ymax

        xstep = (xmax - xmin) / (self.IMAGE_WIDTH - 1)
        ystep = (ymax - ymin) / (self.IMAGE_HEIGHT - 1)

        '''do the actual rendering'''
        for j in range(self.IMAGE_HEIGHT):
                y  = ymin + j*ystep

                for i in range(self.IMAGE_WIDTH):
                    x  = xmin + i*xstep

                    ray = Ray(origin=camera , direction=Vec3(x,y,0) - camera.origin)
                    color = self.trace_ray(camera.origin, ray, -1, math.inf)

                    self.image.set_pixel(i, j, color)
                    if mode=='stream':
                        yield (i, j, color)
        if mode != 'stream':
            print('seving')
            self.image.save('rendExxr.ppm')

