from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
from veclib import vec3
from particle import particle
import datetime

class Bullet:
    def __init__(self, part):
        self.particle = part

    def render(self):
        glColor3f(2,2,2)
        glPushMatrix()
        glTranslatef(self.particle.pos.a, self.particle.pos.b, self.particle.pos.c)
        glutSolidSphere(0.01, 20, 20)
        glPopMatrix()

        glColor3f(0.75, 0.75, 0.75)
        glPushMatrix()
        glTranslatef(self.particle.pos.a, 0, self.particle.pos.c)
        glScalef(1.0, 0.1, 1.0)
        glutSolidSphere(0.01, 20, 20)
        glPopMatrix()
        glFlush()

def fire(bullet):
    bullet.particle.setPos(vec3(-2,0.2,0))
    bullet.particle.setVel(vec3(2,0,0))
    bullet.particle.setAcc(vec3(0,-0.05,0))
    bullet.particle.setDamping(0.99)
    bullet.particle.setinvMass(1/2)

def simUpdate(bullet):
    duration = 0.01
    bullet.particle.integrate(duration)
    #duration += 1/1000
    #print(duration)

glutInit(sys.argv)

glutInitWindowSize(1000,1000)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutCreateWindow(b"Ballistic Demo")
glViewport(1,1,1000,1000)
shot = Bullet(particle())

fire(shot)
while True:
    
    simUpdate(shot)
    print(shot.particle)
    shot.render()