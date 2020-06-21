from tkinter import filedialog

class open_file:
    
    def __init__(self):
        self.open_dialog = filedialog.askopenfilenames()
        self.return_file_path(self.open_dialog)

    def return_file_path(self,file_names):
        return file_names

    