from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as messagebox
import re
import os
import eel
import easygui

def OpenFile():
    global filename
    filename=askopenfilename(filetypes=(("txt file","*.txt"),("All files","*.*")))  #Allows user to browse the location of the capture information text and store it to the global variable: filename
    Reading()


def graph(self):
    os.system('python3 graph.py')

@eel.expose
def Reading():
    global file
    global Time_Cap
    file=open("D:/CapSyslog/A.txt")
    # print(easygui.fileopenbox())
    Find_Cap_Time=file.readline()
    line=file.readline()
    Index_Time_Cap=Find_Cap_Time.find("Capture time",0)
    Index_Time_Cap+=13
    Time_Cap=""
    while Find_Cap_Time[Index_Time_Cap] !=' ':
        Time_Cap+=Find_Cap_Time[Index_Time_Cap]
        Index_Time_Cap+=1
    Time_Cap=int(Time_Cap)
    #In the code above (From Find_Cap_Time=file.readline() to here, it gets the capture time written by the capture program.
    #Because "Capture time" has 12 characters (include space), so the first number will start at the 13th of the string.
    #Because when the capture program will the capture time, after the number it left a blank, so if the program find that place is a blank, it knows this is the end of the line.

    #In the following codes, it's the implement of the pseudo code
    Num_Of_Broadcast=0
    Num_Of_TCPSYN=0
    Num_Of_Size_Of_TCP=0
    Num_Of_Size_Of_UDP=0
    Num_Of_Size_Of_ICMP=0
    buffer=[['' for i in range(2)] for j in range(40)]          #Create a two-dimension array to store the source MAC address of the broadcast packet and the number of packets send by them
    for x in range (40):
        buffer[x][1]=0
    while line!='':                     #Equal to While not EOF
        if "Broadcast" in line:         #If the type of the packet is broadcast
            Num_Of_Broadcast+=1
            index=15
            buffer_addr=""
            while line[index]!=' ':             #This loop is used to get the source MAC address of the broadcast packet
                buffer_addr+=line[index]
                index+=1
            n=0
            while buffer_addr!="":              #This loop is used to write the MAC address of the broadcast packet to the buffer (the two-dimension array)
                if buffer[n][0]==buffer_addr:
                    buffer[n][1]+=1
                    buffer_addr=""
                if buffer[n][0]!='':
                    n+=1
                if buffer[n][0]=="":
                    buffer[n][0]=buffer_addr
                    buffer[n][1]+=1
                    buffer_addr=""
        if "TCP" in line:           #If the type of the packet is TCP
            # if "SYN" in line:       #If this TCP packet is a SYN packet
            #     Num_Of_TCPSYN+=1    #This number is used to check if the computer system is being TCP SYN Flood Attack
            TCP_Size=""
            Index_TCP=line.find("TCP",0)
            Index_TCP+=4
            while line[Index_TCP] !=' ' :           #This loop is used to get the size of the TCP packet (Cause some video sites will use TCP to transfer the video stream (E.g. Niconico)
                TCP_Size+=line[Index_TCP]
                Index_TCP+=1
            if bool(re.search(r'\d',TCP_Size))==True:       #By using regular expression to check if this information is a number (Cause sometimes some information like :TCP.abc, the information after TCP is not a number
                Num_Of_Size_Of_TCP+=int(TCP_Size)
        if "QUIC" in line:
            Index_QUIC=line.find("QUIC",0)
            Index_QUIC+=5
            QUIC_Size=""
            while line[Index_QUIC] !=' ':
                QUIC_Size+=line[Index_QUIC]
                Index_QUIC+=1
            Num_Of_Size_Of_UDP+=int(QUIC_Size)              #Notice:QUIC stands for Quick UDP Internet Connection, it belongs to UDP. Some video sites will use this protocol to transfer the video stream (E.g. Youtube)
        if "UDP" in line:
            Index_UDP=line.find("UDP",0)
            Index_UDP+=4
            UDP_Size=""
            while line[Index_UDP] !=' ':                    #Get the size of UDP packet to check if the computer system is being UDP Flood Attack
                UDP_Size+=line[Index_UDP]
                Index_UDP+=1
            Num_Of_Size_Of_UDP+=int(UDP_Size)

        if "ICMP" in line:
            Index_ICMP=line.find("ICMP",0)
            Index_ICMP+=5
            ICMP_Size=""
            while line[Index_ICMP] !=' ':                   #Get the size of the ICMP packet to check if the computer system is being ICMP Flood Attack
                ICMP_Size+=line[Index_ICMP]
                Index_ICMP+=1
            Num_Of_Size_Of_ICMP+=int(ICMP_Size)

        line=file.readline()                            #Start reading the next line
    # REPORT=self.Report(Num_Of_Broadcast,Num_Of_TCPSYN,Num_Of_Size_Of_UDP,Num_Of_Size_Of_ICMP,Num_Of_Size_Of_TCP,buffer) #Send these information to the mathod called "REPORT" to analyse these figures
    REPORT=Report(Num_Of_Broadcast,Num_Of_Size_Of_UDP,Num_Of_Size_Of_ICMP,Num_Of_Size_Of_TCP,buffer) #Send these information to the mathod called "REPORT" to analyse these figures
    file.close()
    return REPORT       #Return a report that includes the statistics of the packet capturing to user




# def Report(self,Broadcast,TCP,UDP,ICMP,TCP_Size,Broadcast_List):
def Report(Broadcast,UDP,ICMP,TCP_Size,Broadcast_List):
    bandwidth_file=open('Bandwidth.txt')
    Bandwidth_Text=bandwidth_file.readline()
    Index_Bandwidth=10
    Bandwidth=""
    Bandwidth_Output=""
    if Bandwidth_Text!="":
        while Bandwidth_Text[Index_Bandwidth] !=" ":
            Bandwidth+=Bandwidth_Text[Index_Bandwidth]
            Index_Bandwidth+=1
    else:
        Bandwidth=32.01
    Bandwidth=float(Bandwidth)
    Data_Flow_Speed=12500*Bandwidth         #The unit of Data_Flow_Speed is in byte per second
    if Bandwidth==32.01:
        Bandwidth_Output="Bandwidth: 32.01 Mbps"
    if Bandwidth!=32.01:
        Bandwidth_Output="Bandwidth: "+str(Bandwidth)+ " Mbps"
    text_Broadcast=""
    text_TCP=""
    text_UDP=""
    text_TCP_S=""
    Broadcast_PList=Broadcast_List
    text_Broadcast_List=""
    Safe=True
    for i in range (40):
        if Broadcast_PList[i][0]!='':
            text_Broadcast_List+="      "+str(Broadcast_PList[i][0])+": "+str(Broadcast_PList[i][1])+"\n"       #Get the soruce MAC Address of the broadcast packets and the number of broadcast packets those are sent by them
    if text_Broadcast_List!="":
        text_Broadcast_List="The source and number of broadcast packet in your LAN are"+'\n'+text_Broadcast_List
    if Broadcast>=Time_Cap/0.1:
        text_Broadcast="If you feel your computer system is slow, the reason probably is the number of broadcast packet in your LAN network is too much.\n "
        Safe=False
    # if TCP>=Time_Cap/0.001:
    #     text_TCP="If you feel your computer system is slow, the reason probably is you are being SYN Flood(A type of DDoS attack) attack.\n"
    #     Safe=False
    if UDP>=Data_Flow_Speed*Time_Cap:
        text_UDP="If you fell your computer system if slow, the reason probably is you are being UDP Flood(A type of DDoS attack) attack or some software(or site) are using your network resources(Normally are the video sites).\n"
        Safe=False
    if TCP_Size>=Data_Flow_Speed*Time_Cap:
        text_TCP_S="If you feel your computer system is slow, the reason probably is you are being TCP flood attack or some software are transfering data(or site e.g video sites)"
        Safe=False
    # statistics="Number Of Broadcast packet is "+str(Broadcast)+"\n"+"Number of TCP SYN packets is "+str(TCP)+"""Number of Size of UDP packets is """+str(UDP)+"\n"+"Number of Size of ICMP packets is "+str(ICMP)+"\n"+"Number of Size of TCP packets is "+str(TCP_Size)+"\n"
    statistics = "Number Of Broadcast packet is " + str(Broadcast) + "<br>" + """Number of Size of UDP packets is """ + str(UDP) + "<br>" + "Number of Size of ICMP packets is " + str(ICMP) + "<br>" + "Number of Size of TCP packets is " + str(TCP_Size) + "<br>"
    if Safe==True:
        # DDoS_report=Bandwidth_Output+'\n'+"Time Captured:"+str(Time_Cap)+'\n'+statistics+"\nWoooh, it seens that your computer doen't being DDoS Attack"+"\n"+text_Broadcast_List
        report = Bandwidth_Output + '<br>' + "Time Captured:" + str(Time_Cap) + '<br>' + statistics
    else:
        # DDoS_report=Bandwidth_Output+'\n'+"Time Captured:"+str(Time_Cap)+'\n'+statistics+"\n"+text_Broadcast+text_TCP+text_UDP+text_TCP_S+"\n"+text_Broadcast_List
        report = Bandwidth_Output + '<br>' + "Time Captured:" + str(Time_Cap) + '<br>' + statistics
    return report
