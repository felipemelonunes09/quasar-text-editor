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
        
        self.loaded_content = None
        self.content_type   = None 
        self.current_path   = None
        

    def load_file(self):
        path = utils.open_file()
        if path:
            with open(path, 'r') as file:
                self.loaded_content = file.read()
                self.content_type = 'FILE'
                self.current_path = path
            
            self.edit_screen.show_editor(self.loaded_content)        
            self.attribute_screen.show_filetree(path)
            
    def load_dir(self):
        
        path = utils.open_dir()
        if path:
            self.attribute_screen.show_dirtree(path)
            
            self.loaded_content = path
            self.edit_screen.show_editor("")
            self.content_type = 'DIR'
            
    def new_file(self):
        self.edit_screen.show_editor("")
        
    def get_content(self):
        return self.edit_screen.get_text()
    
    def get_context(self):
        return (self.current_path, self.content_type, self.loaded_content)

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuasarEditor(root)
    root.mainloop()
