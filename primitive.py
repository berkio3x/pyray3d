import math

class Sphere:
    
    def __init__(self, center, radius, color, reflective=0.0):
        self.center = center
        self.radius = radius
        self.color = color
        self.reflective = reflective
   

    def dot(self, v1, v2):
        return v1.x* v2.x + v1.y * v2.y + v1.z * v2.z
   
    def intersect_at_point(self, camera, ray):
        
        ''' The reason to keep bot names of form center & C and radius & R is ,
            its easy to reason about code by names like center while its easy to 
            use  names like C & R in mathmetical equations
        '''
        C = self.center
        r = self.radius
        O = camera
        D = ray
        oc = O - C
        k1 = self.dot(D,D)
        k2 = 2*self.dot(oc, D)
        k3 = self.dot(oc, oc) - r*r

        discriminant = k2*k2 - 4*k1*k3
        
        if discriminant < 0:
            return math.inf, math.inf
        
        t1 = (-k2 + math.sqrt(discriminant))/(2*k1)
        t2 = (-k2 - math.sqrt(discriminant))/(2*k1)
        return t1, t2



