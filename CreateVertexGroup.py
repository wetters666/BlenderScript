import bpy

# create vertex group for each bone.
def create_vertex_group():
    # get Bone name array for armature
    bone_names = []
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            # scan all bones
            bone_names = [bone.name for bone in obj.data.bones]
    # Create armatures for each mesh
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            targetobj = obj
            vertex_group_names = [vertex_group.name for vertex_group in targetobj.vertex_groups]
            for bone_name in bone_names:
                if not bone_name in vertex_group_names:
                    # create vertex group for bone name
                    targetobj.vertex_groups.new(name=bone_name)
    return

# 関数の実行例
create_vertex_group()
'''
add_vertexgroup(arg_objectname='Cube', arg_vertexgroup='CubeGroup')
'''