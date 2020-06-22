import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

def file_chooser(event):
    global files_open
    files_open = filedialog.askopenfilenames()
    print(files_open)
    selected_files()

def selected_files():
    print(files_open)
    return files_open

root.title('PDF Generator using Python3')
main_frame= tk.Frame(root)
main_frame.grid()
main_label = tk.Label(main_frame, text='PDF File Generator')
main_label.grid()

choose_file_button = tk.Button(main_frame, text='Choose File')
choose_file_button.bind('<Button-1>',file_chooser)
choose_file_button.grid()

bottom_frame = tk.Frame(root)
bottom_frame.grid()
next_button = tk.Button(bottom_frame,text='Next')
next_button.grid(sticky=tk.E)

quit_button = tk.Button(bottom_frame, text='Quit', command=main_frame.quit)
quit_button.grid(sticky=tk.S)
root.mainloop()