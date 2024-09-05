import config
import json

class Syntax():
    
    @staticmethod
    def map_file_extension(extension: str) -> dict:
        filename = config.MAP_EXTENSION_FILE[extension]
        fullpath = f'{config.HIGHLIGHT_PATH}/{filename}'
        
        with open(fullpath) as file:
            data = json.load(file)
        
        return data
        