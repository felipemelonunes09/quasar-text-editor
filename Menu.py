import tkinter as tk
from core.file_objects import File
from shared import utils

from core.file_handlers import FileWriter

class Menu():
    
    def __init__(self, root, editor) -> None:
        self.root = root
        self.editor = editor
        
    def on_save(self, *args, **kwd):
        
        file = self.editor.get_current_file()      
        file_write = FileWriter(file=file, content=self.editor.get_content())
        file_write.write()
        
    def on_exit(self, *a, **k):
        self.editor.exit()
    
    def create(self) -> None:
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.on_save)
        file_menu.add_command(label="Exit", command=self.on_exit)
        self.root.bind('<Control-s>', self.on_save)

