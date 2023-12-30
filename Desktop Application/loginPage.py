from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


#------------- Functions --------------
def signup_page() :
    logWind.destroy()
    import signup
    
    

def user_enter(event) :
    if usernamebox.get()=='UserName' :
        usernamebox.delete(0,END)


def password_enter(event) :
    if passwordbox.get()=='Password' :
        passwordbox.delete(0,END)



def hide() :
    openeye.config(file='closeeye.png')
    passwordbox.config(show='*')
    eyeButton.config(command=show)


def show() :
    openeye.config(file='openeye.png')
    passwordbox.config(show='')
    eyeButton.config(command=hide)


def login_user() :
    if usernamebox.get() in ['','UserName'] or passwordbox.get() in ['','Password'] :
        messagebox.showerror('Error','All Fields Are Required')
        return

    try :
            connection = pymysql.connect(host='localhost',user='root',password='1234')
            cursorExe = connection.cursor()
    except :
            messagebox.showerror('Error','Please Try Again! Database Not Connected')
            return
    
    from hashlib import sha256

            
    sha256_hash = sha256()
    passwordHashed = passwordbox.get()
    sha256_hash.update(passwordHashed.encode('utf-8'))
    passwordHashed = sha256_hash.hexdigest()

    cursorExe.execute('use diabete')
    cursorExe.execute('select * from signup where username=%s and password=%s',(usernamebox.get(),passwordHashed))

    if not cursorExe.fetchone() :
        messagebox.showerror('Error','Incorrect UserName or Password')
    else :
        
        messagebox.showinfo('Success','Welcome to our Application')
        logWind.destroy()
        import Preview
        connection.commit()
        connection.close()
        #import Preview
        
        
        
        
        

def reset_password_wind() :

    def change_passwd() :
        if userBox.get() == '' or passwdBox.get() == '' or confirmPassBox.get() == '':
            messagebox.showerror('Error','All Fields Are Required')
            return

        if passwdBox.get() != confirmPassBox.get() :
            messagebox.showerror('Error','Incompatible Password')
            return
        try :
            connection = pymysql.connect(host='localhost',user='root',password='1234')
            cursorExe = connection.cursor()
        except :
            messagebox.showerror('Error','Please Try Again! Database Not Connected')
            return

        cursorExe.execute('use diabete')
        cursorExe.execute('select * from signup where username=%s',(userBox.get()))

        if cursorExe.fetchone()== None :
            messagebox.showerror('Error','UserName Does Not Exist')
            return

        cursorExe.execute('update signup set password=%s where username=%s',(passwdBox.get(),userBox.get()))
        messagebox.showinfo('Success','You Have Successfully Changed Your Password')
        connection.commit()
        connection.close()
        resetWindow.destroy()

        
    
    resetWindow = Toplevel(logWind)
    resetWindow.title('Reset Password ')

    bgIm = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(resetWindow,image=bgIm)
    bgLabel.grid()

    headLabel = Label(resetWindow,text='RESET PASSWORD',font=('arial',18,'bold'),
                      bg='white',fg='magenta2')
    headLabel.place(x=480,y=60)

            #-------------------------------

    userLabel = Label(resetWindow,text='UserName',font=('arial',12,'bold'),
                      bg="white",fg='orchid1')
    userLabel.place(x=470,y=130)
    

    userBox = Entry(resetWindow,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    userBox.place(x=470,y=160)


    Frame(resetWindow,width=250,height=2,bg='orchid1').place(x=470,y=180)


    #-------------------------------


    passwdLabel = Label(resetWindow,text='New Password',font=('arial',12,'bold'),
                      bg="white",fg='orchid1')
    passwdLabel.place(x=470,y=210)
    

    passwdBox = Entry(resetWindow,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    passwdBox.place(x=470,y=240)


    Frame(resetWindow,width=250,height=2,bg='orchid1').place(x=470,y=260)


    #-------------------------------

    confirmPassLabel = Label(resetWindow,text='Confirm Password',font=('arial',12,'bold'),
                      bg="white",fg='orchid1')
    confirmPassLabel.place(x=470,y=290)
    

    confirmPassBox = Entry(resetWindow,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    confirmPassBox.place(x=470,y=320)


    Frame(resetWindow,width=250,height=2,bg='orchid1').place(x=470,y=340)


    resetButton = Button(resetWindow,text='Reset',bd=0,bg='magenta2',fg='white',font=('Open Sans','16','bold'),
                         width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',command=change_passwd)
    resetButton.place(x=470,y=390)


    
    
    resetWindow.mainloop()
    

#------------- Login GUI ---------------
logWind = Tk()

logWind.title("Sign in")
logWind.geometry("990x660+200+30")
logWind.resizable(False,False)
backgf = ImageTk.PhotoImage(file="bg.jpg")


bgLabel = Label(logWind,image=backgf)
bgLabel.place(x=0,y=0)


headlabel = Label(logWind,text='USER LOGIN',
            font=('Microsoft Yahei UI Light',23,'bold'),
            bg='white',fg='firebrick1')
headlabel.place(x=605,y=130)


usernamebox = Entry(logWind,width=25,
            font=('Microsoft Yahei UI Light',11,'bold'),
            bd=0,fg='firebrick1')
usernamebox.place(x=580,y=210)
usernamebox.insert(0,'UserName')
usernamebox.bind('<FocusIn>',user_enter)    


frameline1 = Frame(logWind,width=250,height=2,
                   bg='firebrick1').place(x=580,y=232)


passwordbox = Entry(logWind,width=25,
            font=('Microsoft Yahei UI Light',11,'bold'),
            bd=0,fg='firebrick1')
passwordbox.place(x=580,y=270)
passwordbox.insert(0,'Password')
passwordbox.bind('<FocusIn>',password_enter)


frameline2 = Frame(logWind,width=250,height=2,
                   bg='firebrick1').place(x=580,y=292)


openeye = PhotoImage(file='openeye.png')
eyeButton = Button(logWind,image = openeye,bd=0,
            bg='white',activebackground='white',
                cursor='hand2')
eyeButton.place(x=800,y=265)
eyeButton.config(command=hide)


forgotButton = Button(logWind,text="Forgot password ?",
            bd=0,bg='white',activebackground='white',
            cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),
            activeforeground='firebrick1',fg='firebrick1',command=reset_password_wind)
forgotButton.place(x=715,y=305)


loginButton = Button(logWind,text="Login",font=('Open Sans',16,'bold'),
                     fg='white',bg='firebrick1',activeforeground='white',
                     activebackground='firebrick1',cursor='hand2',
                     bd=0,width=19,command=login_user)
loginButton.place(x=578,y=360)



signUpLabel = Label(logWind,text='Dont have an account?',
                font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signUpLabel.place(x=593,y=445)



newAccountButton = Button(logWind,text="Create new one",
                     font=('Open Sans',9,'bold underline'),
                     fg='blue',bg='white',activeforeground='blue',
                     activebackground='white',cursor='hand2',
                     bd=0,command=signup_page)
newAccountButton.place(x=727,y=445)

logWind.mainloop()



#"790x515+300+100"
