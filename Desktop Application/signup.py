from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#-------------------- Fonctions -----------------------

def connect_database():
    if emailbox.get()=='' or userNamebox.get()=='' or passwordbox.get()=='' or confPasswordbox.get()=='' :
        messagebox.showerror('Error','All Fields Are Required')
        return
    if passwordbox.get() != confPasswordbox.get() :
        messagebox.showerror('Error','Incompatible Password')
        return
    if not condition.get() :
        messagebox.showinfo('Warning','Please Accept our Terms & Conditions')
        return
    else :

    #---------------- Connection and save data to our database -------------------
        try :
            connection = pymysql.connect(host='localhost',user='root',password='1234')
            cursorExe = connection.cursor()
        except :
            messagebox.showerror('Error','Please Try Again! Database Not Connected')
            return

        try :
            command = 'create database diabete'
            cursorExe.execute(command)
            command = 'use diabete'
            cursorExe.execute(command)
            command = 'create table signup (id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(30))'
            cursorExe.execute(command)
        except :
            cursorExe.execute('use diabete')
            
                    #   ----- this block for test if the username exist or not if exist then cancel the operation --------

        
        command = 'select * from signup where username=%s'
        cursorExe.execute(command,(userNamebox.get()))


        if cursorExe.fetchone() :
            messagebox.showerror('Error','Username Already Exist')
            return

        else :
            #-------------------------------------------------------
            from hashlib import sha256

            
            sha256_hash = sha256()
            passwordHashed = passwordbox.get()
            sha256_hash.update(passwordHashed.encode('utf-8'))
            passwordHashed = sha256_hash.hexdigest()

            #---------------------------------------------------
            command = "insert into signup(email,username,password) value(%s,%s,%s) "
            cursorExe.execute(command,(emailbox.get(),userNamebox.get(),passwordHashed))
            connection.commit()
            connection.close()
            messagebox.showinfo('Success','Registration is successful')
            signWind.destroy()
            #call(["python", "loginPage.py"])
            import loginPage
            
            




def login_page() :
    signWind.destroy()
    #call(["python", "loginPage.py"])
    import loginPage
    
    

#---------------------- Sign up Page ---------------------------

signWind = Tk()
signWind.title('Signup Page')
signWind.resizable(False,False)


backgImage = ImageTk.PhotoImage(file='bg.jpg')
backgLabel = Label(signWind,image=backgImage)
backgLabel.grid()


gridFrame = Frame(signWind,bg='white')
gridFrame.place(x=554,y=100)


headlabel = Label(gridFrame,text='CREATE AN ACCOUNT',
            font=('Microsoft Yahei UI Light',18,'bold'),
            bg='white',fg='firebrick1')
headlabel.grid(row=0,column=0,padx=10,pady=10)


emailLabel = Label(gridFrame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='firebrick1',bg="white")
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))


emailbox = Entry(gridFrame,width=25,
                 font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
emailbox.grid(row=2,column=0,sticky='w',padx=25)


userNameLabel = Label(gridFrame,text='User Name',font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='firebrick1',bg="white")
userNameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))


userNamebox = Entry(gridFrame,width=25,
                 font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
userNamebox.grid(row=4,column=0,sticky='w',padx=25)


passwordLabel = Label(gridFrame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='firebrick1',bg="white")
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))


passwordbox = Entry(gridFrame,width=25,
                 font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
passwordbox.grid(row=6,column=0,sticky='w',padx=25)


confPasswordLabel = Label(gridFrame,text='Confirme Password',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='firebrick1',bg="white")
confPasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))


confPasswordbox = Entry(gridFrame,width=25,
                 font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
confPasswordbox.grid(row=8,column=0,sticky='w',padx=25)

condition = IntVar()
termsbutton = Checkbutton(gridFrame,text='I agree to the Terms & Conditions',
                          font=('Microsoft Yahei UI Light',9,'bold'),
                          fg='firebrick1',bg='white',
                          activeforeground='firebrick1',activebackground='white',
                          variable=condition)
termsbutton.grid(row=9,column=0,padx=15,pady=10)


signupButton = Button(gridFrame,text='Sign up',font=('Open Sans',16,'bold'),
                bd=0,bg='firebrick1',activebackground='firebrick1',
                fg='white',activeforeground='white',width=17,cursor='hand2',
                      command=connect_database)
signupButton.grid(row=10,column=0,pady=10)


alreadyaccount = Label(gridFrame,text='You already have an account?',
                       font=('Open Sans',9,'bold'),
                       bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)


login = Button(gridFrame,text='Login',bg='white',fg='blue',
                font=('Open Sans',9,'bold underline'),bd=0,
                activebackground='white',activeforeground='blue',
                cursor='hand2',command=login_page)
login.place(x=200,y=404)


signWind.mainloop()
