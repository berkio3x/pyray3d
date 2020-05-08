
class World:
    def __init__(self, width, height, lights=None, objects=None, camera=None):

        self.width = width
        self.height = height

        if camera:
            self.camera = camera
        else:
            self.camera = []
        
        if lights:
            self.lights = lights
        else:
            self.lights = []

        if objects:
            self.objects = objects
        else:
            self.objects = []

    def add_camera(self, position):
        self.camera = position


    def add_object(self, object):
        self.objects.append(object)

    def add_light(self, light):
        self.lights.append(light)
