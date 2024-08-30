import tkinter as tk
from shared import utils

class Menu():
    
    def __init__(self, root, editor) -> None:
        self.root = root
        self.editor = editor
        
    def on_save(self, *args, **kwd):
        
        path, type, _ = self.editor.get_context()
        
        # case its a file loaded into the editor
        if type == 'FILE':
            
            content = self.editor.get_content()
            # this make sure that its path in case there is no path, it means that its a file that is beaing created in the editor
            print(path)
            print(not path)
            if not path:
                
                print("\t(*) Path not founded, opening dialog box")
                
                path = utils.open_save_file()
                self.editor.set_current_path(path)
            
            with open(path, 'w') as file:
                file.write(content)
    
    def create(self) -> None:
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.on_save)
        
        self.root.bind('<Control-s>', self.on_save)
