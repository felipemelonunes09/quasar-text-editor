import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PALLETE = 'dark-pallete'

FS_PALLETES_DIR = os.path.join(BASE_DIR, 'styles', 'palletes')
FS_PALLETE_FILE = os.path.join(FS_PALLETES_DIR, 'fs-palletes.yml')

ICON_PATH = os.path.join(BASE_DIR, 'assets', 'img', 'icons')

FOLDER_ICON_PATH = os.path.join(ICON_PATH, 'folder-tree.png')
RULER_ICON_PATH = os.path.join(ICON_PATH, 'ruler.png')
ROCKET_ICON_PATH   = os.path.join(ICON_PATH, 'rocket.png')

HIGHLIGHT_PATH = os.path.join(BASE_DIR, 'assets', 'highlights')
MAP_EXTENSION_FILE = {
    '.qs': 'quasar.json'
}



