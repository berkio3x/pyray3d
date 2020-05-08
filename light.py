
class Light:
    def __init__(self, type, intensity):
        self.light_type = light
        self.position = position


class PointLight(Light):
    
    def __init__(self, position , position):
        super().__init__(*args, **kwargs):
        self.position = position


    def __calculate_specular(self,s):
        pass


    def calculate_intensity(self, intensity):
        L = light['position'] - P
         n_dot_l = dot(N,L)
            if n_dot_l > 0:
                i += light['intensity']*n_dot_l/(N.mag()*L.mag())



class AmbientLight(Light):
    
    def __init__(self, position , position):
        super().__init__(*args, **kwargs):
        self.position = position

    def calculate_intensity(self, intensity):
        return intensity + self.intensity



class DirectionalLight(Light):
    def __init__(self, position , direction):
        super().__init__(*args, **kwargs):
        
        if not isinstance(direction, Vec3):
            raise TypeError('A Dircetion should be of type Vec3')

        self.direction = direction
