import os
import bpy
from mathutils import *
from math import *

h_resolution = 256
v_resolution = 512

def render_sides(output_dir, output_file_pattern_string = 'render%d.jpg', rotation_steps = 32, subject = bpy.context.object):
  bpy.context.scene.camera.data.ortho_scale = subject.dimensions.z
  bpy.context.scene.render.resolution_x = h_resolution
  bpy.context.scene.render.resolution_y = v_resolution
  rotation_angle = 360.0
  for step in range(0, rotation_steps):
    angle = radians(step * (rotation_angle / rotation_steps))
    radius = max(subject.dimensions.x, subject.dimensions.y)
    bpy.context.scene.camera.location = (cos(angle) * radius, sin(angle) * radius, subject.dimensions.z/2)
    bpy.context.scene.camera.rotation_euler = (radians(90), 0, angle + radians(90))
    bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % step))
    bpy.ops.render.render(write_still = True)

def render_top(output_dir, output_file_pattern_string = 'render%d.jpg', subject = bpy.context.object, and_bottom = False):
  bpy.context.scene.camera.data.ortho_scale = max(subject.dimensions.x, subject.dimensions.y)
  bpy.context.scene.render.resolution_x = h_resolution
  bpy.context.scene.render.resolution_y = h_resolution
  bpy.context.scene.camera.location = (0,0, subject.dimensions.z)
  bpy.context.scene.camera.rotation_euler = (0, 0, 0)
  bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % 'top'))
  bpy.ops.render.render(write_still = True)
  if(and_bottom):
    bpy.context.scene.camera.location = (0,0,0)
    bpy.context.scene.camera.rotation_euler = (radians(180), 0, 0)
    bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % 'bottom'))
    bpy.ops.render.render(write_still = True)



#bpy.context.scene.display.shading.light = 'MATCAP'
#rotate_and_render('/Users/lshehane/Downloads/BlenderProjects/BillboardGen/', 'rendernormal%d.jpg', 4)
#bpy.context.scene.display.shading.light = 'FLAT'
subject = bpy.context.object
rotate_and_render('/Users/lshehane/Downloads/BlenderProjects/BillboardGen/', subject.name + '_%d.png', 4, subject)
top_and_render('/Users/lshehane/Downloads/BlenderProjects/BillboardGen/', subject.name + '_%s.png', subject, True)
