import tkinter as tk
from tkinter import ttk

import config
from core.file_objects import File
from shared import utils
from PIL import Image, ImageTk


class StartFrame(tk.Frame):
    def __init__(self, parent, editor, *a, **k):
        tk.Frame.__init__(self, parent, *a, **k)
        
        img_rocket  = ImageTk.PhotoImage(Image.open(config.ROCKET_ICON_PATH).resize((30, 30)))
        img_rule    = ImageTk.PhotoImage(Image.open(config.RULER_ICON_PATH).resize((30, 30)))      
        img_folder  = ImageTk.PhotoImage(Image.open(config.FOLDER_ICON_PATH).resize((30, 30)))     
        
        self.editor = editor
        
        label_quasar        = tk.Label(self, text="<Quasar-Editor>", bg="#06141B", font=("Helvetica", 25), fg="#9BA8AB")
        label_description   = tk.Label(self, text="Try opening a directorie or creating a new file :)", bg="#06141B", fg="#4A5C6A")
        
        button_open_file    = ttk.Button(self, image=img_rocket, text="\nOpen File", command=self.__on_click_btn_open_file, style="Custom.TButton", compound=tk.TOP)
        button_open_project = ttk.Button(self, image=img_folder, text="\nOpen Project", command=self.editor.load_dir, style="Custom.TButton", compound=tk.TOP)
        button_new          = ttk.Button(self, image=img_rule, text="\nNew File", command=self.editor.new_file, style="Custom.TButton", compound=tk.TOP)
        
        button_open_file.image      = img_rocket
        button_open_project.image   = img_folder
        button_new.image            = img_rule
        
        label_quasar.place(x=20, y=20)
        label_description.place(x=20, y=60)
        
        button_open_file.place(x=20, y=100)
        button_new.place(x=165, y=100)
        button_open_project.place(x=310, y=100)
        
        ## remote this and put into editor
    def __on_click_btn_open_file(self):
        path = utils.open_file()
        file = File(path=path, name=path.split("/")[-1])
        self.editor.load_file(file=file)
        