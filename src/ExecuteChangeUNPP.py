from tkinter import *
import tkinter.messagebox as messagebox
import hashlib
filename='unpp.txt'         #The location of the file
class EGUI(Frame):          #Use the class to make the GUI
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.UI()
    def UI(self):
        self.NewUNinput=Entry(self)         #Input box for username
        self.NewPPinput=Entry(self,show='*')    #Input box for password
        self.ComPPinput=Entry(self,show='*')    #Input box for repeat password
        self.CheckButton=Button(self,text='Comfirm',command=self.NEW_Com)   
        self.NewUNinput.pack()
        self.NewPPinput.pack()
        self.ComPPinput.pack()
        self.CheckButton.pack()


    def NEW_Com(self):
        NewPP=self.NewPPinput.get()     #Get the new password
        ComPP=self.ComPPinput.get()     #Get the repeat password
        NewUN=self.NewUNinput.get()     #Get the new username
        if NewPP==ComPP:                
            change(NewUN,NewPP)         #If the new password match the repeat password, then change the username and password by using change(UN,PP) function
        else:
            messagebox.showinfo('Message','The first password does not match the second password')  #Return a error message to user if the new password doesn't match the password



def change(UN,PP):
    openfile=open(filename,'w')     #mode 'w' will open the text file and erase all the text
    PP=PP.encode('utf-8')
    UN=UN.encode('utf-8')
    Hash_UN=hashlib.sha512()
    Hash_PP=hashlib.sha512()
    Hash_UN.update(UN)
    Hash_PP.update(PP)
    After_Hash_UN=Hash_UN.hexdigest()
    After_Hash_PP=Hash_PP.hexdigest()
    openfile.write(After_Hash_UN+'\n')
    openfile.write(After_Hash_PP)
    openfile.close()
    messagebox.showinfo('Message','Username and Password are successfully changed!')


execute=EGUI()
execute.master.title('Change Password')
execute.master.geometry('400x300')
execute.mainloop()
    
    

        
        
