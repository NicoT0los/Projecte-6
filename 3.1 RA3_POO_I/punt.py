import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        return math.sqrt((self.x - altre.x)**2 + (self.y - altre.y)**2)
