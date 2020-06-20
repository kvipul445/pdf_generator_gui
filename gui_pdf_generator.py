import tkinter as tk

root = tk.Tk()

root.title('PDF Generator using Python3')
main_frame= tk.Frame(root)
main_frame.grid()
main_label = tk.Label(main_frame, text='PDF File Generator')
main_label.grid()

bottom_frame = tk.Frame(root)
bottom_frame.grid()
next_button = tk.Button(main_frame,text='Next')
next_button.grid()
root.mainloop()