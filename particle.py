from veclib import vec3

class particle:
    def __init__(self, position=0, velocity=0, acceleration=0, invMass=0, damping=0):
       self.pos = position
       self.vel = velocity
       self.acc = acceleration 
       self.invMass = invMass
       self.damping = damping

    def updatePos(self, vector):
        self.pos = self.pos + vec3(vector.a, vector.b, vector.c)

    def updateVel(self, vector):
        self.vel = self.vel + vec3(vector.a, vector.b, vector.c)

    def updateAcc(self, vector):
        self.acc = self.acc + vec3(vector.a, vector.b, vector.c)

    def setPos(self, vector):
        self.pos = vec3(vector.a, vector.b, vector.c)

    def setVel(self, vector):
        self.vel = vec3(vector.a, vector.b, vector.c)

    def setAcc(self, vector):
        self.acc = vec3(vector.a, vector.b, vector.c)

    def setinvMass(self, scalar):
        self.invMass = scalar

    def setDamping(self, scalar):
        self.damping = scalar    

    #During simulation integrate() should run on all 
    #frames that the particle is present 
    #p = dp/dt*t + d2p/dp2t^2/2
    
    def integrate(self, duration):
        self.updateVel(self.acc*duration)
        self.updatePos(self.vel*duration)
    
    def __repr__(self):
        return "(" + str(self.pos) + ", " + str(self.vel) + ", " + str(self.acc) + ", " + str(self.invMass) + ", " + str(self.damping) + ")"