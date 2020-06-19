from tkinter import *

root = Tk()

main_frame= Frame(root, width=200, height=200)
main_frame.pack()
main_label = Label(main_frame, text='PDF File Generator')
main_label.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)
next_button = Button(main_frame,text='Next')
next_button.pack()
root.mainloop()