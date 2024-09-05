import tkinter as tk
import config
import Menu
import yaml

from types import SimpleNamespace
from core.file_handlers import FileLoader
from shared import utils
from core.screens.AttributeScreen import AttributeScreen
from core.screens.EditorScreen import EditorScreen
from core.file_objects import File
from styles import style

class QuasarEditor:
    def __init__(self, root):
        
        self.__pallete        = None
        self.root = root
        self.set_pallete(config.FS_PALLETES_DIR, config.FS_PALLETE_FILE, config.PALLETE)
        
        self.root = root
        self.root.title("<QuasarEditor>")

        self.edit_screen        = EditorScreen(self.root, self)
        self.attribute_screen   = AttributeScreen(self.root, self)
        self.menu               = Menu.Menu(root, self)
        
        self.__current_file: File = None
        
        self.edit_screen.show_default()
        self.menu.create()
        
        style.configure(root)
        
    def set_pallete(self, dir_pallete: str, file_pallete: str, theme: str):
        
        self.__pallete = SimpleNamespace()
        
        with open(f"{dir_pallete}/{file_pallete}", 'r') as file:
            object = yaml.safe_load(file)
        
        for key in object[theme]:
            self.__pallete.__setattr__(key, object[theme][key])

    def load_file(self, file: File = None):
               
        self.set_current_file(file=file)
        file_loader = FileLoader(file=file)
        
        self.edit_screen.show_editor(file_loader.load())        
            
    def load_dir(self):
        path = utils.open_dir()
            
        self.attribute_screen.show_dirtree(path)
        self.edit_screen.show_editor("")
            
    def new_file(self):
        self.edit_screen.set_visible()
        self.edit_screen.show_editor("")
    
    def get_current_file(self) -> File:
        return self.__current_file
    
    def get_pallete(self):
        return self.__pallete
        
    def get_content(self):
        return self.edit_screen.get_text()
    
    def set_current_file(self, file: File):
        self.__current_file = file
    


# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuasarEditor(root)
    root.mainloop()



