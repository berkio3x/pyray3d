import math
from collections import namedtuple


class P3Image:
    def __init__(self, width,  height):
        self.width = width
        self.height = height

        self.img = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.img[y][x] = color


    def __rescale(self, color):
        ''' rescale a color range from 0-1 to 0-225 '''
        return Vec3(round(color.x*255), round(color.y*255) , round(color.z*255))


    def save(self, filename):
        with open(filename, 'w') as f:

            f.write(f'P3 {self.width} {self.height}\n255\n')
            for row in self.img:
                for color in row:
                    c = self.__rescale(color)
                    f.write(f'{c.x} {c.y} {c.z}  ')

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
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __div__(self, other):
        return Vec3(self.x/other, self.y/other , self.z/other)

    def __mul__(self, other):
        return Vec3(self.x*other, self.y*other , self.z*other)     

    def __truediv__(self, other):
        return Vec3(self.x/other, self.y/other , self.z/other)

    def dot(self, other):
        if isinstance(other, Vec3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise Exception('this should recieve an arfument of type Vec3') 
    
    def cross(self, other):
        if isinstance(other, Vec3):
            return Vec3( self.y* other.z - self.x* other.y, self.z* other.x - self.x* other.z , self.x * self.y - self.y * self.x)
        raise Exception('this should recieve an arfument of type Vec3') 




def compute_light(P, N):
    i = 0.0
    for light in scene['lights']:
        if light['type'] == 'ambient':
            i += light['intensity']
        else:
            if light['type'] == 'point':
                L = light['position'] - P
            if light['type'] == 'directional':
                L = light['direction']

            n_dot_l = dot(N,L)
            if n_dot_l > 0:
                i += light['intensity']*n_dot_l/(N.mag()*L.mag())
    return i


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
        return Vec3(173/255, 216/255, 230/255)
    else:
        P = Vec3(closest_t*D.x , closest_t*D.y, closest_t*D.z)
        N = P - closest_sphere['center']
        N = N / N.mag()
        return closest_sphere['color']*compute_light(P, N)



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
            # {'center':Vec3(0, 0 ,0),'radius': 0.3,'color':Vec3(1,0,0)},
            # {'center':Vec3(0, 1 ,2),'radius': 0.5,'color':Vec3(0.3,1,1.0)},
            # {'center':Vec3(-0.9, 1 ,2),'radius': 0.2,'color':Vec3(0.3,0.3,1.0)},


            {'center':Vec3(-1.2 ,0    ,0.9),'radius': 0.6,'color':Vec3(0.7,0.2,0.7)},
            {'center':Vec3(1.2  ,0    ,0.9),'radius': 0.6,'color':Vec3(0.3,1,1.0)},
            {'center':Vec3(0    ,0.5  ,0.9),'radius': 0.6,'color':Vec3(0.3,0.3,1.0)},
            {'center':Vec3(0    ,5001 ,0.9),'radius': 5000,'color':Vec3(0.1,0.8,0.1)},

            ],

        'lights':[
            {'type':'ambient','intensity':0.3,'position':Vec3(0,-0.6,0)},
            {'type':'point','intensity':0.4,'position':Vec3(0,0.3,1.8)},
            {'type':'directional','intensity':0.2,'direction':Vec3(1,4,4)}
        ]
    }


if __name__ == '__main__':
    
    WIDTH  =  800
    HEIGHT = 620
    camera = Vec3(0, 0, -1)

    aspect_ratio = WIDTH/HEIGHT

    xmin = -1 
    xmax = 1  

    ymax = 1/aspect_ratio
    ymin = -1*ymax

    xstep = (xmax - xmin) / (WIDTH-1)
    ystep = (ymax - ymin) / (HEIGHT-1)

    image = P3Image(WIDTH, HEIGHT)

    for j in range(HEIGHT):
        y  = ymin + j*ystep
        for i in range(WIDTH): 
            x  = xmin + i*xstep
            ray = Vec3(x,y,0) - camera
            color = trace_ray(camera, ray, -1, math.inf)
            
            image.set_pixel(i, j, color)

            print(f'rendering block [{i}] [{j}] ', end='\r')
    image.save('render.ppm')



