import tkinter as tk
import functions.open_file_function as fun

root = tk.Tk()

root.title('PDF Generator using Python3')
main_frame= tk.Frame(root)
main_frame.grid()
main_label = tk.Label(main_frame, text='PDF File Generator')
main_label.grid()

choose_file_button = tk.Button(main_frame, text='Choose File')
choose_file_button.bind('<Button-1>',fun.open_file.open_file_dialog)
choose_file_button.grid()

bottom_frame = tk.Frame(root)
bottom_frame.grid()
next_button = tk.Button(bottom_frame,text='Next')
next_button.grid(sticky=tk.E)

quit_button = tk.Button(bottom_frame, text='Quit', command=main_frame.quit)
quit_button.grid(sticky=tk.S)
root.mainloop()