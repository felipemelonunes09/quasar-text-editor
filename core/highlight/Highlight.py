import re
from core.file_objects import File
import tkinter as tk

class Highlight():
    
    def __init__(self, syntax: list[dict], text_widget: tk.Text) -> None:
        self.__syntax_rules = syntax
        self.__text_widget = text_widget
        
    def apply_rule(self) -> None:
        for rule in self.__syntax_rules:
            
            _rule       = rule.get("rule")
            name        = rule.get("id")
            color       = rule.get("color")
            is_regex     = rule.get("is-regex", False) 
            
            tag = f'highlight_{name}'
            
            self.__text_widget.tag_remove(tag, '1.0', tk.END)
            self.highlight_by_regex(_rule, tag, color) if is_regex else self.highlight_word(_rule, tag, color)
    
    def highlight_word(self, rule, tag, color):
            start_pos = '1.0'
            while True:
                start_pos = self.__text_widget.search(rule, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                
                end_pos = f"{start_pos}+{len(rule)}c"
                self.__text_widget.tag_add(tag, start_pos, end_pos)
                self.__text_widget.tag_config(tag, foreground=color)
                start_pos = end_pos
                
    def highlight_by_regex(self, rule, tag, color):
        text = self.__text_widget.get('1.0', tk.END)
        
        for match in re.finditer(rule, text):
            start_pos = f"1.0+{match.start()}c"
            end_pos = f"1.0+{match.end()}c"
            
            self.__text_widget.tag_add(tag, start_pos, end_pos)
            self.__text_widget.tag_config(tag, foreground=color)