
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Select a file ")
    return file_path

def open_dir():
    dir_path = filedialog.askdirectory(title="Select a directory")
    return dir_path