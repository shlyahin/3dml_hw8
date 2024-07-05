import bpy
import bpy_extras.object_utils
import math
import os

PATH = '/home/victor/mset/3d/3DML/ts_markup'

cam = bpy.data.objects['Camera']
obj = bpy.data.objects['Plane']
scene = bpy.context.scene



def update_border(camera, scene, object, step, split):

    matrix = object.matrix_world

    mesh = object.bound_box

    col0 = matrix.col[0]
    col1 = matrix.col[1]
    col2 = matrix.col[2]
    col3 = matrix.col[3]

    minX = 1
    maxX = 0
    minY = 1
    maxY = 0

    numVertices = len(mesh)

    for t in range(numVertices):
        co = mesh[t]
        pos = (col0 * co[0]) + (col1 * co[1]) + (col2 * co[2]) + col3
        pos = bpy_extras.object_utils.world_to_camera_view(scene, camera, pos)
    
        if pos.x < minX:
            minX = pos.x
        if pos.y < minY:
            minY = pos.y
        if pos.x > maxX:
            maxX = pos.x
        if pos.y > maxY:
            maxY = pos.y

    print(minX, minY, maxX, maxY)
    pMinX = minX
    pMinY = 1 - maxY
    pMaxX = maxX
    pMaxY = 1 - minY
    
    xc = (pMinX + pMaxX) / 2
    yc = (pMinY + pMaxY) / 2
    w = pMaxX - pMinX
    h = pMaxY - pMinY

    with open(os.path.join(PATH, 'labels', split, f"{step}.txt"), 'w') as f:
        f.write(f"0 {xc} {yc} {w} {h}\n")


j = 0

cam.rotation_euler = (-math.pi / 2, math.pi, 0)

target_angle = math.pi #/ 2
num_steps = 15
t_loc_x = 0
t_loc_y = 0

for r in [3, 5, 8, 10]:
    for t_loc_z in [1, 2, 3]:
        for x in range(num_steps):
            alpha = x * target_angle / num_steps
            cam.rotation_euler[2] = -alpha #-math.pi / 2 + alpha
            cam.location.x = t_loc_x + math.sin(alpha) * r
            cam.location.y = t_loc_y + math.cos(alpha) * r
            cam.location.z = t_loc_z
            
            if (j % 10) in [8, 9]:
                split = 'val'
            else:
                split = 'train'

            bpy.context.scene.render.filepath = os.path.join(PATH, 'images', split, f"{str(j)}.png")
            bpy.ops.render.render(write_still=True)
            
            update_border(cam, scene, obj, j, split)
            
            j += 1
    

    