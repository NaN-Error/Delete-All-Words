import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileDeleterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Deleter")
        
        self.select_folder_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Word Documents", state=tk.DISABLED, command=self.delete_docs)
        self.delete_button.pack(pady=10)

        self.selected_folder = None

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.delete_button['state'] = tk.NORMAL

    def delete_docs(self):
        if self.selected_folder:
            for root, dirs, files in os.walk(self.selected_folder):
                for file in files:
                    if file.endswith(".docx"):
                        os.remove(os.path.join(root, file))
            messagebox.showinfo("Info", "Word documents deleted successfully.")
        else:
            messagebox.showwarning("Warning", "No folder selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDeleterApp(root)
    root.mainloop()
