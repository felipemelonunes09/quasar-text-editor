import tkinter as tk
from tkinter.constants import *

from core.file_objects import File
from shared.widgets.FileListBox.FileListBoxWid import FileListboxWidget

class AttributesFrame(tk.Frame):
    def __init__(self, parent, editor, *args, **kwds):
        tk.Frame.__init__(self, parent, *args, **kwds)
        
        self.editor = editor        
    
    def show_tree(self, path):
        listbox = FileListboxWidget(master=self, path=path, callback=self.__on_tem_click, width=25, bd=0, bg=self.cget('background'))
        listbox.pack(fill="y", expand=True, pady=20, padx=10)
        listbox.update()
      
    def __on_tem_click(self, entity: File, event, *a, **k):
        self.editor.load_file(file=entity)