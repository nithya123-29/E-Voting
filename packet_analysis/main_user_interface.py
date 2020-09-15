import os
from tkinter import *

#GUI interface
class UI(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.Widgets()
    def Widgets(self):          #In this fuction, I made some buttons that are used to open different modules
        self.bandwidthbutton=Button(self,text='Open the network interface bandwidth configuration tool',command=self.openbandwidth)   #Create a button used to open the bandwidth setting tools
        self.bandwidthbutton.pack()
        self.NDopenbutton=Button(self,text='Open Network Diagnosticer',command=self.openND)  #Create a button use to open the Network Diagnostic tools
        self.NDopenbutton.pack()
        self.OpenSettingToolsButton=Button(self,text='Open the setting tools to set you capture interface',command=self.OpenSettingTools)   #Create a button used to open the interface setting tools
        self.OpenSettingToolsButton.pack()




    def openbandwidth(self):
        os.system('python3 ChangeBandwidth.py')
    def openND(self):
        os.system('python3 Network_Diagnosticer.py')
    def OpenSettingTools(self):
        os.system('python3 Interface_Setting.py')








UI=UI()
UI.master.title('Main user interface')
UI.master.geometry('400x300')
UI.mainloop()
