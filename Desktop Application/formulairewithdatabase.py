from tkinter import *
from tkinter import messagebox
import pymysql

from pandas import DataFrame
from pickle import load







#------------------------------------------ Functions -----------------------------------------------


def sauvgarde(input):
    
    try :
            connection = pymysql.connect(host='localhost',user='root',password='1234')
            cursorExe = connection.cursor()
    except :
            messagebox.showerror('Error','Please Try Again! Database Not Connected')
            return
    
    try :
        command = 'use diabete'
        cursorExe.execute(command)
        command = 'create table modelPredic(id int auto_increment primary key not null,Pregnancies float,Glucose float,BloodPressure float,SkinThickness float,Insulin float,BMI float,DPFunction float,Age float,Outcome float)'
        cursorExe.execute(command)
    except :
        cursorExe.execute('use diabete')
    
    
    command = 'insert into modelpredic value(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursorExe.execute(command,(input[0],input[1],input[2],input[3],input[4],input[5],input[6],input[7],input[8]))
    connection.commit()
    connection.close()
    messagebox.showinfo('Success','sauvegarde reussi')


def Predect() :
    
    
    pre = ecr_pre.get()
    gle = ecr_Gle.get()
    bp = ecr_bp.get()
    sk = ecr_sk.get()
    ins = ecr_ins.get()
    bmi = ecr_bmi.get()
    dia = ecr_dia.get()
    ag = ecr_ag.get()

    if pre == '' or gle == '' or bp == '' or sk == '' or ins == '' or bmi == '' or dia == '' or ag == '' :
        messagebox.showerror('Error','All Fields Are Required')
        return
                        

    
    with open(r'C:\Users\Aboubakr\Desktop\PFE\Application\super_model','rb') as f :
         super_model = load(f)


    
    
    input_data = [[pre,gle,bp,sk,ins,bmi,dia,ag]]

    column = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']

    input_data = DataFrame(input_data,columns=column)
    
    

    prediction = super_model.predict(input_data)
                        

    global label_file

    if (prediction[0] == 0):
                               
        label_file["text"]="The person is not diabetic"
        label_file["fg"]="limegreen"
        label_file.place(x=250,y=520,width=300,height=30)
                               
    else:
                                          
        label_file["text"]="The person is  diabetic"
        label_file["fg"]="firebrick1"
        label_file.place(x=250,y=520,width=300,height=30)

    input = [pre,gle,bp,sk,ins,bmi,dia,ag,prediction[0]]
    
    if messagebox.askquestion('Save','Voulez-vous Sauvegarder cet Prediction ?') == 'yes' :
        sauvgarde(input)

    


def reni() :
    ecr_pre.delete(0,END)
    ecr_Gle.delete(0,END)
    ecr_bp.delete(0,END)
    ecr_sk.delete(0,END)
    ecr_ins.delete(0,END)
    ecr_bmi.delete(0,END)
    ecr_dia.delete(0,END)
    ecr_ag.delete(0,END)
    global label_file
    label_file.place_forget()



#---------------------------------------------------------------------------------------------
#--------------------------------------- Predict window GUI ----------------------------------
#---------------------------------------------------------------------------------------------


root=Tk()
root.title("Diabetes Prediction ")
root.geometry("800x680+300+10")
root.config(bg="#EF4166")
                

Label(root,text="Diabetes Prediction",font=("algerian",20,"bold") ,bg="#EF4166", fg="white").place(x=250,y=12)


contentFrame = Frame(root,bg="#FFCFE9")
contentFrame.place(x=100, y= 70, width=600,height=580)
                
Label(contentFrame, text="Pregnancies",bg="#FFCFE9",   
      fg="#EF4166",font=("time new roman", 15,'bold')).grid(column=0,row=0,sticky='w',padx=65,pady=(30,10))      
          
ecr_pre=Entry(contentFrame, bg='#EF4166',fg='white',font=("time new roman",15))
ecr_pre.grid(column=1,row=0,padx=25,pady=(30,10))
                
Label(contentFrame, text="Glucose",  
      fg="#EF4166",font=("time new roman", 15,'bold'),bg="#FFCFE9").grid(column=0,row=1,sticky='w',padx=65,pady=(10,10))                
ecr_Gle=Entry(contentFrame, bg="#EF4166",fg='white',font=("time new roman",15))
ecr_Gle.grid(column=1,row=1,padx=25,pady=(10,10)) 
                
Label(contentFrame, text="BP", bg="#FFCFE9",  
      fg="#EF4166",font=("time new roman", 15,'bold')).grid(column=0,row=2,sticky='w',padx=65,pady=(10,10))                
ecr_bp=Entry(contentFrame, bg="#EF4166",fg='white',font=("time new roman",15))
ecr_bp.grid(column=1,row=2,padx=25,pady=(10,10)) 
                
Label(contentFrame, text="Skin TK", bg="#FFCFE9",   
      fg="#EF4166",font=("time new roman", 15,'bold')).grid(column=0,row=3,sticky='w',padx=65,pady=(10,10))                
ecr_sk=Entry(contentFrame, bg="#EF4166",fg='white',font=("time new roman",15))
ecr_sk.grid(column=1,row=3,padx=25,pady=(10,10)) 


Label(contentFrame, text="Insulin", bg="#FFCFE9",  
      fg="#EF4166",font=("time new roman", 15,'bold')).grid(column=0,row=4,sticky='w',padx=65,pady=(10,10))  
ecr_ins=Entry(contentFrame, bg="#EF4166",fg='white',font=("time new roman",15))              
ecr_ins.grid(column=1,row=4,padx=25,pady=(10,10)) 
                
Label(contentFrame, text="BMI", bg="#FFCFE9",  
      fg="#EF4166",font=("time new roman", 15,'bold')).grid(column=0,row=5,sticky='w',padx=65,pady=(10,10))               
ecr_bmi=Entry(contentFrame, bg="#EF4166",fg='white',font=("time new roman",15))
ecr_bmi.grid(column=1,row=5,padx=25,pady=(10,10)) 
                
Label(contentFrame, text="DiabetesPF", bg="#FFCFE9",  
      fg="#EF4166",font=("time new roman", 15,'bold')).grid(column=0,row=6,sticky='w',padx=65,pady=(10,10))                
ecr_dia=Entry(contentFrame, bg="#EF4166",fg='white',font=("time new roman",15))
ecr_dia.grid(column=1,row=6,padx=25,pady=(10,10)) 
                
Label(contentFrame, text="Age", bg="#FFCFE9", 
      fg="#EF4166",font=("time new roman", 15,'bold')).grid(column=0,row=7,sticky='w',padx=65,pady=(10,10))              
ecr_ag=Entry(contentFrame, bg="#EF4166",fg='white',font=("time new roman",15))
ecr_ag.grid(column=1,row=7,padx=25,pady=(10,10)) 


global label_file
label_file = Label(root,text='The person is not diabetic',fg="limegreen",bg='#FFCFE9',font=("time new roman", 16,'bold'))
#label_file.place(x=250,y=520,width=300,height=30)

Button(contentFrame, text="  Predict  ",font=('Open Sans',17,'bold'),
                     fg='white',bg='#EF4166',activeforeground='white',
                     activebackground='#EF4166',cursor='hand2',
                     bd=0,command=Predect).grid(column=0,row=8,padx=65,pady=(90,10))

Button(contentFrame, text=" Initialize ",font=('Open Sans',17,'bold'),
                     fg='white',bg='#EF4166',activeforeground='white',
                     activebackground='#EF4166',cursor='hand2',
                     bd=0,command=reni).grid(column=1,row=8,padx=25,pady=(90,10))
                


root.mainloop()