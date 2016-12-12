# >>> p = point.from_frac(0.3, 0.7)
# >>> p.frac()
# (0.3, 0.7)
# >>> p.pixel(500, 500)
# (150, 350)
# >>> p.pixel(1000, 800)
# (300, 560)
# >>> p2 = point.from_pixel(200, 200, 500, 800)
# >>> p2.frac()
# (0.4, 0.25)
# >>> p2.pixel(1000, 1000)
# (400, 250)
# >>> p2.pixel(500, 800)
# (200, 200)

import math

class Point:
    def __init__(self, frac_x: float, frac_y: float):
        self._frac_x = frac_x
        self._frac_y = frac_y
    
    def frac(self) -> (float, float):
        return (self._frac_x, self._frac_y)

    def pixel(self, size_x: float, size_y: float) -> (float, float):
        return (self._frac_x * size_x, self._frac_y * size_y)

    def distance_from(self, p: 'Point') -> float:
        px, py = p.frac()

        return math.sqrt(
            (self._frac_x-px)*(self._frac_x-px) + (self._frac_y-py)*(self._frac_y-py))



def from_frac(frac_x: float, frac_y: float) -> Point:
    return Point(frac_x, frac_y)

def from_pixel(pixel_x: float, pixel_y: float, size_x: float, size_y: float) -> Point:
    return Point(pixel_x / size_x, pixel_y / size_y)
