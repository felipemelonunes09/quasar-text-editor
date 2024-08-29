
import tkinter as tk
import config

from screens.Screen import Screen
from shared import utils

class EditorScreen(Screen):
    
    def __init__(self, root, editor) -> None:
        
        super().__init__(root, bg=config.EDITOR_BACKGROUND_COLOR)
        self.screen.pack(side="right", fill="both", expand=True)
        self.editor = editor
        
    def show_default(self):
        
        self.clear_screen()
        
        label_quasar        = tk.Label(self.screen, text="QuasarEditor", bg = config.EDITOR_BACKGROUND_COLOR, font=("Helvetica", 25), fg="white")
        label_description   = tk.Label(self.screen, text="Try opening a directorie or creating a new file :)", bg=config.EDITOR_BACKGROUND_COLOR)
        button_open_file    = tk.Button(self.screen, text="Open File", height=2, command=self.editor.load_file)
        button_open_project = tk.Button(self.screen, text="Open Project", height=2, command=self.editor.load_dir)
        button_new          = tk.Button(self.screen, text="New File", height=2, command=self.editor.new_file)
        
        label_quasar.place(x=20, y=20)
        label_description.place(x=20, y=60)
        button_open_file.place(x=20, y=100)
        button_new.place(x=150, y=100)
        button_open_project.place(x=280, y=100)
        
    def show_editor(self, text):
        
        self.clear_screen()
        
        # Create a horizontal scrollbar
        h_scrollbar = tk.Scrollbar(self.screen, orient='horizontal')
        h_scrollbar.pack(side='bottom', fill='x')
        
        # Create the text widget with no word wrapping
        self.text_widget = tk.Text(self.screen, wrap='none', xscrollcommand=h_scrollbar.set)
        self.text_widget.pack(expand=1, fill='both')
        self.text_widget.insert(tk.END, text)
        self.text_widget.bind('<KeyRelease>', self.highlight_keywords)
        self.highlight_keywords()
        
        
    def highlight_keywords(self, event=None):
        # Clear previous highlights
        self.text_widget.tag_remove('highlight_var', '1.0', tk.END)
        self.text_widget.tag_remove('highlight_string', '1.0', tk.END)
        self.text_widget.tag_remove('highlight_number', '1.0', tk.END)

        # Highlight '-var' in blue
        self.highlight_word('-var', 'highlight_var', 'blue')

        # Highlight 'string' in green
        self.highlight_word('string', 'highlight_string', 'green')
        
        # Highlight 'number' in green
        self.highlight_word('number', 'highlight_string', 'green')
        
    def highlight_word(self, word, tag, color):
        start_pos = '1.0'
        while True:
            start_pos = self.text_widget.search(word, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(word)}c"
            
            self.text_widget.tag_add(tag, start_pos, end_pos)
            self.text_widget.tag_config(tag, foreground=color)
            start_pos = end_pos
            
    def get_text(self):
        if self.text_widget:
            return self.text_widget.get("1.0", tk.END)