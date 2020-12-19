import bpy

def delete_all():
    for item in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.unlink(item)

    for item in bpy.data.objects:
        bpy.data.objects.remove(item)

    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

    for item in bpy.data.materials:
        bpy.data.materials.remove(item)

delete_all()