import csv
import glob
import os
import bpy
import bmesh

obj = bpy.data.objects['RocheOutline']
bpy.ops.object.mode_set(mode = 'EDIT')
bm = bmesh.from_edit_mesh(obj.data)
dicts = [{'X': xx[i], 'Y':yc[i]} for i in range(0,len(xx))]

#Add in vertex elements with XYZ coordinates at each row
for row in dicts:
xpos = row['X']
ypos = row['Y']
bm.verts.new((xpos,ypos,0.0))
bmesh.update_edit_mesh(obj.data)
#Note that the minus 2 is the number of points to connect
bm.edges.new((bm.verts[i] for i in range(-2,0)))
bmesh.update_edit_mesh(obj.data)
bpy.ops.object.mode_set(mode=’OBJECT’)
