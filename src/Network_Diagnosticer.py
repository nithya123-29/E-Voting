import os
from tkinter import *

#There is only a little code here because the main purpose of this program is allowing user to open the capture program and the reading program
#In the Class below, I defined a main user interface with two buttons: one is used to open the capture program and another is used to open the reading program
class DUI(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.AWidgets()
    def AWidgets(self):
        self.OpenCapButton=Button(self,text='Open Capture Program', command=self.OpenCap)
        self.OpenReaderButton=Button(self,text='Open the Reader', command=self.OpenReader)
        self.OpenCapButton.pack()
        self.OpenReaderButton.pack()

    def OpenCap(self):
        os.system('python3 Timing_Capture.py')
    def OpenReader(self):
        os.system('python3 Reader.py')
    
UI=DUI()
UI.master.title('Network Diagnosticer')
UI.master.geometry('400x300')
UI.mainloop()
