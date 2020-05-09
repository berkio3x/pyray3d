
class Light:
    def __init__(self, type, intensity):
        self.type = type
        self.intensity = intensity


class PointLight(Light):
    
    def __init__(self, position , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position


    def __calculate_specular(self,s):
        pass
    #


class AmbientLight(Light):
    
    def __init__(self , position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position


class DirectionalLight(Light):
    def __init__(self , direction, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction=direction
        
