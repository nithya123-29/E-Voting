from tkinter import *
import tkinter.messagebox as messagebox

#In the class below, it defined a user interface to allow the user to input the name of the network interface.
#Above the input box, there are two buttons: one is set the capture interface as Wi-Fi and another set as Ethernet
#Under these two buttons, there is a text box and a button. The text box allows user to input the name of the capture interface if the name of the interface is not shown above.
#And the button is set the capture interface as the name input by user

class UI(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.SettingUI()
    def SettingUI(self):
        self.SetWifiAsNicButton=Button(self,text="set your capture interface as Wi-Fi(If you normally use this as your main interface",command=self.SetAsWifi)
        self.SetWifiAsNicButton.pack()
        self.SetEthernetZeroButton=Button(self,text="set your capture interface as Ethernet(If you normally use this as your main interface",command=self.SetAsEthernet)
        self.SetEthernetZeroButton.pack()
        self.InputInterface=Entry(self)
        self.InputInterface.pack()
        self.InputAndSetButton=Button(self,text="If your interface is no shown above, please enter your interface and click me",command=self.SetAsInput)
        self.InputAndSetButton.pack()

    def SetAsWifi(self):
        UserProfile=open("User.txt",'w')
        UserProfile.write("Capture Interface=Wi-Fi")
        UserProfile.close()
        messagebox.showinfo("Message","Success")

    def SetAsEthernet(self):
        UserProfile=open("User.txt",'w')
        UserProfile.write("Capture Interface=Ethernet")
        UserProfile.close()
        messagebox.showinfo("Message","Success")

    def SetAsInput(self):
        UserProfile=open("User.txt",'w')        
        Name_Of_Interface=self.InputInterface.get()
        String_To_Write="Capture Interface="+str(Name_Of_Interface)+" \n"
        UserProfile.write(String_To_Write)      #Wrtie the name of the interface to the file to let the capture program to read it
        UserProfile.close()
        messagebox.showinfo("Message","Success")



SUI=UI()
SUI.master.title("Setting")
SUI.master.geometry('400x300')
SUI.mainloop()
