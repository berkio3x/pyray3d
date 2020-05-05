import math
from collections import namedtuple

class P3Image:
    def __init__(self, width,  height):
        self.width = width
        self.height = height
        self.img = [[None]*width]*height
    
    def pixel(self, x, y, color):
        self.img[x][y] = color

    def __rescale(self, color):
        ''' rescale a color range from 0-1 to 0-225 '''
        return Vec3(round(color.x*255), round(color.y*255) , round(color.z*255))

    def save(self, filename):
        print(self.img)
        with open(filename, 'w') as f:
            f.write(f'P3\n {self.width} {self.height}\n255\n')
            for y in range(self.height):
                for x in range(self.width):
                    if self.img[y][x]:
                        color = self.__rescale(self.img[y][x])
                        f.write(f'{color.x} {color.y} {color.z}  ')
                f.write('\n')






class Vec3:
    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'Vec3({self.x},{self.y},{self.z})'

    def __sub__(self, other):
        return Vec3(self.x - other.x , self.y - other.y , self.z - other.z)

    def __add__(self, other):
        return Vec3(self.x +  other.x , self.y + other.y , self.z + other.z)

    def mag(self):
        return math.sqrt(self.x**2, self.y**2, self.z**2)

    def dot(self, other):
        if isinstance(other, Vec3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise Exception('this should recieve an arfument of type Vec3') 
    
    def cross(self, other):
        if isinstance(other, Vec3):
            return Vec3( self.y* other.z - self.x* other.y, self.z* other.x - self.x* other.z , self.x * self.y - self.y * self.x)
        raise Exception('this should recieve an arfument of type Vec3') 


def trace_ray(O, D, t_min, t_max):
    closest_t = math.inf
    closest_sphere = None

    for sphere in scene['spheres']:
        t1, t2 = ray_sphere_intersect(O, D, sphere)
        
        if  (t_min < t1 < t_max) and t1 < closest_t:
            closest_t  = t1
            closest_sphere = sphere

        if (t_min < t2 < t_max) and t2 < closest_t:
            closest_t = t2

            closest_sphere = sphere

    if closest_sphere == None:
        print(t1, t2 , closest_sphere)
        return Vec3(1,0,0)
    else:
        print(t1, t2, closest_sphere['color'])

        return closest_sphere['color']



def dot(v1, v2):
    return v1.x* v2.x + v1.y * v2.y + v1.z * v2.z

def ray_sphere_intersect(O, D, sphere):
    C = sphere['center']
    r = sphere['radius']
    oc = O - C
    k1 = dot(D,D)
    k2 = 2*dot(oc, D)
    k3 = dot(oc, oc) - r*r

    discriminant = k2*k2 - 4*k1*k3
    
    if discriminant < 0:
        return math.inf, math.inf
    
    t1 = (-k2 + math.sqrt(discriminant))/(2*k1)
    t2 = (-k2 - math.sqrt(discriminant))/(2*k1)
    #print(t1,t2)
    return t1, t2


def canvas_to_viewport(x,y):
    return Vec3(x*Vw/Cw, y*Vh/Ch, d)


def c_to_i(x, y):
    '''canvas to image'''
    
    xnew = xmin + (xmax - xmin)/Cw
    ynew = ymin + (ymax - ymin)/Ch
    return Vec3(xnew, ynew, d)
       


# define scene with one sphere 
scene = {
        'spheres':[
                {
                'center':Vec3(0,0 ,0),
                'radius': 0.5,
                'color':Vec3(1,0,0)
                },
               #                     {
               # 'center':Vec3(2,0 ,4),
               # 'radius': 1,
               # 'color':Vec3(0,1,0)
               # },

               #                     {
               # 'center':Vec3(-2,0 ,4),
               # 'radius': 1,
               # 'color':Vec3(0,0,1)
               # }
            ]
        }

if __name__ == '__main__':
    
    WIDTH  = 320 
    HEIGHT = 200
    camera = Vec3(0, 0, -1)
    
    aspect_ratio = WIDTH/HEIGHT

    xmin = -1 
    xmax = 1  

    ymax = 1/aspect_ratio
    ymin = -1*ymax

    xstep = (xmax - xmin)/(WIDTH-1)
    ystep = (ymax - ymin)/(HEIGHT-1)

    image = P3Image(WIDTH,HEIGHT)

    for j in range(HEIGHT):
        y  = ymin + j*ystep
        for i in range(WIDTH): 
            x  = xmin + i*xstep
            ray = Vec3(x,y,0) - camera
            color = trace_ray(camera, ray, 1, math.inf)
            print(x,y,color)
            image.pixel(int(x),int(y),color)

     
    #for x in range(-Cw//2 , Cw//2):
    #    for y in range(-Ch//2 , Ch//2):
    #        D = canvas_to_viewport(x,y)
    #        #print(D)
    #        color = trace_ray(O, D, 1, math.inf)
    #        #print(x,y, color)
    #        image.pixel(x, y, color)

    image.save('ii.ppm')



