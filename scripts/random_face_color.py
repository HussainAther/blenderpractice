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

def assignMats2Ob( ob ):
    mats = bpy.data.materials
    # load up the materials into the material slots
    for mat in mats:
        bpy.ops.object.material_slot_add()
        ob.active_material = mat
 
    # tie the loaded up materials o each of the faces
    i=0
    faces = ob.data.faces
    while i < len( faces ):
        faces[i].material_index = i
    i+=1


getUnusedRandoms = lambda : [ x for x in bpy.data.materials
    if x.name.startswith( "randmat" ) and x.users == 0 ]

def clearMaterialSlots( ob ):
    while len( ob.material_slots ) > 0:
        bpy.ops.object.material_slot_remove()
