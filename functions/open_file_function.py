from tkinter import filedialog

class open_file:
    
    def open_file_dialog(self):
        open_dialog = filedialog.askopenfilenames()
        return open_dialog

    