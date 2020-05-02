import math

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
