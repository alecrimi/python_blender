import nibabel as nib
import bpy
import numpy as np

# Load the trackvis file
CST = nib.streamlines.load('CST.trk') 
# Access the streamline data
streamlines = list(CST.streamlines)

# Iterate over the streamlines
for i, sl in enumerate(streamlines):
   # Create a new curve object
   curve = bpy.data.curves.new(name='Streamline {}'.format(i), type='CURVE')
   curve.dimensions = '3D'
   # Create a new curve spline
   spline = curve.splines.new('NURBS')
   spline.points.add(len(sl) - 1)
   # Set the control points of the spline
   for j, point in enumerate(sl): 
        spline.points[j].co = np.append(point, 1) #Append the w coordinate for the homogenous coordinates.

# Create an object for the curve and link it to the scene
obj = bpy.data.objects.new('Streamline {}'.format(i), curve)
bpy.context.collection.objects.link( obj )
