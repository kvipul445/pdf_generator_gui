from __future__ import absolute_import
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
from functions.pdf_generator import pdf_process

root = tk.Tk()

def selected_files(name):
    print(name)
    return name

def name_of_pdf():
    global pdf_name
    pdf_file_label = tk.Label(main_frame,text='Enter the file name')
    pdf_file_label.grid(row=4,column=0)

    pdf_name = tk.Entry(main_frame)
    pdf_name.grid(row=4,column=1,columnspan=2, sticky="ew")

    pdf_label = tk.Label(main_frame,text=".pdf")
    pdf_label.grid(row=4,column=3)

def show_images():
    for file_path in files_open:
        image_file = ImageTk.PhotoImage(Image.open(file_path).resize((100,100)))
        image_label = tk.Label(main_frame,image=image_file)
        image_label.image = image_file
        image_label.grid(row=1,column=files_open.index(file_path))

def file_chooser(event):
    global files_open
    files_open = filedialog.askopenfilenames()
    selected_files(files_open)
    show_images()

def directory_chooser(event):
    global dir_open
    dir_open = filedialog.askdirectory()
    selected_files(dir_open)
    name_of_pdf()
    create_pdf_button()

def pdf_generate(event):
    pdf_class = pdf_process()
    pdf_class.selected_directory(dir_open,pdf_name.get(),files_open)
    successful_label = tk.Label(bottom_frame,text='Successfully Generated')
    successful_label.grid()

def create_pdf_button():
    next_button = tk.Button(bottom_frame,text='Create PDF')
    next_button.bind('<Button-1>',pdf_generate)
    next_button.grid(row=0,column=0,pady=5)
        
root.title('PDF Generator using Python3')
root.geometry('500x400')
root.resizable(width=True, height=True)

top_frame= tk.Frame(root)
top_frame.grid()

main_label = tk.Label(top_frame, text='PDF File Generator')
main_label.grid(pady=10,sticky=tk.NSEW)

main_frame= tk.Frame(root)
main_frame.grid(pady=5)

choose_file_button = tk.Button(main_frame, text='Choose File')
choose_file_button.bind('<Button-1>',file_chooser)
choose_file_button.grid()

choose_dir_button = tk.Button(main_frame, text='Choose Directory to save PDF')
choose_dir_button.bind('<Button-1>',directory_chooser)
choose_dir_button.grid(row=3)

bottom_frame = tk.Frame(root)
bottom_frame.grid(pady=5)

quit_button = tk.Button(bottom_frame, text='Quit', command=main_frame.quit)
quit_button.grid(row=0,column=1,pady=5)

root.mainloop()