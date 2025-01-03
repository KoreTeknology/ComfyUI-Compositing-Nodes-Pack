import importlib.util
import glob
import os
import sys
from .nai import init
#from .nai import init, get_ext_dir

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# --------------------
def get_ext_dir(subpath=None, mkdir=False):
    dir = os.path.dirname(__file__)
    if subpath is not None:
        dir = os.path.join(dir, subpath)

    dir = os.path.abspath(dir)

    if mkdir and not os.path.exists(dir):
        os.makedirs(dir)
    return dir

# --------------------

if init():
    # CHECK FOR NODES DIRECTORY
    py = get_ext_dir("nodes")
    # CHECK FOR FILES
    files = glob.glob(os.path.join(py, "*.py"), recursive=False)

    for file in files:
        name = os.path.splitext(file)[0]
        spec = importlib.util.spec_from_file_location(name, file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        # Console list of all the nodes files
        #print("🛡️ComfyUI Compositing Nodes Pack: Loading " + name)
        # Register and update each class from the files
        if hasattr(module, "NODE_CLASS_MAPPINGS") and getattr(module, "NODE_CLASS_MAPPINGS") is not None:
            NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
            if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS") and getattr(module, "NODE_DISPLAY_NAME_MAPPINGS") is not None:
                NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
    
    print("")
    print("🛡️ ComfyUI Compositing Nodes Pack......................[LOADED]")
    print("")

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
