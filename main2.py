import tkinter as tk

class TwoScreenEditor:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title("QuasarEditor")

        # Create the two frames with different background colors
        self.edit_frame = tk.Frame(self.root, width=400, height=300, bg="lightcoral")
        self.attribute_frame = tk.Frame(self.root, width=200, height=300, bg="lightseagreen")

        # Use pack to place the frames side by side
        self.edit_frame.pack(side="right", fill="both", expand=True)
        self.attribute_frame.pack(side="left", fill="both", expand=True)


        # Add widgets to the attribute frame
        self.attribute_label = tk.Label(self.attribute_frame, text="Attributes", font=("Arial", 14), bg="lightseagreen", fg="white")
        self.attribute_label.pack(pady=10)
        
        # Create a horizontal scrollbar
        h_scrollbar = tk.Scrollbar(self.edit_frame, orient='horizontal')
        h_scrollbar.pack(side='bottom', fill='x')
        
         # Create the text widget with no word wrapping
        self.text_widget = tk.Text(self.edit_frame, wrap='none', xscrollcommand=h_scrollbar.set)
        self.text_widget.pack(expand=1, fill='both')
        
        self.text_widget.bind('<KeyRelease>', self.highlight_keywords)
        
    def highlight_keywords(self, event=None):
        # Clear previous highlights
        self.text_widget.tag_remove('highlight_var', '1.0', tk.END)
        self.text_widget.tag_remove('highlight_string', '1.0', tk.END)

        # Highlight '-var' in blue
        self.highlight_word('-var', 'highlight_var', 'blue')

        # Highlight 'string' in green
        self.highlight_word('string', 'highlight_string', 'green')
        
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


# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TwoScreenEditor(root)
    root.mainloop()
