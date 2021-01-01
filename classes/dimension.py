import math

class tuplexy:
    def __init__(self, xi, yi):
        self.x = xi
        self.y = yi
    
    def setx(self, xi):
        self.x = xi
    
    def sety(self, yi):
        self.y = yi
    
    def getx(self):
        return self.x

    def gety(self):
        return self.y
    
    def getx25(self):
        return math.trunc(self.x / 4)
    
    def getx75(self):
        return math.trunc((self.x / 4) * 3)
