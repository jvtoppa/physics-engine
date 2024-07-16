from veclib import vec3

#position = vec3
#velocity = vec3
#acceleration = vec3
#invMass = 1/scalar
#damping = scalar
#forceAccum = vec3
#force = vec3

#The particle class per se
class particle:
    def __init__(self, position=0, velocity=0, acceleration=0, invMass=0, damping=0, forceAccum=0):
       self.pos = position
       self.vel = velocity
       self.acc = acceleration 
       self.invMass = invMass
       self.damping = damping
       self.forceAccum = forceAccum
    def getInvMass(self):
        return self.invMass
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
        #Remember that force should be added at the start (will persist during sim) or with addforce
        self.updateVel(self.acc*duration*0.5)
        self.updatePos(self.vel*duration)
        self.acc += self.forceAccum*self.invMass
        
    def addForce(self, force):
        self.forceAccum += force

    def DoDrag(self, duration):
        self.vel *= self.damping**duration

    def clearAccumulator(self):
        self.forceAccum = 0


    def __repr__(self):
        return "(" + str(self.pos) + ", " + str(self.vel) + ", " + str(self.acc) + ", " + str(self.invMass) + ", " + str(self.damping) + ")"
    
class ParticleForceGenerator:

    #updateForce can be overwritten with "class WhateverGen(ParticleForceGenerator)""
    #and then you just need to define the method again:
    #updateForce(self, _particle, duration)

    #this serves as a front to any force that acts upon any particle, generators must be implemented
    #separately


    def updateForce(self, _particle, duration):
        raise NotImplementedError("ForceGenerators must implement updateForce method")

#Holds all force generators and particles they apply to
#IMPORTANT!!!!! THIS IS JUST A NORMAL LIST, HOWEVER I TRIED TO IMPLEMENT IT LIKE THE BOOK SO ITS
# A LITTLE BIT CONFUSING (although I believe  it to be a little bit more organized)
#This follows a c++ structure, not as pythonic as I'd like it to be
           
class ParticleForceRegistry(ParticleForceGenerator):
    def __init__(self, duration=0):
        self.particleReg = []
    
    def updateForce(self, _particle, duration):
        return super().updateForce(_particle, duration)        

    def add(self, partiAndGen):
        self.particleReg.append(partiAndGen) #PARTIANDGEN IS A TUPLE (particle, generator)
    
    def remove(self, partiAndGen):
        self.particleReg.remove(partiAndGen)

    def clear(self):

        self.particleReg.clear()

    def updateForces(self, duration):
        for i in self.particleReg:
            self.updateForce(i[1], duration)

    def __repr__(self):
        return str(self.particleReg)

class ParticleGravity:
    def __init__(self, _particle, gravity):
        self.particle = _particle
        self.gravity = gravity

    def updateForce(self, duration):
        self.particle.addForce(self.gravity*self.particle.getInvMass(self))
