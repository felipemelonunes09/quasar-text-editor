import tkinter as tk
import config
import os

from screens.Screen import Screen

class AttributeScreen(Screen):
    def __init__(self, root):
        
        super().__init__(root, bg=config.ATTRIBUTE_BACKGROUND_COLOR, width=200)
        self.screen.pack(side="left", fill="both", expand=False)
        
        self.show_fileeplorer_label()
       
    def show_fileeplorer_label(self):
        self.attribute_label = tk.Label(self.screen, text="Explorer", bg=config.ATTRIBUTE_BACKGROUND_COLOR, font=("Arial", 14), fg="white")
        self.attribute_label.place(x=15, y=10)      
        
    def show_filetree(self, path):
        
        self.clear_screen()
        self.show_fileeplorer_label()
        
        filename = path.split("/")
        
        listbox = tk.Listbox(self.screen, height=self.screen.winfo_height(), width=self.screen.winfo_width(), bg=config.ATTRIBUTE_BACKGROUND_COLOR, bd=0)
        dirname = tk.Label(self.screen, text=filename[-2], bg=config.ATTRIBUTE_BACKGROUND_COLOR, font=('Arial', 14, 'bold'))
        
        
        dirname.place(x=15, y=40)
        listbox.place(x=0, y=65)
        
        listbox.insert(tk.END, "\t"+filename[-1])

    def show_dirtree(self, path):
        
        self.clear_screen()
        
        objects = os.listdir(path)
        self.show_fileeplorer_label()
        
        filename = path.split("/")
        
        listbox = tk.Listbox(self.screen, height=self.screen.winfo_height(), width=self.screen.winfo_width(), bg=config.ATTRIBUTE_BACKGROUND_COLOR, bd=0)
        dirname = tk.Label(self.screen, text=filename[-2], bg=config.ATTRIBUTE_BACKGROUND_COLOR, font=('Arial', 14, 'bold'))
        
        
        dirname.place(x=15, y=40)
        listbox.place(x=0, y=65)
        
        for item in objects: 
            listbox.insert(tk.END, "\t"+item)
            
        listbox.update_idletasks()
        dirname.update_idletasks()