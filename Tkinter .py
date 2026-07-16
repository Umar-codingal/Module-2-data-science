from tkinter import *

window=Tk()
window.title("my profile card")
window.geometry("400x380")

title = Label(window, text="My Profile Card" , fg = 'white', bg='purple', width=40)
title.grid(row=0 , column = 0, columnspan=2, padx=10,pady=10)

name_label = Label(window, text= 'Name:' , fg = 'black', bg = 'white')
n