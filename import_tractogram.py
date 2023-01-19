import bpy
import nibabel as nib
import numpy as np
import os

from bpy.props import StringProperty
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper


def load_tractogram(context, filepath):
    print('Attempting to load tractogram: {}'.format(filepath))
    filename = os.path.splitext(os.path.basename(filepath))[0]
    print('Loading file...')
    data = nib.streamlines.load(filepath)
    # Access the streamline data
    print('Accessing data...')
    streamlines = list(data.streamlines)
    # Accessing a custom collection
    print('Accessing "{}" collection...'.format(filename))
    if (bpy.data.collections.find(filename) == True):
        sls_col = bpy.data.collections[filename]
    else:
        sls_col = bpy.data.collections.new(filename)
        bpy.context.scene.collection.children.link(sls_col)
    # Iterate over the streamlines
    print('Converting lines to NURBS...')
    for i, sl in enumerate(streamlines):
        # Create a new curve object
        curve = bpy.data.curves.new(name='Streamline {}'.format(i), type='CURVE')
        curve.dimensions = '3D'
        # Create a new curve spline
        spline = curve.splines.new('NURBS')
        spline.points.add(len(sl) - 1)
        # Set the control points of the spline
        for j, point in enumerate(sl):
            spline.points[j].co = np.append(point, 1)
        # Create an object for the curve and link it to the scene
        obj = bpy.data.objects.new('Streamline {}'.format(i), curve)
        sls_col.objects.link(obj)
    print('Tractogram loaded')
    return {'FINISHED'}


class TractogramImportHelper(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    # Important since its how bpy.ops.import_helper.tractogram is constructed
    bl_idname = 'import_helper.tractogram'
    bl_label = 'Import tractogram'
    
    # ImportHelper mixin class uses this
    filename_ext = ".trk"
    
    filter_glob: StringProperty(
        default='*.trk',
        options={'HIDDEN'},
    )
    
    # List of operator properties, the attributes will be assigned to the class instance
    # from the operator settings before calling
    
    def execute(self, context):
        return load_tractogram(context, self.filepath)

# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(TractogramImportHelper.bl_idname, text='Tractogram (.trk)')

    
def register():
    bpy.utils.register_class(TractogramImportHelper)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(TractogramImportHelper)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == '__main__':
    register()
