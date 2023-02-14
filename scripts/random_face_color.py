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

def removeUnusedRandoms():
    unusedRandoms = getUnusedRandoms()
    for mat in unusedRandoms:
        bpy.data.materials.remove( mat )

class RemoveUnusedRandomOp( bpy.types.Operator ):
    bl_label = "Remove Unused Randoms"
    bl_options = { 'REGISTER'}
    bl_idname = "material.remove_unusedmats"

    def execute( self, context ):
    removeUnusedRandoms()
    return {'FINISHED'}

class RandomMatOp( bpy.types.Operator ):
    bl_label = "Random Face Materials"
    bl_idname = "material.randommat"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute( self, context ):
        ob = context.active_object
        clearMaterialSlots( ob )
        removeUnusedRandoms()
        makeMaterials( ob )
        eassignMats2Ob( ob )
        return {'FINISHED'}

    @classmethod
    def poll( self, context ):
        ob = context.active_object
        return ob != None and ob.select

class RandomMatPanel( bpy.types.Panel ):
    bl_label = "Random Mat Panel"
    bl_region_type = "TOOLS"
    bl_space_type = "VIEW_3D"
    def draw( self, context ):
        self.layout.row().operator( "material.randommat" )
        row = self.layout.row()
        self.layout.row().operator( "material.remove_unusedmats" )
        matCount = len( getUnusedRandoms() )
        countLabel = "Unused Random Materials: %d" % matCount
        self.layout.row().label( countLabel )

def register():
    bpy.utils.register_class( RemoveUnusedRandomOp )
    bpy.utils.register_class( RandomMatOp )
    bpy.utils.register_class( RandomMatPanel )

def unregister():
    bpy.utils.unregister_class( RandomMatPanel )
    bpy.utils.unregister_class( RandomMatOp )
    bpy.utils.unregister_class( RemoveUnusedRandomOp )

if __name__ == '__main__':
    register()
