import tkinter as tk
from tkinter import ttk

def configure(root):
    style = ttk.Style(root)
    style.theme_use('default') 

    style.configure("Custom.TButton", background="#253745", foreground="white", borderwidth=0, relief="flat", padding=(25, 40))
    style.map("Custom.TButton", 
              background=[('active', '#4A5C6A')],
              relief=[('active', 'solid')],
              borderwidth=[('active', 2)],
              highlightbackground=[('active', 'blue')]
            )  
    
    style.configure("TScrollbar", gripcount=0, background="#5a5a5a", darkcolor="#5a5a5a",lightcolor="#5a5a5a", troughcolor="#2e2e2e",    bordercolor="#2e2e2e", arrowcolor="#f0f0f0")
    style.map("TScrollbar", background=[('active', '#8a8a8a'),   ('!active', '#5a5a5a')],  lightcolor=[('!active', '#5a5a5a')],darkcolor=[('!active', '#5a5a5a')])
    
    