import tkinter as tk

class Menu():
    
    def __init__(self, root, editor) -> None:
        self.root = root
        self.editor = editor
        
    def on_save(self):
        
        path, _, _ = self.editor.get_context()
        content = self.editor.get_content()
        
        with open(path, 'w') as file:
            file.write(content)
    
    def create(self) -> None:
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.on_save)