bl_info = {
    "name": "Dimensions Panel",
    "author": "Hunanbean, with ChatGPT4",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "description": "Add a Dimensions panel to the Object Properties. Due to Blender design, I cannot seem to add it directly to the existing Transform Panel. It must be its own",
    "category": "Object",
    "location": "Properties > Object > Dimensions",
}

import bpy

# Custom operator to apply scale
class OBJECT_OT_ApplyScale(bpy.types.Operator):
    bl_idname = "object.apply_scale"
    bl_label = "Apply Scale"
    
    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        return {'FINISHED'}

# Custom operator to apply rotation
class OBJECT_OT_ApplyRotation(bpy.types.Operator):
    bl_idname = "object.apply_rotation"
    bl_label = "Apply Rotation"
    
    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        return {'FINISHED'}

# Custom operator to apply location
class OBJECT_OT_ApplyLocation(bpy.types.Operator):
    bl_idname = "object.apply_location"
    bl_label = "Apply Location"
    
    def execute(self, context):
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
        return {'FINISHED'}

class OBJECT_PT_CustomDimensions(bpy.types.Panel):
    bl_label = "Transform"
    bl_idname = "OBJECT_PT_custom_dimensions"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        obj = context.object

        col = layout.column()
        row = col.row(align=True)
        row.prop(obj, "dimensions")

        # Add Apply Scale, Apply Rotation, and Apply Location buttons
        col.separator()
        col.operator("object.apply_scale", text="Apply Scale")
        col.operator("object.apply_rotation", text="Apply Rotation")
        col.operator("object.apply_location", text="Apply Location")

def register():
    bpy.utils.register_class(OBJECT_PT_CustomDimensions)
    bpy.utils.register_class(OBJECT_OT_ApplyScale)
    bpy.utils.register_class(OBJECT_OT_ApplyRotation)
    bpy.utils.register_class(OBJECT_OT_ApplyLocation)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_CustomDimensions)
    bpy.utils.unregister_class(OBJECT_OT_ApplyScale)
    bpy.utils.unregister_class(OBJECT_OT_ApplyRotation)
    bpy.utils.unregister_class(OBJECT_OT_ApplyLocation)

if __name__ == "__main__":
    register()
