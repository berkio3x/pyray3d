import math

class Shape:

    def intersect_at_point(self, point, normal):
        raise NotImplementedError


class Sphere(Shape):

    def __init__(self, center, color, radius, specular=-1, reflective=0.0):
        self.center = center
        self.color = color
        self.specular = specular
        self.reflective = reflective
        self.radius = radius


    def intersect_at_point(self, origin, ray):
        '''
            Given the origin point of ray & the direction vector,
            find the point at which the ray intersects with the sphere

        '''

        C = self.center
        r = self.radius
        O = origin
        D = ray
        oc = O - C
        k1 = D.dot(D)
        k2 = 2 * oc.dot(D)
        k3 = oc.dot(oc) - r * r
        discriminant = k2 * k2 - 4 * k1 * k3

        if discriminant < 0:
            return math.inf, math.inf

        t1 = (-k2 + math.sqrt(discriminant)) / (2 * k1)
        t2 = (-k2 - math.sqrt(discriminant)) / (2 * k1)
        return t1, t2

