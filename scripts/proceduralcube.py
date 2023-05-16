import bpy
import random

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Number of cubes to generate
num_cubes = 10

# Generate cubes
for i in range(num_cubes):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.object

    # Set random scale
    scale = random.uniform(0.5, 2.0)
    cube.scale = (scale, scale, scale)

    # Set random location
    x = random.uniform(-5.0, 5.0)
    y = random.uniform(-5.0, 5.0)
    z = random.uniform(0.0, 5.0)
    cube.location = (x, y, z)

    # Set random rotation
    rx = random.uniform(0.0, 360.0)
    ry = random.uniform(0.0, 360.0)
    rz = random.uniform(0.0, 360.0)
    cube.rotation_euler = (rx, ry, rz)

    # Set random material color
    material = bpy.data.materials.new(name='Cube Material')
    material.use_nodes = True
    material.node_tree.nodes.remove(material.node_tree.nodes.get('Principled BSDF'))
    material_output = material.node_tree.nodes.get('Material Output')
    rgb = [random.uniform(0.0, 1.0) for _ in range(3)]
    emission_node = material.node_tree.nodes.new('ShaderNodeEmission')
    emission_node.inputs['Color'].default_value = (rgb[0], rgb[1], rgb[2], 1.0)
    material.node_tree.links.new(emission_node.outputs['Emission'], material_output.inputs['Surface'])
    cube.data.materials.append(material)

