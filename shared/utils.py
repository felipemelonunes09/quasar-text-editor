
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Select a file ")
    return file_path

def open_dir():
    dir_path = filedialog.askdirectory(title="Select a directory")
    return dir_path

def open_save_file():
    file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",  
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")], 
            initialfile="your_file.txt",  
            title="Save your file" 
        )
    
    return file_path