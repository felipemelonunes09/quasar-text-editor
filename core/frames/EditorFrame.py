import tkinter as tk
from tkinter import ttk

import config
from core.file_objects import File
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
        self.text_widget.pack(expand=1, fill='both')
        self.text_widget.bind('<KeyRelease>', self.highlight_keywords)
        

    def show_editor(self, text):
        self.text_widget.delete('1.0', 'end')
        self.text_widget.insert(tk.END, text)
        self.highlight_keywords()
        
    
    def highlight_keywords(self, event=None):
        
        # this two line above can be removed to load the file syntax when the editor screen show, not when a key is pressed
        syntax    = Syntax.map_file_extension(".qs")
        highlight = Highlight(syntax.get('syntax'), self.text_widget)
        highlight.apply_rule()
        
    def get_text(self):
        if self.text_widget:
            return self.text_widget.get("1.0", tk.END)