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
        self.menu = Menu.Menu(root, self)
        self.menu.create()
        self.attributes_frame = AttributesFrame(root, self, bg="#06141B", width=200)
        self.start_frame = StartFrame(root, self, bg="#06141B", width=500, height=500)   
        self.start_frame.pack(fill=tk.BOTH, expand=True)
        self.editor_frame: EditorFrame = None
        self.editors: list[EditorFrame] = list()
        style.configure(root)
        
    def split(self) -> None:
        n = self.add_new_editor()
        self.editor_frame = n
        
    def add_new_editor(self) -> EditorFrame:
        n = EditorFrame(root, self, on_focus_callback=self.__on_editor_focus)
        n.pack(fill=tk.BOTH, side="right", expand=True, before=self.editor_frame)
        self.editors.append(n)
        return n
    
    def get_current_editor(self) -> EditorFrame:
        if self.editor_frame == None or len(self.editors) == 0:
            editor = self.add_new_editor()
            self.editor_frame = editor
        return self.editor_frame

    def load_file(self, file: File = None):
        editor = self.get_current_editor()
        self.editor_frame.update()
        self.start_frame.forget()
        self.set_current_file(file=file)      
        editor.load_file(file)
            
    def load_dir(self):
        path = utils.open_dir()
        self.start_frame.forget()
        self.attributes_frame.pack(fill=tk.BOTH, side="left")
        editor = self.get_current_editor()
        self.attributes_frame.show_tree(path)
        editor.show_editor("")
            
    def new_file(self):
        self.start_frame.forget()
        self.attributes_frame.forget()
        editor = self.get_current_editor()
        editor.new_file()
        
    def exit(self):
        self.editor_frame.forget()
        for editor in self.editors:
            editor.forget()
            editor.set_current_file(None)
        self.attributes_frame.forget()
        self.start_frame.pack(fill=tk.BOTH, expand=True)
        
    def get_current_file(self) -> File:
        return self.editor_frame.get_current_file()
    
    def get_pallete(self):
        return self.__pallete
        
    def get_content(self):
        return self.editor_frame.get_text()
    
    def set_current_file(self, file: File):
        self.editor_frame.load_file(file)
        
    def __on_editor_focus(self, event, *a, **k):
        self.editor_frame = event.widget.master

# Create the main window and run the application
if __name__ == "__main__":#
    root = tk.Tk()
    app = QuasarEditor(root)
    root.mainloop()

