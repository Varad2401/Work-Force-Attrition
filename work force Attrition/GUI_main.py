import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Work force attrition system")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('A.jpg')
image2 = image2.resize((1200,750))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=20, y=60)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Work force attrition system",font=("Times New Roman", 30, 'bold'),
                    background="#152238", fg="white", width=70, height=1)
label_l1.place(x=0, y=0)



################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
frame_alpr = tk.LabelFrame(root, text="  ", width=470, height=770, bd=5, font=('times', 14, ' bold '),bg="black")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=1100, y=50)



def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=1200, y=260)

button2 = tk.Button(root, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=1200, y=340)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="brown", fg="white")
button3.place(x=1200, y=430)

root.mainloop()