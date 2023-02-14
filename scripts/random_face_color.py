import bpy
import time
from random import random, seed

# start simple be just generating random colors
def getRandomColor():
    seed( time.time() )
    red = random()
    green = random()
    blue = random()
    return red, green, blue

def makeMaterials( ob ):
    for face in ob.data.faces:
        randcolor = getRandomColor()
        mat = bpy.data.materials.new( "randmat" )
        mat.diffuse_color = randcolor
