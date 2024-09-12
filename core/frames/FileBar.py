import tkinter as tk
from typing import Callable
from core.file_objects import File
from PIL import Image, ImageTk
import config

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
    
    def __close_tab(self, event, *a, **k):
        try:
            file = event.widget.file
            self.__items.remove(file)
            event.widget.file = next(iter(self.__items))
            self.callback(event)
        except:
            self.callback(None)
        finally:
            self.update()
    
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
            
            item_name = item.get_name()
            item_name = f"* {item_name}" if item.get_edited() else item_name
                        
            label = tk.Label(frame, text=item_name, font=("Arial", 14), bg="#06141B")
            buttom = tk.Label(frame, text="X", font=("Arial", 11), bg="#06141B", fg="#4A5C6A")
            
            label.pack(fill="x", side="left", padx=30, pady=5)
            buttom.pack(side="right", padx=10)
            
            frame.pack(fill="y", side="left")
            setattr(frame, "file", item)
            setattr(buttom, "file", item)

            self.__widgets.append(frame)
                        
            # Bind events to change color on hover
            frame.bind("<Enter>", lambda e, f=frame: f.config(highlightbackground="#4A5C6A"))  # Change to a lighter color on hover
            frame.bind("<Leave>", lambda e, f=frame: f.config(highlightbackground="#253745"))  # Change back to original color when cursor leaves
            frame.bind("<Button-1>", self.callback)
            buttom.bind("<Button-1>", self.__close_tab)
