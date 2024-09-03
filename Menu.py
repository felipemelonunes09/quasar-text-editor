import tkinter as tk
from shared import utils

from core.file_handlers import FileWriter

class Menu():
    
    def __init__(self, root, editor) -> None:
        self.root = root
        self.editor = editor
        
    def on_save(self, *args, **kwd):
        
        file_write = FileWriter(file=self.editor.get_current_file(), content=self.editor.get_content())
        file_write.write()
    
    def create(self) -> None:
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.on_save)
        
        self.root.bind('<Control-s>', self.on_save)
