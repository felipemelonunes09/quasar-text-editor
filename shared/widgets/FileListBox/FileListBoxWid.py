import tkinter as tk
import os

from typing import Callable, Union
from core.file_objects import Dir, File

class FileListBoxWid():
    
    def __init__(self, path: str, callback: Callable[[Union[File, Dir], object], None], *args, **kwds) -> None:
        
        self.listbox = tk.Listbox(*args, **kwds, )
        self.listbox.bind("<<ListboxSelect>>", self.__on_item_click)
        self.callback = callback
        
        self.entities = [Dir(path=path, name=path.split("/")[-1])]
        
        #for item in os.listdir(path):
        #    fullpath = os.path.join(self.path, item)
        #    self.entities.append( Dir(path=path, name=item) if os.path.isdir(fullpath) else File(path=path, name=item))

    def place(self, x, y):
        self.listbox.place(x=x, y=y)

    def update(self):
        # fix this, and att deletion just from the item clicked
        self.listbox.delete(0, tk.END)
        for entity in self.entities:
            name = entity.get_name()
            if isinstance(entity, File):
                self.listbox.insert(tk.END, name)
            else:
                self.listbox.insert(tk.END, name + "/")
                if not entity.is_closed():
                    self.__insert_subitem_recursive(entity.get_entities())
                    
        
    def __insert_subitem_recursive(self, entities: list[Union[Dir, File]], offset="\t"):
        
        for entity in entities:
            display_name = f"{offset}{entity.get_name()}"
            if isinstance(entity, File):
                self.listbox.insert(tk.END, display_name)
            else:
                self.listbox.insert(tk.END, display_name + "/")
                if not entity.is_closed():
                    self.__insert_subitem_recursive(entity.get_entities(), offset=f"\t{offset}")
    
    def __on_item_click(self, event, *a, **k):
        selection = self.listbox.curselection()
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
        
                
        
    