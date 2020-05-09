
class Light:
    def __init__(self, type, intensity):
        self.type = type
        self.intensity = intensity



    def __calculate_specular(self,s):
        pass


    def dot(self, v1, v2):
        return v1.x* v2.x + v1.y * v2.y + v1.z * v2.z

class PointLight(Light):
    '''
    A point light as suggest, is a point in space which emits lights from its position Lp,
    The light emitted is equal in all directions.
    ex an approximation of a  bulb can be considered as a point light.

    '''
    
    def __init__(self, position , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position




    #
class AmbientLight(Light):
    
    def __init__(self , position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position


class DirectionalLight(Light):
    def __init__(self , direction, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction=direction



        
