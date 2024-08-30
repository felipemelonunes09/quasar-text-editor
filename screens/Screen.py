import tkinter as tk
import config

from shared import utils

class Screen():
    
    def __init__(self, root, bg, width=400, height=300) -> None:
        
        self.root = root
        self.screen = tk.Frame(self.root, width=width, height=height, bg=bg)
    
    def clear_screen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()

    def set_visible(self, *args, **kwd):
        self.screen.pack(*args, **kwd)
        
    def set_invisible(self):
        self.screen.forget()