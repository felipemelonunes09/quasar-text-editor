from typing import Any

import os

class Dir():
    def __init__(self, name, path) -> Any:
        
        self.name       = name
        self.path       = path
        
        self.open       = False
        
        self.entities   = self.__get_entities()    
    
    def toggle_open(self):
        self.open = not self.open
        
    def is_closed(self):
        return self.open == False
    
    def get_entities(self):
        return self.entities
    
    def __get_entities(self):
        self.entities = []
        for item in os.listdir(self.path):
            fullpath = os.path.join(self.path, item)
            self.entities.append(
                Dir(path=os.path.join(fullpath), name=item) if os.path.isdir(fullpath) else File(path=fullpath, name=item)
            )
        return self.entities
    
    def getOpenItems(self):
        items = [self]
            
        if not self.is_closed():
            for entity in self.get_entities():
                if isinstance(entity, File):
                    items.append(entity)
                if isinstance(entity, Dir):
                    items.extend(entity.getOpenItems())
        return items
        
class File():
    
    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path 
    