from tkinter import *

import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

root = tk.Tk()

root.geometry("800x850+250+5")
root.title("Work force attrition system")
root.configure(background="deeppink4")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
        #####For background Image
image2 = Image.open('b1.jpg')
image2 = image2.resize((w, h))
    
background_image = ImageTk.PhotoImage(image2)
    
background_label = tk.Label(root, image=background_image)
    
background_label.image = background_image
    
background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
        
        
    
    
Age = tk.IntVar()
BusinessTravel = tk.StringVar()
Department = tk.StringVar()
Gender = tk.StringVar()
JobInvolvement = tk.IntVar()
JobLevel = tk.IntVar()
JobRole = tk.StringVar()    
JobSatisfaction = tk.IntVar()
MaritalStatus = tk.StringVar()
MonthlyIncome= tk.IntVar()
NumCompaniesWorked= tk.IntVar()
OverTime = tk.StringVar()
PercentSalaryHike = tk.IntVar()
PerformanceRating = tk.IntVar()
Modeofwork = tk.StringVar()
Jobmode = tk.StringVar()    
    #===================================================================================================================
def Detect():
        e1= Age.get()
        print(e1)
        
        e2=BusinessTravel.get()
        print(e2)
        if e2=="Travel_Rarely":
           e2=0
        elif e2=="Travel_Frequently":
           e2=1
        else:
           e2=2
       
        e3= Department.get()
        print(e3)
        if e3=="Research and Development":
           e3=0
        else:
           e3=1
           
        e4=Gender.get()
        print(e4)
        if e4=="Male":
           e4=0
        else:
           e4=1
           
        e5= JobInvolvement.get()
        print(e5)
        
        e6=JobLevel.get()
        print(e6)
        
        e7=JobRole.get()
        print(e7)
        if e7=="Laboratory Technician":
           e7=0
        elif e7=="Research Scientist":
           e7=1
        elif e7=="Research Director":
           e7=2  
        elif e7=="Sales Representative":
           e7=3 
        elif e7=="Manager":
           e7=4
        elif e7=="Manufacturing Director":
           e7=5 
        elif e7=="Sales Executive":
           e7=6
        elif e7=="Human Resource":
           e7=7
        else:
           e7=8
        
        e8=JobSatisfaction.get()
        print(e8)
        
        e9=MaritalStatus.get()
        print(e9)
        if e9=="Single":
           e9=0
        elif e9=="Married":
           e9=1
        else:
           e9=2
        
        e10=MonthlyIncome.get()
        print(e10)
        
        e11=NumCompaniesWorked.get()
        print(e11)
        
        e12=OverTime.get()
        print(e12)
        if e12=="No":
           e12=0
        else:
           e12=1
        
        e13= PercentSalaryHike.get()
        print(e13)
       
        e14= PerformanceRating.get()
        print(e14)
       
        e15=  Modeofwork.get()
        print(e15)
        if e15=="OFFICE":
           e15=0
        else:
           e15=1
      
        e16= Jobmode.get()
        print(e16)
        if e16=="Contract":
           e16=0
        elif e16=="Full time":
           e16=1
        else:
           e16=2
       
        #########################################################################################
        
        from joblib import dump , load
        a1=load('D:/Ravina data/work force Attrition/SVM_Prediction.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11,e12, e13, e14,e15, e16]])
        print(v)
        if v[0]==0:
            print("No")
            yes = tk.Label(root,text="Not Attrited",background="red",foreground="white",font=('times', 20, ' bold '),width=20,fg="white")
            yes.place(x=550,y=650)
        else:
             print("Yes")
             yes = tk.Label(root,text="Employee Has Attrited",background="red",foreground="white",font=('times', 20, ' bold '),width=20,fg="white")
             yes.place(x=550,y=650)        
        
            


l1=tk.Label(root,text="Age",background="#8B8989",font=('times', 20,' bold '),width=20,fg="white")
l1.place(x=100,y=50)
    #gender=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=gender)
    #gender.place(x=400,y=1)
Age=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Age)
Age.place(x=450,y=50)   


l2=tk.Label(root,text="BusinessTravel",background="#8B8989",font=('times', 20, ' bold '),width=20, fg="white")
l2.place(x=100,y=100)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = BusinessTravel)

    # Adding combobox drop down list
monthchoosen['values'] = ('Travel_Rarely','Travel_Frequently','No_Travel')
monthchoosen.place(x=450,y=100)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current() 
  
    #gender=tk.Entryroot,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Married)
    #gender.place(x=00,y=1)

l3=tk.Label(root,text="Department",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l3.place(x=100,y=150)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = Department)

    # Adding combobox drop down list
monthchoosen['values'] = ('Research and Development','Sales')
monthchoosen.place(x=450,y=150)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()  
    
l4=tk.Label(root,text="Gender",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l4.place(x=100,y=200)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = Gender)

    # Adding combobox drop down list
monthchoosen['values'] = ('Male','Female')
monthchoosen.place(x=450,y=200)
#monthchoosen.grid(column = 1, row = 1)
monthchoosen.current() 
  
    
l5=tk.Label(root,text="JobInvolvement",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l5.place(x=100,y=250)
JobInvolvement=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=JobInvolvement)
JobInvolvement.place(x=450 ,y=250) 

l6=tk.Label(root,text="JobLevel",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l6.place(x=100,y=300)
JobLevel=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=JobLevel)
JobLevel.place(x=450,y=300) 

l7=tk.Label(root,text="JobRole",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l7.place(x=100,y=350)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = JobRole)

    # Adding combobox drop down list
monthchoosen['values'] = ('Laboratory Technician','Research Scientist','Research Director','Sales Representative','Manager','Manufacturing Director','Sales Executive','Human Resource','Health Representative')
monthchoosen.place(x=450,y=350)
#monthchoosen.grid(column = 1, row = 1)
monthchoosen.current() 
    
l8=tk.Label(root,text="JobSatisfaction",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l8.place(x=100,y=400)
    #Self_Employed=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Self_Employed)
    #Self_Employed.place(x=400,y=200)
JobSatisfaction=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=JobSatisfaction)
JobSatisfaction.place(x=450,y=400) 



l9=tk.Label(root,text="MaritalStatus",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l9.place(x=100,y=450)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = MaritalStatus)

    # Adding combobox drop down list
monthchoosen['values'] = ('Single','Married','Divorced')
monthchoosen.place(x=450,y=450)
#monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()  

l10=tk.Label(root,text="MonthlyIncome",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l10.place(x=800,y=50)
MonthlyIncome=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=MonthlyIncome)
MonthlyIncome.place(x=1150,y=50) 

l11=tk.Label(root,text="NumCompaniesWorked",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l11.place(x=800,y=100)
#Self_Employed=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Self_Employed)
    #Self_Employed.place(x=400,y=200)
NumCompaniesWorked=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=NumCompaniesWorked)
NumCompaniesWorked.place(x=1150,y=100) 
    
        
l12=tk.Label(root,text="OverTime",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l12.place(x=800,y=150)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = OverTime)

    # Adding combobox drop down list
monthchoosen['values'] = ('No','Yes')
monthchoosen.place(x=1150,y=150)
#monthchoosen.grid(column = 1, row = 1)
monthchoosen.current() 
  
    
l13=tk.Label(root,text="PercentSalaryHike",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l13.place(x=800,y=200)
PercentSalaryHike=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PercentSalaryHike)
PercentSalaryHike.place(x=1150,y=200) 

    
l14=tk.Label(root,text="PerformanceRating",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l14.place(x=800,y=250)
PerformanceRating=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PerformanceRating)
PerformanceRating.place(x=1150,y=250) 
    
l15=tk.Label(root,text="Modeofwork",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l15.place(x=800,y=300)
    #Self_Employed=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Self_Employed)
    #Self_Employed.place(x=400,y=200)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = Modeofwork)

    # Adding combobox drop down list
monthchoosen['values'] = ('OFFICE','WFH')
monthchoosen.place(x=1150,y=300)
#monthchoosen.grid(column = 1, row = 1)
monthchoosen.current() 
    
l16=tk.Label(root,text="Jobmode",background="#8B8989",font=('times', 20, ' bold '),width=20,fg="white")
l16.place(x=800,y=350)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = Jobmode)

    # Adding combobox drop down list
monthchoosen['values'] = ('Contract','Part time','Full time')
monthchoosen.place(x=1150,y=350)
#monthchoosen.grid(column = 1, row = 1)
monthchoosen.current() 
    
    
    
button1 = tk.Button(root,text="Submit",command=Detect,background="black",font=('times', 20, ' bold '),width=10, fg="white")
button1.place(x=650,y=550)


root.mainloop()

Train()