from tkinter import *
import tkinter.messagebox as messagebox
import os
import hashlib

filetxt='unpp.txt'      #Name Of the file that stored the username and password

class ChangeUNPPui(Frame):              #Use the class to define the GUI 
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.CheckForSafe()
    def CheckForSafe(self):
        messagebox.showinfo('Message','For Security, please enter your username and password')  #Inform to user that they need to input the username and password
        # the label for current user_name
        self.user_name = Label(self, text="Current User Name")
        self.user_name.pack()
        self.UNSinput=Entry(self)
        self.UNSinput.pack()
        # the label for current user_password
        self.user_password = Label(self, text="Current Password")
        self.user_password.pack()
        self.PPSinput=Entry(self,show='*')
        self.PPSinput.pack()
        self.Checkbutton=Button(self,text='Confirm',command=self.CheckInput)
        self.Checkbutton.pack()
    def CheckInput(self):
        usernameC=self.UNSinput.get()
        passwordC=self.PPSinput.get()
        if check_UNPP(usernameC,passwordC)==True:
            os.system('python3 ExecuteChangeUNPP.py')
        else:
            messagebox.showinfo('Message','Wrong username or password!')        #Return an error message to user to inform them that they input the current username and password

def storage():
    global un
    global pp
    filename=open(filetxt,'r')
    un=filename.readline()
    pp=filename.readline()    


def check_UNPP(us,pw):          #This function is used to hash the username and password input by user and hash them to compare with the information in the file
    us=us.encode('utf-8')
    pw=pw.encode('utf-8')
    Hash_US=hashlib.sha512()
    Hash_PP=hashlib.sha512()
    Hash_US.update(us)
    Hash_PP.update(pw)
    After_Hash_US=Hash_US.hexdigest()+'\n'
    After_Hash_PP=Hash_PP.hexdigest()
    if After_Hash_US==un and After_Hash_PP==pp:
        return True

storage()
CGUI=ChangeUNPPui()
CGUI.master.geometry('400x300')
CGUI.mainloop()
