bl_info = {
    "name": "camera_viz",
    "author": "anton",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
from mathutils import Matrix
import csv
from random import random
from os import listdir
from os.path import isfile, join
from datetime import datetime

def add_object(self, context):
    scale_x = self.scale.x
    scale_y = self.scale.y

    verts = [
        Vector((-1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, -1 * scale_y, 0)),
        Vector((-1 * scale_x, -1 * scale_y, 0)),
    ]

    edges = []
    faces = [[0, 1, 2, 3]]

    mesh = bpy.data.meshes.new(name="New Object Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)


class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_object"
    bl_label = "Add Mesh Object"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        add_object(self, context)

        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Add Object",
        icon='PLUGIN')


def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def spawnCameras(train_frames, test_frames, pose_path): 
    # the red will decrease by 0.05 with every camera spawned
    if len(train_frames) > 0:
        # add parent for cleaner hierarchy
        parent_train_object = bpy.data.objects.new('train_views', None)
        bpy.context.collection.objects.link(parent_train_object)
        color_r = [1, 0, 0, 0]
        for train_frame in train_frames: 
            f = pose_path + train_frame + ".txt"
            matr = Matrix(((0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0)))      
            row = 0
            with open(f, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    tmplist = []
                    for item in line.split(): 
                        tmplist.append(float(item))
                    v = Vector(tmplist) 
                    matr[row] = v
                    row += 1
            addCamera(train_frame, matr, color_r, parent_train_object)    
            color_r[0] -= 1/(len(train_frames)+1)
    
    if len(test_frames) > 0:
        # add parent for cleaner hierarchy
        parent_test_object = bpy.data.objects.new('test_views', None)
        bpy.context.collection.objects.link(parent_test_object)
        color_g = [0, 1, 0, 0]
        for test_frame in test_frames: 
            f = pose_path + test_frame + ".txt"
            matr = Matrix(((0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0)))      
            row = 0
            with open(f, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    tmplist = []
                    for item in line.split(): 
                        tmplist.append(float(item))
                    v = Vector(tmplist) 
                    matr[row] = v
                    row += 1
            addCamera(test_frame, matr, color_g, parent_test_object)    
            color_g[1] -= 1/(len(test_frames)+1)        
        
def addCamera(frame, matr, color, parent_object):
    # define vertices for a simple pyramid
    fov_width = 0.15
    fov_height = 0.15
    # needs to be negative
    focal_length = -0.25
    verts = [(0,0,0),(0,fov_width,0),(fov_height,fov_width,0),(fov_height,0,0),(fov_height/2,fov_width/2,focal_length)]
    faces = [(0,1,2,3), (0,4,1),(1,4,2),(2,4,3),(3,4,0)]
    mesh = bpy.data.meshes.new(frame)
    cam_object = bpy.data.objects.new(frame, mesh)
    cam_object.parent = parent_object
    bpy.context.collection.objects.link(cam_object)    
    mesh.from_pydata(verts,[],faces)
    # assign color to pyramid
    if(len(mesh.materials) < 1):
        mat = bpy.data.materials.new('newMat')
        bpy.data.objects[frame].data.materials.append(mat)
    bpy.data.objects[frame].data.materials[0].diffuse_color = color
    mesh.transform(matr)
    mesh.update()

def getFrames(csv_path):
    frames = []
    with open(csv_path, newline='') as csvfile:
        framereader = csv.reader(csvfile, delimiter = '"', quotechar = '|')
        for row in framereader: 
            frame = ', '.join(row)
            frames.append(frame[:-4])
    return frames
    
def setVertColors():
    newmat = bpy.data.materials.new("VertCol")
    newmat.use_nodes = True
    node_tree = newmat.node_tree
    nodes = node_tree.nodes
    bsdf = nodes.get("Principled BSDF") 
    assert(bsdf) # make sure it exists to continue
    vcol = nodes.new(type="ShaderNodeVertexColor")
    vcol.layer_name = "Col" # the vertex color layer name
    # make links
    node_tree.links.new(vcol.outputs[0], bsdf.inputs[0])
    return newmat

def loadScanNetMesh(scene_path): 
    bpy.ops.import_mesh.ply(filepath=scene_path)
    room = bpy.context.object
    roommat = setVertColors()
    # Assign it to object
    if room.data.materials:
        # assign to 1st material slot
        room.data.materials[0] = roommat
    else:
        # no slots
        room.data.materials.append(roommat)
    #bpy.data.materials["Material.001"].node_tree.nodes["Vertex Color"].layer_name = "Col"
    
if __name__ == "__main__":
    
    # CONFIG ----------------
    scene_id = "scene0000_00"
    use_test = False
    export_obj = True
    all_poses = True
    #------------------------
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    save_path = "/home/anton/code/ss22/practicum/progress/date/" + scene_id + "_viz.obj"
    scene_path = "/home/anton/code/ss22/practicum/data/scans/scans_test/" + scene_id + "/" + scene_id + "_vh_clean_2.ply"
    train_csv = "/home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/data_samples/" + scene_id + "/train_set.csv"
    test_csv = "/home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/data_samples/" + scene_id + "/test_set.csv"
    pose_path = "/home/anton/code/ss22/practicum/data/scans/scans_test/" + scene_id + "/pose/"
    
    loadScanNetMesh(scene_path)
    print("Loaded ScanNet Scene!")
    if all_poses == True: 
        train_frames = [file[:-4] for file in listdir(pose_path) if isfile(join(pose_path, file))]
    else: 
        train_frames = getFrames(train_csv)
    print(train_frames[0])
    if use_test:
        test_frames = getFrames(test_csv)
    else: 
        test_frames = []
    spawnCameras(train_frames, test_frames, pose_path)
    bpy.ops.view3d.camera_to_view_selected()
    if export_obj:
        bpy.ops.export_scene.obj(filepath=save_path, use_vertex_groups=True)
