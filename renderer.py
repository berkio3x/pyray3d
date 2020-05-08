from ray import Ray
from image import P3Image
from vector import Vec3
import math

class Renderer:

    def __init__(self, world):
        self.world = world
        self.IMAGE_WIDTH = world.width
        self.IMAGE_HEIGHT = world.height
        self.image = P3Image(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

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
            P = Vec3(closest_t*camera.x , closest_t*camera.y, closest_t*camera.z)
            N = P - closest_sphere.center
            N = N / N.mag()
            return closest_sphere.color


    def render(self):
        print(self)
        camera = self.world.camera
        '''calculate the aspect ratio to avoid squashing of objects bewteen world coordinates & image coordinates'''
        aspect_ratio = self.IMAGE_WIDTH/self.IMAGE_HEIGHT

        '''Our world coordinates x axis will span from -1 to 1'''
        xmin = -1
        xmax = 1

        ''' use the aspect ratio to correcly find the Y coordinate range in our world coordinate system'''
        ymax = 1/aspect_ratio
        ymin = -1*ymax

        xstep = (xmax - xmin) / (self.IMAGE_WIDTH-1)
        ystep = (ymax - ymin) / (self.IMAGE_HEIGHT-1)

        '''do the actual rendering'''
        for j in range(self.IMAGE_HEIGHT):
                y  = ymin + j*ystep
                
                for i in range(self.IMAGE_WIDTH): 
                    x  = xmin + i*xstep
                    
                    ray = Ray(origin=camera ,direction=Vec3(x,y,0) - camera.origin)
                    color = self.trace_ray(camera.origin, ray, -1, math.inf)
                    
                    self.image.set_pixel(i, j, color)
                    print(i, j, color)
                    #print(f'rendering block [{i}] [{j}] - [{"{:3.0f}%".format(float(j) / float(self.IMAGE_HEIGHT) * 100)}] ', end='\r')
        self.image.save('newrender.ppm')
