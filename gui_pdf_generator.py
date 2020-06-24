import tkinter as tk
from tkinter import filedialog
import functions

root = tk.Tk()

def selected_files(name):
    print(name)
    return name

def name_of_pdf():
    global pdf_name
    name_frame = tk.Frame(root)
    name_frame.grid()
    pdf_name = tk.Entry(name_frame)
    pdf_name.grid(columnspan=2)

def file_chooser(event):
    global files_open
    files_open = filedialog.askopenfilenames()
    selected_files(files_open)

def directory_chooser(event):
    global dir_open
    dir_open = filedialog.askdirectory()
    selected_files(dir_open)
    name_of_pdf

def pdf_generator(dir_open,files_open,pdf_name):
    pdf_class = functions.pdf_generator.pdf_process()
    pdf_class.selected_directory(dir_open,pdf_name,files_open)
    successful_label = tk.Label(bottom_frame,text='Successfully Generated')
    successful_label.grid()
        
root.title('PDF Generator using Python3')
main_frame= tk.Frame(root)
main_frame.grid()
main_label = tk.Label(main_frame, text='PDF File Generator')
main_label.grid()

choose_file_button = tk.Button(main_frame, text='Choose File')
choose_file_button.bind('<Button-1>',file_chooser)
choose_file_button.grid()

choose_dir_button = tk.Button(main_frame, text='Choose Directory to save PDF')
choose_dir_button.bind('<Button-1>',directory_chooser)
choose_dir_button.grid()

bottom_frame = tk.Frame(root)
bottom_frame.grid()
next_button = tk.Button(bottom_frame,text='Next')
next_button.grid(sticky=tk.E)

quit_button = tk.Button(bottom_frame, text='Quit', command=main_frame.quit)
quit_button.grid(sticky=tk.S)
root.mainloop()