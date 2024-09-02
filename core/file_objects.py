
import os
from typing import Any

class FileObject():
    
    def __init__(self, name, path) -> None:
        self.__name = name
        self.__path = path
        
    def get_name(self) -> str:
        return self.__name
    
    def get_path(self) -> str:
        return self.__path

class Dir(FileObject):
    def __init__(self, name, path) -> None:
        
        super().__init__(name, path)
        
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
        path = self.get_path()
        
        for item in os.listdir(path):
            fullpath = os.path.join(path, item)
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
        
class File(FileObject):
    def __init__(self, name, path) -> Any:
        super().__init__(name, path)
    