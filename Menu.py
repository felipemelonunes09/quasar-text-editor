import tkinter as tk
from core.file_objects import File
from shared import utils

from core.file_handlers import FileWriter

class Menu():
    
    def __init__(self, root, editor) -> None:
        self.root = root
        self.editor = editor
        
    def __on_save(self, *args, **kwd):
        
        file = self.editor.get_current_file()    
        if(file.get_path() == None):
            file.set_path(utils.open_save_file())  
        file_write = FileWriter(file=file, content=self.editor.get_content())
        file_write.write()
        
    def __on_exit(self, *a, **k):
        self.editor.exit()
        
    def __on_split(self, *a, **k):
        self.editor.split()
    
    def create(self) -> None:
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.__on_save)
        file_menu.add_command(label="Exit", command=self.__on_exit)
        
        screen_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Editor", menu=screen_menu)
        screen_menu.add_command(label="Split", command=self.__on_split)
        self.root.bind('<Control-s>', self.__on_save)

