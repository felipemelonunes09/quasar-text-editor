import tkinter as tk
import config
import os

from screens.Screen import Screen
from shared.widgets.FileListBox.FileListBoxWid import FileListBoxWid

class AttributeScreen(Screen):
    def __init__(self, root, editor):
        
        super().__init__(root, bg=editor.get_pallete().primary, width=200)
        
        self.editor = editor
        self.item_data = dict()
        self.listbox = None
        
    def set_visible(self):
        return super().set_visible(side="left", fill="both", expand=False)
       
    def show_fileeplorer_label(self):
        self.attribute_label = tk.Label(self.screen, text="Explorer", bg=self.editor.get_pallete().primary, font=("Arial", 14), fg="white")
        self.attribute_label.place(x=15, y=10)      
        
    def show_dirtree(self, path):
        
        self.set_visible()
        self.clear_screen()    
        self.show_fileeplorer_label()
    
        
        listbox = FileListBoxWid(path=path, callback=self.__on_item_click, master=self.screen, height=self.height, width=self.width, bg=self.editor.get_pallete().primary, bd=0)
        listbox.place(x=20, y=50)
        listbox.update()
        
    
    def __on_item_click(self, entity, event, *a, **k):
        print("File")
