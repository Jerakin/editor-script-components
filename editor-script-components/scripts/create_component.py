"""
Editor script to create a component for the provided resource
"""
from pathlib import Path
import deftree
import sys

# If we need to do some debug printing
# sys.stdout = open(Path("python_log.txt"), 'w')


_anchor = Path("/").anchor

def _fix_path(path, suffix):
    """We have to remove the anchor if there is one"""
    if path.anchor == _anchor:
        path = Path(str(path)[1:])
    return Path().cwd() / path.with_suffix(suffix)

def sound(path):
    tree = deftree.DefTree()
    root = tree.get_root()
    root.add_attribute("sound", path.as_posix())
    root.add_attribute("looping", 0)
    root.add_attribute("group", "master")
    root.add_attribute("gain", 1.0)
    root.add_attribute("pan", 0.0)
    root.add_attribute("speed", 1.0)
    tree.write(_fix_path(path, ".sound"))

def spine_scene(path):
    tree = deftree.DefTree()
    root = tree.get_root()
    root.add_attribute("spine_json", path.as_posix())
    root.add_attribute("atlas", "")
    root.add_attribute("sample_rate", 30)
    tree.write(_fix_path(path, ".spinescene"))

def spine_model(path):
    tree = deftree.DefTree()
    root = tree.get_root()
    root.add_attribute("spine_scene", path.as_posix())
    root.add_attribute("default_animation", "")
    root.add_attribute("skin", "")
    tree.write(_fix_path(path, ".spinemodel"))

def atlas(paths):
    first_path = paths[0]
    tree = deftree.DefTree()
    root = tree.get_root()
    for path in paths:
        images = root.add_element("images")
        images.add_attribute("image", path.as_posix())
    root.add_attribute("margin", 0)
    root.add_attribute("extrude_borders", 2)
    root.add_attribute("inner_padding", 0)

    if first_path.anchor == _anchor:
        first_path = Path(str(first_path)[1:])
    first_path = Path().cwd() / first_path.with_name("NEW_ATLAS.atlas")

    tree.write(first_path)

resource_map = {".wav": sound,
                ".ogg": sound,
                ".json":spine_scene,
                ".spinescene":spine_model
                }

def main(paths):
    paths =[Path(path) for path in paths]
    if len([path for path in paths if path.suffix == ".png"]) == len(paths):
        atlas(paths)
    else:
        for path in paths:
            path = Path(path)
            if path.suffix in resource_map:
                resource_map[path.suffix](path)

if __name__ == '__main__':
    main(sys.argv[1:])

