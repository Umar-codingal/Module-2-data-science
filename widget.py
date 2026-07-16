from tkinter import *
from tkinter import messagebox  
from PIL import Image , ImageTk
window = Tk()
window.title("My Photo Album")
window.geometry("400x420")


title = Label(window, text='My photo album', fg='White', bg='purple', width=40)
title.pack(pady=10)
img_file = Image.open('image1.jpg')
img_file= img_file.resize((300, 300))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)

def show_message():
    messagebox.showinfo('Great!', 'You clicked the image!')
msg_btn = Button(window, text='Click to React', bg='blue', fg='white', command=show_message)
msg_btn.pack(pady=10)

def show_details():
    top = Toplevel(window)
    top.title("Photo Details")
    top.geometry("200x120")
    info = Label(top, text='Taken by my friend')
    info.pack(pady=10)
    place=Label(top, text='Edited by me')
    place.pack()
    top.mainloop()
details_btn = Button(window, text='Show Details', bg='green', fg='white', command=show_details)
details_btn.pack(pady=5)


window.mainloop()