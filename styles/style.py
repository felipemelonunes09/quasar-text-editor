import tkinter as tk
from tkinter import ttk

def configure(root):
    # Set the desired theme (optional, depending on your environment)
    style = ttk.Style(root)
    style.theme_use('default')  # You can experiment with different themes like 'clam', 'alt', etc.

    # Configure the style with a specific name
    style.configure("Custom.TButton", background="#4681f4", foreground="white", borderwidth=0, relief="flat", padding=(5, 5))
    style.map("Custom.TButton", background=[('active', '#4681f4')])  # Change on active

#root = tk.Tk()

# Load the image and resize it using subsample
#icon = tk.PhotoImage(file="file_plus.png") # Adjust the subsample values to resize

# Set the desired theme (optional, depending on your environment)
#style = ttk.Style(root)
#style.theme_use('default')  # You can experiment with different themes like 'clam', 'alt', etc.

# Configure the style with a specific name
#style.configure("Custom.TButton", background="#4681f4", foreground="white", borderwidth=0, relief="flat", padding=(5, 5))
#style.map("Custom.TButton", background=[('active', '#4681f4')])  # Change on active

# Apply the custom style to the button with an icon
#button = ttk.Button(root, text="Open File", image=icon, compound=tk.LEFT, style="Custom.TButton")
#button.place(x=20, y=20)

#root.mainloop()