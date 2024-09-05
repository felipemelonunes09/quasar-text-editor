import tkinter as tk
from tkinter import ttk

def configure(root):
    style = ttk.Style(root)
    style.theme_use('default') 

    style.configure("Custom.TButton", background="#4681f4", foreground="white", borderwidth=0, relief="flat", padding=(5, 5))
    style.map("Custom.TButton", background=[('active', '#4681f4')])  