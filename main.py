import tkinter as tk
import config
import Menu

from shared import utils
from screens.AttributeScreen import AttributeScreen
from screens.EditorScreen import EditorScreen

class QuasarEditor:
    def __init__(self, root, workspace = None):
        
        # Set up the main window
        self.root = root
        self.root.title("QuasarEditor")

        # Create the two frames with different background colors
        self.edit_screen        = EditorScreen(self.root, self)
        self.attribute_screen   = AttributeScreen(self.root)
        self.menu               = Menu.Menu(root, self)
            
        self.edit_screen.show_default()
        self.menu.create()
        
        self.__loaded_content = None
        self.__content_type   = None
        self.__current_path   = None
        

    def load_file(self):
        path = utils.open_file()
        if path:
            with open(path, 'r') as file:
                self.set_loaded_content(file.read())
                self.set_content_type('FILE')
                self.set_current_path(path)
            
            self.edit_screen.show_editor(self.loaded_content)        
            self.attribute_screen.show_filetree(path)
            
    def load_dir(self):
        path = utils.open_dir()
        if path:
            self.attribute_screen.show_dirtree(path)
            self.set_loaded_content(path)
            self.set_current_path(path)
            self.set_content_type('DIR')
            self.edit_screen.show_editor("")
            
    def new_file(self):
        self.set_content_type('FILE')
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

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuasarEditor(root)
    root.mainloop()
