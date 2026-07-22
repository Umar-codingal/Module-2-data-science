from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title("Denomination Calculator")
root.configure(bg="lightblue")
root.geometry("650x400")

upload= Image.open("den-money.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image,bg="lightblue")
label.place(x=180, y=20)

label1=Label(root, text="Denomination Calculator", font=("Arial", 20), bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do u want to continue?")
    if MsgBox == 'ok':
        topwin()

button1=Button(root,
               text="Click Here", font=("Arial", 15), bg="brown", fg="white" )
button1.place(x=260,y=360)


def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    
    label = Label(top, text="Enter the amount", font=("Arial", 15), bg="light grey")
    entry= Entry(top)
    lbl= Label(top,text="Here are number of nates for each denomination", font=("Arial", 15), bg="light grey")

    l1=Label(top, text="2000",bg = "light grey")
    l2=Label(top, text="500",bg = "light grey")
    l3=Label(top, text="200",bg = "light grey")

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculate():
        try:
            global amount
            amount = int(entry.get())
            notes_2000 = amount // 2000
            amount %= 2000
            notes_500 = amount // 500
            amount %= 500
            notes_200 = amount // 200

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)


            t1.insert(END, str(notes_2000))
            t2.insert(END, str(notes_500))    
            t3.insert (END, str(notes_200))  
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")


        btn = Button(top, text="Calculate", font=("Arial", 15), bg="brown", fg="white", command=calculate)

        label.place(x=230, y=50)  
        entry.place(x=200, y=80)
        btn.place(x=240, y=120)
        lbl.place(x=140, y=170)

        l1.place(x=180, y=200)
        l2.place(x=180, y=230)
        l3.place(x=180,y=260)

        t1.place(x=270, y=200)
        t2.place(x=270, y=230)
        t3.place(x=270,y=260)

        top.mainloop()

root.mainloop()
