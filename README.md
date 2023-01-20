# Tractography loader for Blender 3D

The easiest way to work with brain tractography within Blender 3D is to either load them from .tck or .trk files (from DIPY or MRTRIX) or to compute them directly from Blender's Python console.
 
<img src="https://github.com/alecrimi/python_blender/blob/main/Capture_TRK.PNG"  height="200"> 
<img src="https://github.com/alecrimi/python_blender/blob/main/Capture_Blender.PNG"   height="200">

## Setup

First, you need to make sure that Blender has access to the path where you will want to install some dependencies. To know what are the valid paths in your system type the following commands in Blender's python console:

```python
import sys
print(sys.path)
```

You should see something like this:

<img src="https://user-images.githubusercontent.com/9929496/213748854-13fa18b7-4b55-48d2-8781-3006b40b6a75.png">

 Next, execute the script `install_libs.py` which will install the required libraries. This might not work for all systems so, make sure that these dependencies are present in one of the paths (`sys.path`) to which Blender has access.

Then you need to load the streamlines and convert them into NURBS or anything that is Blender manageble.

See the full explanation in the video below

[![Using brain tractography with Nibabel or Dipy directly from Blender 3D](https://img.youtube.com/vi/ANkq9EAEEeI/0.jpg)](https://www.youtube.com/watch?v=ANkq9EAEEeI "Using brain tractography with Nibabel or Dipy directly from Blender 3D")

## Installation

For ease of use we have included the script `import_tractogram.py` that adds the menu item **Tractogram (.trk)** to the **File** > **Import** menu.

<img src="https://user-images.githubusercontent.com/9929496/213745671-9b84c624-0ab2-463a-93de-dc9c6e21dc50.png">

To install it, import the script in Blender's text editor and execute it.
