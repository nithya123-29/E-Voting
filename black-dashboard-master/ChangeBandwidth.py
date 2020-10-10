from tkinter import *
import tkinter.messagebox as messagebox

#In the following GUI class, it contains an input box that allows user to input the network bandwidth and a button that confirm this operation and it will return a message to user that this operation is successful
#And it will return an error message to user if they input an invalid value
#Unit of bandwidth: Mbps
class UI(Frame):    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.inputUI()
    def inputUI(self):
        # the label for bandwidth
        self.bandwidth = Label(self, text="Bandwidth")
        self.bandwidth.pack()
        self.BandWidthInput=Entry(self)
        self.BandWidthInput.pack()
        self.ConfirmAction=Button(self,text='Confirm',command=self.Change)
        self.ConfirmAction.pack()
    def Change(self):
        UserProfile=open('Bandwidth.txt', 'w')
        Bandwidth=self.BandWidthInput.get()
        try:
            Bandwidth=int(Bandwidth)
            text="Bandwidth="+str(Bandwidth)+" "
            UserProfile.write(text)
            UserProfile.close()
            messagebox.showinfo("Message","Successful")
        except  ValueError:
            messagebox.showinfo("Message","The value input is invaild, please try again")

Main=UI()
Main.master.title("Change Bandwidth")
Main.master.geometry('400x300')
Main.mainloop()
