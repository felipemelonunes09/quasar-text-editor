import tkinter as tk
from tkinter import ttk
from typing import Callable

import config
from core.file_handlers import FileLoader
from core.file_objects import File
from core.frames.FileBar import FileBar
from core.highlight.Highlight import Highlight
from core.highlight.Syntax import Syntax
from shared import utils
from shared import utils

class EditorFrame(tk.Frame):
    
    def __init__(self, parent, editor, on_focus_callback: Callable, *a, **k):
        tk.Frame.__init__(self, parent, *a, **k)
        self.editor = editor
        h_scrollbar = tk.Scrollbar(self, orient='horizontal')
        h_scrollbar.pack(side='bottom', fill='x')
        v_scrollbar = tk.Scrollbar(self, orient='vertical')
        v_scrollbar.pack(side='right', fill='y')
        self.text_widget = tk.Text(self, wrap='none', bg="#11212D", xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        self.text_widget.bind('<KeyRelease>', self.__on_file_edit)
        self.text_widget.pack(expand=1, fill='both', side='bottom')  
        self.file_bar = FileBar(self, bg="#06141B", height=30, callback=self.__on_file_tab_clicked)
        self.file_bar.pack(fill="x", side="top")
        self.text_widget.bind("<Button-1>", on_focus_callback)
        self.text_widget.pack(expand=1, fill='both', side='bottom')
        self.__current_file = None
        
    def get_current_file(self):
        return self.__current_file
    
    def set_current_file(self, file: File):
        self.__current_file = file
    
    def update(self) -> None:
        self.file_bar.forget()
        self.file_bar.pack(fill="x", side="top")
        self.file_bar.update()
        
    def show_editor(self, text):
        text = text
        self.text_widget.delete('1.0', 'end')
        self.text_widget.insert(tk.END, text)
        self.__highlight_keywords()
        self.update_idletasks()
        
    def load_file(self, file: File):
        self.file_bar.addItem(file)
        fileloader = FileLoader(file)
        self.show_editor(fileloader.load())
        self.set_current_file(file=file)
        
    def new_file(self):
        f = File(name="Unknow", path=None)
        self.file_bar.addItem(f)
        self.set_current_file(f)
        self.show_editor("")
    
    def get_text(self):
        if self.text_widget:
            return self.text_widget.get("1.0", tk.END)
    
    def __highlight_keywords(self):
        
        # this two line above can be removed to load the file syntax when the editor screen show, not when a key is pressed
        # would be interressing to allow other file extensions 
        syntax    = Syntax.map_file_extension(".qs")
        highlight = Highlight(syntax.get('syntax'), self.text_widget)
        highlight.apply_rule()
        
    def __on_file_edit(self, event=None):
        self.__highlight_keywords()
        self.get_current_file().set_edited(True)
        self.file_bar.update()
        
    def __on_file_tab_clicked(self, event, *a, **k):
        if event == None:
            self.show_editor("")
            self.set_current_file(None)
            return 
        self.load_file(event.widget.file)
        
    