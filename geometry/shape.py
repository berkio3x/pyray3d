import math
from vector import Vec3

class Shape:

    def intersect_at_point(self, point, normal):
        raise NotImplementedError


class Plane(Shape):
    def __init__(self, color, y=0, specular=-1, reflective=0):
        self.specular = specular
        self.reflective = reflective
        self.center = Vec3(0,y,0)
        self.normal = Vec3(0,-1,0)
        self.color = color

    def intersect_at_point(self, origin, ray):
        '''
            We define an infinite plane in x-z plane, these 3 thigs can happen:
            1. A ray is is parallel to the plane so there will be no intersection
            2. A ray is orthogonal to the x-z plane so there will be infinetly many intersections,
            & since the width of plane is infinetly small, we can ignore this safely .
            3. Origin lies above the plane & is neithe parallel.
            4. Origin lies below the plane & is not parallel.

            The normal to the plane is always constant as its same for all points on the plane.
            Finding if the ray intersects with the plane is pretty simple,
            jus check the Y component of vector with the Y of Plane.
        '''


        denom = ray.dot(self.normal)

        if abs(denom) > 0.0001:
            diff  = self.center - ray
            t = diff.dot(self.normal) / denom

            if t > 0.0001:
                return t
        return math.inf


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

