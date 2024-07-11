from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
from veclib import vec3
from particle import particle

class Bullet:
    def __init__(self, part):
        self.particle = part


    def render(self):

        self.simUpdate()
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(2,2,2)
        glPushMatrix()
        glTranslatef(self.particle.pos.a, self.particle.pos.b, self.particle.pos.c)
        glutSolidSphere(0.05, 40, 40)
        glPopMatrix()
        glFlush()
        glutPostRedisplay()
    def simUpdate(self):
        duration = 0.01
        self.particle.integrate(duration)
        duration+= 1

    def fire(self, x, y):
        self.particle.setPos(vec3(x,y,0))
        self.particle.setVel(vec3(0.5,0.5,0))
        self.particle.setAcc(vec3(0,-0.3,0))
        self.particle.setDamping(0.99)
        self.particle.setinvMass(1/2)

glutInit(sys.argv)

glutInitWindowSize(1000,1000)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutCreateWindow(b"Ballistic Demo")
glViewport(1,1,1000,1000)
glMatrixMode( GL_PROJECTION )
glLoadIdentity()
w = glutGet( GLUT_WINDOW_WIDTH ) / 300.0
h = glutGet( GLUT_WINDOW_HEIGHT ) / 300.0
glOrtho( -1 * w, 1 * w, -1 * h, 1 * h, 10, -10)

glMatrixMode( GL_MODELVIEW )
glLoadIdentity(); 
shot = Bullet(particle())
shot.fire(-2,1)

glutDisplayFunc(shot.render)
glutMainLoop()
