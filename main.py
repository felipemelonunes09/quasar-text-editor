import tkinter as tk
from tkinter import ttk
import config
import Menu
import yaml

from core.frames.StartFrame import StartFrame
from shared import utils
from types import SimpleNamespace
from core.file_handlers import FileLoader
from core.frames.AttributesFrame import AttributesFrame
from core.frames.EditorFrame import EditorFrame
from core.file_objects import File
from styles import style

class QuasarEditor:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("<QuasarEditor>")    
        self.__current_file: File = None
        self.menu = Menu.Menu(root, self)
        self.menu.create()
        
        self.attributes_frame = AttributesFrame(root, self, bg="#06141B")
        self.editor_frame = EditorFrame(root, self, bg="#11212D")
        self.start_frame = StartFrame(root, self, bg="#06141B", width=500, height=500)   

        self.start_frame.pack(fill="both", expand=True)
        style.configure(root)

    def load_file(self, file: File = None):
        self.start_frame.forget()
        self.editor_frame.pack(fill=tk.BOTH, side="right", expand=True)
        self.set_current_file(file=file)
        #file_loader = FileLoader(file=file)
        #self.editor_frame.show_editor(file_loader.load())        
        self.editor_frame.load_file(file)
            
    def load_dir(self):
        path = utils.open_dir()
        self.start_frame.forget()
        self.attributes_frame.pack(fill=tk.BOTH, side="left", expand=False)
        self.editor_frame.pack(fill=tk.BOTH, side="right", expand=True)
        self.attributes_frame.show_tree(path)
        self.editor_frame.show_editor("")
            
    def new_file(self):
        self.start_frame.forget()
        self.attributes_frame.forget()
        self.editor_frame.pack(fill=tk.BOTH, expand=True)
        self.editor_frame.show_editor("")
        
    def exit(self):
        self.attributes_frame.forget()
        self.editor_frame.forget()
        self.start_frame.pack(fill="both", expand=True)
        self.set_current_file(None)
    
    def get_current_file(self) -> File:
        return self.__current_file
    
    def get_pallete(self):
        return self.__pallete
        
    def get_content(self):
        return self.editor_frame.get_text()
    
    def set_current_file(self, file: File):
        self.__current_file = file

# Create the main window and run the application
if __name__ == "__main__":#
    root = tk.Tk()
    app = QuasarEditor(root)
    root.mainloop()
