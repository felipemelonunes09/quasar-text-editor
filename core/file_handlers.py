
from core.file_objects import File

class FileLoader():
    
    def __init__(self, file: File) -> None:
        self.__file = file

    def load(self) -> str:
        with open(self.__file.get_path(), 'r') as file:
            return file.read()
        
class FileWriter():
    
    def __init__(self, file: File, content: str) -> None:
        
        self.__file = file
        self.__content = content
        
    def write(self, file: File):
        with open(self.__file.get_path(), 'w') as file:
            file.write(self.__content)
            
            