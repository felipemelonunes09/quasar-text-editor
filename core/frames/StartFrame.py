import tkinter as tk
from tkinter import ttk

import config
from core.file_objects import File
from shared import utils

class StartFrame(tk.Frame):
    def __init__(self, parent, editor, *a, **k):
        tk.Frame.__init__(self, parent, *a, **k)
        self.editor = editor
        
        label_quasar        = tk.Label(self, text="<Quasar-Editor>", bg="#2f2f2f", font=("Helvetica", 25), fg="white")
        label_description   = tk.Label(self, text="Try opening a directorie or creating a new file :)", bg="#2f2f2f")
        
        button_open_file    = ttk.Button(self, text="Open File", command=self.__on_click_btn_open_file, style="Custom.TButton", compound=tk.LEFT)
        button_open_project = ttk.Button(self, text="Open Project", command=self.editor.load_dir, style="Custom.TButton", compound=tk.LEFT)
        button_new          = ttk.Button(self, text="New File", command=self.editor.new_file, style="Custom.TButton", compound=tk.LEFT)
        
        label_quasar.place(x=20, y=20)
        label_description.place(x=20, y=60)
        button_open_file.place(x=20, y=100)
        button_new.place(x=150, y=100)
        button_open_project.place(x=280, y=100)
        
        ## remote this and put into editor
    def __on_click_btn_open_file(self):
        path = utils.open_file()
        file = File(path=path, name=path.split("/")[-1])
        self.editor.load_file(file=file)
        