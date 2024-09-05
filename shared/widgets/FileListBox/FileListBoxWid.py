import tkinter as tk
import os

from tkinter import ttk
from typing import Callable, Union
from core.file_objects import Dir, File

class FileListboxWidget(tk.Listbox):
    
    def __init__(self, master, path: str, callback: Callable[[File, Dir], object], *args, **kwd):
        
        tk.Listbox.__init__(self, master, *args, **kwd)
        self.callback=callback
        self.entities = [Dir(path=path, name=path.split("/")[-1])]
        
        ## Scrols
        v_scroll = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.yview, style="TScrollbar")
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        h_scroll = ttk.Scrollbar(master, orient=tk.HORIZONTAL, command=self.xview, style="TScrollbar")
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X) 
        
        self.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        self.bind("<<ListboxSelect>>", self.__on_item_click)
        
    
    def update(self):
        super().update()
        self.delete(0, tk.END)
        for entity in self.entities:
            name = entity.get_name()
            
            if isinstance(entity, File):
                self.insert(tk.END, name)
            else:
                self.insert(tk.END, name + "/")
                if not entity.is_closed():
                    self.__insert_subitem_recursive(entity.get_entities(), offset="\t")
                        
    def __insert_subitem_recursive(self, entities: list[Union[Dir, File]], offset="\t"):
        for entity in entities:
            display_name = f"{offset}{entity.get_name()}"
            if isinstance(entity, File):
                self.insert(tk.END, display_name)
            else:
                self.insert(tk.END, display_name + "/")
                if not entity.is_closed():        
                    self.__insert_subitem_recursive(entity.get_entities(), offset=f"\t{offset}")
                        
    def __on_item_click(self, event, *a, **k):
        selection = self.curselection()
        if selection:
            index = selection[0]
            items = self.__get_all_open_items(self.entities)
            entity = items[index]
                
            if isinstance(entity, Dir):
                entity.toggle_open()
                self.update()    
            else:
                self.callback(entity, event)

            

    def __get_all_open_items(self, entities: Union[File, Dir]):
        items = []
        
        for entity in self.entities:
            if isinstance(entity, File):
                items.append(entity)
            if isinstance(entity, Dir):
                items.extend(entity.getOpenItems())
        return items