import tkinter as tk
from typing import Callable

from core.file_objects import File

class FileBar(tk.Frame):
    
    __items:    set[File]        = set()
    __widgets:  list[tk.Frame]   = list()
    
    def __init__(self, parent, callback: Callable, *a, **k):
        self.callback = callback
        tk.Frame.__init__(self, parent, *a, **k)
        self.update()
        
    def addItem(self, file: File):
        self.__items.add(file)
        self.update()
        
    def __file_clicked(self, file: File):
        self.callback(file)
        
    def update(self):
        super().update()
        
        for wid in self.__widgets:
            wid.destroy()
        
        for item in self.__items:
        
            frame = tk.Frame(
                self,
                bg="#06141B",
                height=30, 
                width=40,
                borderwidth=1,
                relief="solid",
                highlightbackground="#253745",
                highlightthickness=1
            )
            
            
            frame.unbind("<Button-1>")
            label = tk.Label(frame, text=item.get_name(), font=("Arial", 14), bg="#06141B")
            label.pack(fill="x", padx=45, pady=5)
            
            frame.pack(fill="y", side="left")
            setattr(frame, "file", item)

            self.__widgets.append(frame)
            
            print(item.get_name())
            
            # Bind events to change color on hover
            frame.bind("<Enter>", lambda e, f=frame: f.config(highlightbackground="#4A5C6A"))  # Change to a lighter color on hover
            frame.bind("<Leave>", lambda e, f=frame: f.config(highlightbackground="#253745"))  # Change back to original color when cursor leaves
            frame.bind("<Button-1>", self.callback)
