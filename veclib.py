import math

class vec3:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, o):
        return vec3(self.a + o.a, self.b + o.b, self.c + o.c)
    
    def __sub__(self, o):
        return vec3(self.a - o.a, self.b - o.b, self.c - o.c)

    def __truediv__(self, o):
        return vec3(self.a / o.a, self.b / o.b, self.c / o.c)

    def __mul__(self, o):
        return vec3(self.a * o, self.b * o, self.c * o)

    __rmul__ = __mul__

    def dotProduct(self, o):
        return vec3(self.a * o.a, self.b * o.b, self.c * o.c)
    
    def invert(self):
        return vec3(-self.a, -self.b, -self.c)
    
    def magnitude(self):
        return math.sqrt(self.a*self.a + self.b*self.b + self.c*self.c)
    
    def squareMagnitude(self):
        return self.a*self.a + self.b*self.b + self.c*self.c
    
    def normalize(self):
        if self.a or self.b or self.c != 0:

            selfmag = vec3.magnitude(vec3(self.a, self.b, self.c))
            return vec3(self.a/selfmag, self.b/selfmag, self.c/selfmag) 
        else:
            return vec3()
    
    def vecProd(self, o):
        return vec3(self.b*o.c-self.c*o.b,self.c*o.a-self.a*o.c,self.a*o.b-self.b*o.a)
    #returns prints as "(a, b, c)"
        
    def __repr__(self):
        return "(" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ")"
