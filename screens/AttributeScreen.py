import tkinter as tk
import config
import os

from screens.Screen import Screen

class AttributeScreen(Screen):
    def __init__(self, root, editor):
        
        super().__init__(root, bg=editor.get_pallete().primary, width=200)
        self.editor = editor
        self.show_fileeplorer_label()
        
    def set_visible(self):
        return super().set_visible(side="left", fill="both", expand=False)
       
    def show_fileeplorer_label(self):
        self.attribute_label = tk.Label(self.screen, text="Explorer", bg=self.editor.get_pallete().primary, font=("Arial", 14), fg="white")
        self.attribute_label.place(x=15, y=10)      
        
    def show_dirtree(self, path):
        
        self.clear_screen()    
        self.show_fileeplorer_label()
    
        objects = os.listdir(path)
        filename = path.split("/")
        
        listbox = tk.Listbox(self.screen, height=self.screen.winfo_height(), width=self.screen.winfo_width(), bg=self.editor.get_pallete().primary, bd=0)
        dirname = tk.Label(self.screen, text=filename[-2], bg=self.editor.get_pallete().primary, font=('Arial', 14, 'bold'))
        
        dirname.place(x=15, y=40)
        listbox.place(x=0, y=65)
        
        for item in objects: 
            
            full_path = f"{path}/{item}"
            if os.path.isdir(full_path):
                listbox.insert(tk.END, "\t> "+item)
            else:
                listbox.insert(tk.END, "\t"+item)
                
            
        listbox.update_idletasks()
        dirname.update_idletasks()
        
