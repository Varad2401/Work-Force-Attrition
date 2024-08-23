
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import numpy as np
import time
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################++++++++++++++=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("MAIN PAGE")


#430
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


frame_alpr = tk.LabelFrame(root, width=1850, height=1850, bd=5, font=('times', 14, ' bold '),bg="#192841")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=0, y=0)

image2 =Image.open('o.jpg')
image2 =image2.resize((140,120))

background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(frame_alpr, image=background_image)

background_label.image = background_image

background_label.place(x=680, y=25)

lbl = tk.Label(frame_alpr, text="Work force attrition system", font=('Times New Roman', 35,' bold '),bg="black",fg="white")
lbl.place(x=450, y=180)

lbl = tk.Label(frame_alpr, text="Using Machine Learning", font=('Times New Roman', 35,' bold '),bg="black",fg="white")
lbl.place(x=530, y=250)

logo_label=tk.Label()
logo_label.place(x=300,y=55)


logo_label1=tk.Label(text='...To develop a system that capable \n To Predict Work force attrition system...',compound='bottom',font=("Times New Roman", 20, 'bold', 'italic'),width=35, bg="#cce6ff", fg="black")
#logo_label=tk.Label(height=500, width=400)
logo_label1.place(x=500,y=590)


def login():

    from subprocess import call
    call(["python", "GUI_main.py"])  
   



#################################################################################################################

   
def window():
    root.destroy()

button1 = tk.Button(frame_alpr, text=" START",command=login,width=15, height=1, font=('times', 15, ' bold '),bg="#3BB9FF",fg="black")
button1.place(x=650, y=450)

# button2 = tk.Button(frame_alpr, text="LOGIN",command=login,width=15, height=1, font=('times', 15, ' bold '),bg="#3BB9FF",fg="black")
# button2.place(x=200, y=450)

# button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=160)
#




root.mainloop()