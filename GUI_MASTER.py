from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve

root = tk.Tk()
root.title("Work force attrition system")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image2 = Image.open('c2.png')
image2 = image2.resize((w, h))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  




  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Work force attrition system", font=('times', 35,' bold '), height=2, width=62,bg="#560319",fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def SVM():
    data = pd.read_csv("dataset.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""


    """Feature Selection => Manual"""
    x = data.drop(['Attrition'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Attrition']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=12)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SVM_Prediction.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"SVM_Prediction.joblib")
    print("Model saved as SVM_Prediction.joblib")


def RF():
    data = pd.read_csv("dataset.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""
   


    """Feature Selection => Manual"""
    x = data.drop(['Attrition'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Attrition']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=2)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    
    from sklearn.ensemble import RandomForestClassifier  
    svcclassifier =RandomForestClassifier(n_estimators= 10, criterion="entropy") 
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
     
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as RF_Prediction.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"RF_Prediction.joblib")
    print("Model saved as RF_Prediction.joblib")
    
    

def DT():
    data = pd.read_csv("dataset.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""


    """Feature Selection => Manual"""
    x = data.drop(['Attrition'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Attrition']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=2)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier(criterion='entropy', random_state=0)  
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()


 
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as DT_Prediction.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"DT_Prediction.joblib")
    print("Model saved as DT_Prediction.joblib")


def call_file():
    print("Check")
    from subprocess import call
    call(["python","Check.py"])  



def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="SVM Training", command=SVM, width=15, height=2)
button3.place(x=600, y=160)

button4 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="RF Training", command=RF, width=15, height=2)
button4.place(x=600, y=240)

button5 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="DT Training", command=DT, width=15, height=2)
button5.place(x=600, y=320)

button6 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Work force attrition", command=call_file, width=25, height=2)
button6.place(x=600, y=400)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=600, y=480)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''