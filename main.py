import tkinter as tk
import config
import Menu
import yaml

from types import SimpleNamespace
from core.file_handlers import FileLoader
from shared import utils
from screens.AttributeScreen import AttributeScreen
from screens.EditorScreen import EditorScreen
from core.file_objects import File


class QuasarEditor:
    def __init__(self, root, workspace = None):
        
        
        self.__pallete        = None
        self.set_pallete(config.FS_PALLETES_DIR, config.FS_PALLETE_FILE, config.PALLETE)
        
        # Set up the main window
        self.root = root
        self.root.title("QuasarEditor")

        # Create the two frames with different background colors
        self.edit_screen        = EditorScreen(self.root, self)
        self.attribute_screen   = AttributeScreen(self.root, self)
        self.menu               = Menu.Menu(root, self)
            
        self.edit_screen.show_default()
        self.menu.create()
        
        self.__loaded_content = None
        self.__content_type   = None
        self.__current_path   = None
        
        
    def set_pallete(self, dir_pallete: str, file_pallete: str, theme: str):
        
        self.__pallete = SimpleNamespace()
        
        with open(f"{dir_pallete}/{file_pallete}", 'r') as file:
            object = yaml.safe_load(file)
        
        for key in object[theme]:
            self.__pallete.__setattr__(key, object[theme][key])


    def load_theme(self, theme):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Button):
                child.config(bg=theme['primary'], fg=theme['text'])
            elif isinstance(child, tk.Label):
                child.config(bg=theme['background'], fg=theme['text'])
            elif isinstance(child, tk.Frame):
                child.config(bg=theme['background'])
            else:
                child.config(bg=theme['background'], fg=theme['text'])
        

    def load_file(self, file: File = None):
                
        file_loader = FileLoader(file=file)
        self.set_loaded_content(file_loader.load())
        self.set_content_type('FILE')
        self.set_current_path(file.get_path())
        
        self.edit_screen.show_editor(self.__loaded_content)        
            
    def load_dir(self):
        path = utils.open_dir()
        if path:
            self.set_loaded_content(path)
            self.set_current_path(path)
            self.set_content_type('DIR')
            
            self.attribute_screen.show_dirtree(path)
            self.edit_screen.show_editor("")
            
    def new_file(self):
        self.set_content_type('FILE')
        self.edit_screen.set_visible()
        self.edit_screen.show_editor("")
        
    def get_content(self):
        return self.edit_screen.get_text()
    
    def get_context(self):
        return (self.__current_path, self.__content_type, self.__loaded_content)
    
    def set_current_path(self, path: str):
        self.__current_path = path
        
    def set_loaded_content(self, content: str):
        self.__loaded_content = content
        
    def set_content_type(self, type):
        self.__content_type = type
        
    def get_pallete(self):
        return self.__pallete

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuasarEditor(root)
    root.mainloop()

