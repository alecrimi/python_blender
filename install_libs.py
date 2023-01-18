import subprocess
import sys

#Install Nibabel and Dipy from within the Blender Python interface
subprocess.check_call([sys.executable, "-m", "pip", "install", "nibabel"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "dipy"])
