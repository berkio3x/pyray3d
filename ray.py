import math


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


def make_sphere(center, radius, color):
    sphere = {
            'center': center,
            'radius': radius,
            'color' : color
        }
    return sphere




camera = Vec3(0,1,0)
print(camera)

image = P3Image(3,2)

image.pixel(0,0,Vec3(1,0,0))
image.pixel(0,1,Vec3(0,1,0))
image.pixel(0,2,Vec3(0,0,1))
image.pixel(1,0,Vec3(1,1,0))
image.pixel(1,1,Vec3(1,0,1))
image.pixel(1,2,Vec3(0,1,1))
image.save('image.ppm')

