

from tkinter import Tk,Label,Frame,LabelFrame,ttk,Scrollbar,Label,Button,filedialog,messagebox
from pandas import read_csv,read_excel




# initalise the tkinter GUI

root = Tk()
global file_frame1

root.geometry("714x630+300+30") # set the root dimensions
root.configure(bg="#EF4166")
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.

Label(root,text="Dataset Preview",font=('Open Sans',18,'bold'),
            bg='#EF4166',fg='white').place(x=260,y=12)

contentFrame = Frame(root,bg="#FFCFE9")
contentFrame.place(x=70,y=60,height=515,width=574)

#----------------------------------------------------------------------

# Frame for TreeView
treeFrame = LabelFrame(root, text="Check Out Dataset",bg="#FFCFE9")
treeFrame.place(x=112,y=80,height=250, width=500)

## Treeview Widget
style = ttk.Style(root)
style.configure("Custom.Treeview", background="#FFCFE9") # the color of the tree background 

tv1 = ttk.Treeview(treeFrame, style="Custom.Treeview")
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (treeFrame).

treescrolly = Scrollbar(treeFrame, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = Scrollbar(treeFrame, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

#--------------------------------------------------------------------------------

# Frame for open file dialog
file_frame = LabelFrame(root, text="Open File",bg="#FFCFE9")
file_frame.place(x=112,y=350,height=80, width=500)


# The file/file path text
label_file = Label(file_frame, text="No File Selected",background="#FFCFE9")
label_file.place(rely=0, relx=0)

# Buttons
browseButton = Button(file_frame, text="Browse A File" ,font=('Open Sans',12,'bold'),
                     fg='white',bg='#EF4166',activeforeground='white',
                     activebackground='#EF4166',cursor='hand2',
                     bd=0,command=lambda: File_dialog()
                    )
browseButton.place(rely=0.4, relx=0.55,width=120)

loadButton = Button(file_frame, text="Load File", font=('Open Sans',12,'bold'),
                     fg='white',bg='#EF4166',activeforeground='white',
                     activebackground='#EF4166',cursor='hand2',
                     bd=0,command=lambda: Load_excel_data())
loadButton.place(rely=0.4, relx=0.25,width=120)

#-----------------------------------------------------------------------------------


predictLabel = LabelFrame(root, text="Prediction",background="#FFCFE9")
predictLabel.place(y=450, x=112,width=500,height=80 )

b2 = Button(predictLabel, text="Go To Prediction", font=('Open Sans',12,'bold'),
                     fg='white',bg='#EF4166',activeforeground='white',
                     activebackground='#EF4166',cursor='hand2',
                     bd=0, command=lambda:test()).place(relx=0.32, rely=0.4, width=200
                )








#------------------------------------- Functions ----------------------------------------------------

def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    global filename
    filename = filedialog.askopenfilename(initialdir=r"C:\Users\Aboubakr\Desktop\PFE\Application",
                                          title="Select A File",
                                          filetype=(("csv files","*csv"),("xlsx files","*xlsx"),("All Files", "*.*")))

    n=[]
    n=filename.split("/")         
    label_file["text"] = n[-1]
    return None


def Load_excel_data():
    
    """If the file selected is valid this will load the file into the Treeview"""
    
    if label_file["text"] == "No File Selected" :
        messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    
    else :
        file_path = filename
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = read_csv(excel_filename)
            else:
                df = read_excel(excel_filename)

        except ValueError:
            messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column) # let the column heading = column name

        df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.thtml#tkinter.tTreeview.insert
        return None
 
def clear_data():
    tv1.delete(*tv1.get_children())
    return None

def test():
    root.destroy()
    import formulairewithdatabase
    
    
    
                        
root.mainloop()
