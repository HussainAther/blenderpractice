#N-body simulation rendering with Blender

'''
Please note that this Python script should be run inside
the Blender environment.
'''

import math
import bpy
import pickle
import glob     #glob can be used to read a directory of snapshot files
import csv

# MODIFY THIS TO THE DIRECTORY ON YOUR COMPUTER!
filepath = '/export/data_2/blender/threebody/text/0000b.txt'

'''
#This section can be used to remove all objects if so desired
for object in bpy.data.scenes['Scene'].objects: 
    if 'point.' in object.name:
        #print(object.name)
        #bpy.context.scene.objects.active = bpy.data.objects[object.name]
        bpy.data.objects[object.name].select = True
        bpy.ops.object.delete()
        #bpy.data.scenes['Scene'].objects.unlink(bpy.context.active_object)
'''




###################################################################

#Set original file and positions for loading a single 
bpy.ops.anim.change_frame(frame=1)
fields = ['xdisk', 'ydisk', 'zdisk']
reader = csv.DictReader(open(filepath), fields, delimiter=',')


for row in reader:
    bpy.ops.object.duplicate()
    bpy.context.active_object.location.xyz=(float(row['xdisk'])/10.0, float(row['ydisk'])/10.0, float(row['zdisk'])/10.0)

############################################################################################

