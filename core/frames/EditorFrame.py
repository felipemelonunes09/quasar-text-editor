import tkinter as tk
from tkinter import ttk

import config
from core.file_handlers import FileLoader
from core.file_objects import File
from core.frames.FileBar import FileBar
from core.highlight.Highlight import Highlight
from core.highlight.Syntax import Syntax
from shared import utils
from shared import utils

class EditorFrame(tk.Frame):
    
    def __init__(self, parent, editor, *a, **k):
        tk.Frame.__init__(self, parent, *a, **k)
        self.editor = editor
                
        # Create a horizontal scrollbar
        h_scrollbar = tk.Scrollbar(self, orient='horizontal')
        h_scrollbar.pack(side='bottom', fill='x')
        
        # Create a vertical scrollbar
        v_scrollbar = tk.Scrollbar(self, orient='vertical')
        v_scrollbar.pack(side='right', fill='y')
        
        # Create the text widget with no word wrapping
        self.text_widget = tk.Text(self, wrap='none', bg="#11212D", xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        self.text_widget.bind('<KeyRelease>', self.__on_file_edit)
        
        self.file_bar = FileBar(self, bg="#06141B", height=30, callback=self.__on_file_tab_clicked)
        
        self.file_bar.pack(fill="x", side="top")
        self.text_widget.pack(expand=1, fill='both', side='bottom')
        
    def show_editor(self, text):
        self.text_widget.delete('1.0', 'end')
        self.text_widget.insert(tk.END, text)
        self.__highlight_keywords()
        
    def load_file(self, file: File):
        self.file_bar.addItem(file)
        fileloader = FileLoader(file)
        self.show_editor(fileloader.load())
    
    def __highlight_keywords(self):
        
        # this two line above can be removed to load the file syntax when the editor screen show, not when a key is pressed
        # would be interressing to allo other file extensions 
        syntax    = Syntax.map_file_extension(".qs")
        highlight = Highlight(syntax.get('syntax'), self.text_widget)
        highlight.apply_rule()
        
    def __on_file_edit(self, event=None):
        self.__highlight_keywords()
        self.editor.get_current_file().set_edited(True)
        self.file_bar.update()
        
    def get_text(self):
        if self.text_widget:
            return self.text_widget.get("1.0", tk.END)
        
    def __on_file_tab_clicked(self, event, *a, **k):
        if event == None:
            self.show_editor("")
            self.editor.set_current_file(None)
            return 
        
        self.editor.set_current_file(event.widget.file)
        self.load_file(event.widget.file)