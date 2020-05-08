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
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __div__(self, other):
        return Vec3(self.x/other, self.y/other , self.z/other)

    def __rmul__(self, other):
        return Vec3(self.x*other, self.y*other , self.z*other) 

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

