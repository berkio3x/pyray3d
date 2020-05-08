from vector import  Vec3
class P3Image:
    def __init__(self, width,  height):
        self.width = width
        self.height = height

        self.img = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.img[y][x] = color


    def __rescale(self, color):
        ''' rescale a color range from 0-1 to 0-225 '''
        return Vec3(round(color.x*255), round(color.y*255) , round(color.z*255))


    def save(self, filename):
        with open(filename, 'w') as f:

            f.write(f'P3 {self.width} {self.height}\n255\n')
            for row in self.img:
                for color in row:
                    c = self.__rescale(color)
                    f.write(f'{c.x} {c.y} {c.z}  ')

                f.write('\n')