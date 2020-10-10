import subprocess
from tkinter import *
import tkinter.messagebox as messagebox
import time
from ReaderStat import Reading
import os
import shutil
import eel

eel.init('Web')


# In this module, the user interface only includes two buttons and one input box
# The button above is used to capture the program with 10 seconds
# If the user want to capture the packets for other times, they can input a number in the text box and press the lowest button


@eel.expose
def CheckInterfaceAndCap(line):

    if line == "Wi-Fi":
        capturedPackets = OpenTshark_WiFi()  # Using OpenTshark_WiFi() method to capture packets via Wi-Fi
        # checkfile.close()  # Close the file
        return capturedPackets  # The purpose of return 0 is return a value and end this method so that the program will not continue (Or otherwise the program will capture twice because of the else statement)
    if line == "Ethernet":
        capturedPackets = OpenTshark_Ethernet()  # Using OpenTshark_Ethernet() method to capture packets via Ethernet
        # checkfile.close()
        return capturedPackets
    else:
        capturedPackets = OpenTshark_Any(
            line)  # If the name of interface is neither Wi-Fi nor Ethernet, the program will get take the name of the network interface and pass this as a parameter to OpenTshark_Any(line) method
        # report = Reader.Reading()
        return capturedPackets
        # return [capturedPackets, report]

# In the following code, tshark -i [name of the interface] will let tshark using this interface to capture
# -a duration: [time] will let tshark stop capturing automatically after that time period
# >> D:\CapSyslog\A.txt will stored the syslog of CMD to D:\CapSyslog\A.txt
def OpenTshark_WiFi():
    file = open("C:/Program Files/Wireshark/A.txt", 'w')  # 'w' mode will erase all the text in the file when it's opened by the program
    file.write("Capture time:10 \n")  # Write the Capture time to the txt file so that the reading will know how long does the capture last
    file.close()
    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -i WiFi -w firstcapturedpackets.pcap -F pcap -a duration:10')  # Cause tshark is in C:\Program Files\Wireshark, so before it's executed in CMD, we need to change the location first.
    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r firstcapturedpackets.pcap -t ad > firstcapturedpackets.txt')
    fin = open("C:/Program Files/Wireshark/firstcapturedpackets.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open("C:/Program Files/Wireshark/A.txt", "a")
    fout.write(data2)
    fout.close()
    files = ['C:/Program Files/Wireshark/A.txt', 'C:/Program Files/Wireshark/firstcapturedpackets.pcap','C:/Program Files/Wireshark/firstcapturedpackets.txt']
    for f in files:
        shutil.copy(f, 'D:/CapSyslog/')

    print('Capture is Finished, please close the program and open the reader to analyse')
    with open("D:/CapSyslog/firstcapturedpackets.txt", "r") as file:
        for last_line in file:
            pass
    words = []
    words = last_line.split(' ')

    while ('' in words):
        words.remove('')
    return words[0]

def OpenTshark_Ethernet():
    file = open("C:/Program Files/Wireshark/A.txt", 'w')  # 'w' mode will erase all the text in the file when it's opened by the program
    file.write("Capture time:10 \n")  # Write the Capture time to the txt file so that the reading will know how long does the capture last
    file.close()
    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -i Ethernet -w firstcapturedpackets.pcap -F pcap -a duration:10')
    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r firstcapturedpackets.pcap -t ad > firstcapturedpackets.txt')
    fin = open("C:/Program Files/Wireshark/firstcapturedpackets.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open("C:/Program Files/Wireshark/A.txt", "a")
    fout.write(data2)
    fout.close()
    files = ['C:/Program Files/Wireshark/A.txt', 'C:/Program Files/Wireshark/firstcapturedpackets.pcap','C:/Program Files/Wireshark/firstcapturedpackets.txt']
    for f in files:
        shutil.copy(f, 'D:/CapSyslog/')
    print('Capture is Finished, please close the program and open the reader to analyse')
    with open("D:/CapSyslog/firstcapturedpackets.txt", "r") as file:
        # first_line = file.readline()
        for last_line in file:
            pass
    words = []
    words = last_line.split(' ')

    while ('' in words):
        words.remove('')
    return words[0]


def OpenTshark_Any(interface):
    file = open("C:/Program Files/Wireshark/A.txt", 'w')  # 'w' mode will erase all the text in the file when it's opened by the program
    file.write("Capture time:10 \n")  # Write the Capture time to the txt file so that the reading will know how long does the capture last
    file.close()
    interface_index = interface.find('Capture Interface=', 0)
    interface_index += 18
    Name_Of_Interface = ""
    Length = len(interface) - 1
    while interface_index <= Length:
        Name_Of_Interface += interface[interface_index]  # Get the name of the interface
        interface_index += 1
    command = '"pushd C:\Program Files\Wireshark" & tshark -i ' + str(Name_Of_Interface) + ' -w firstcapturedpackets.pcap -F pcap -a duration: 10'
    # Form the command
    ExecuteCMD(command)

    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r firstcapturedpackets.pcap -t ad > firstcapturedpackets.txt')
    fin = open("C:/Program Files/Wireshark/firstcapturedpackets.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open("C:/Program Files/Wireshark/A.txt", "a")
    fout.write(data2)
    fout.close()
    files = ['C:/Program Files/Wireshark/A.txt','C:/Program Files/Wireshark/firstcapturedpackets.pcap','C:/Program Files/Wireshark/firstcapturedpackets.txt']
    for f in files:
        shutil.copy(f, 'D:/CapSyslog/')
    # ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -x -i - < tshark -r "firstcapturedpackets.pcap" -t ad > "A.txt"')
    # messagebox.showinfo('Message', 'Capture is Finished, please close the program and open the reader to analyse')
    print('Capture is Finished, please close the program and open the reader to analyse')
    with open("D:/CapSyslog/firstcapturedpackets.txt", "r") as file:
        # first_line = file.readline()
        for last_line in file:
            pass
    words = []
    words = last_line.split(' ')

    while ('' in words):
        words.remove('')
    return words[0]


# Similar to the method CheckInterfaceAndCap(), but here, it take the time input by user as a parameter of the capturing methods
@eel.expose
def CheckInterfaceAndCap_Any(line, time):
    # checkfile = open("User.txt")
    # line = checkfile.readline()
    # time = Timeinput.get()
    if line == "Wi-Fi":
        capturedPackets = OpenTshark_WiFi_Any(time)
        # checkfile.close()
        return capturedPackets
    if line == "Ethernet":
        capturedPackets = OpenTshark_Ethernet_Any(time)
        # checkfile.close()
        return capturedPackets
    else:
        capturedPackets = OpenTshark_Any_Any(line, time)
        # checkfile.close()
        return capturedPackets

# Similar to the Capturing methods above but here it takes time_Cap as the parameter
def OpenTshark_WiFi_Any(time_Cap):
    file = open("C:/Program Files/Wireshark/A.txt", 'w')
    Text = "Capture time:" + str(time_Cap)
    file.write(Text + ' \n')
    file.close()
    command = '"pushd C:\Program Files\Wireshark" & tshark -i WiFi -w firstcapturedpackets.pcap -F pcap -a duration:' + str(time_Cap)
    ExecuteCMD(command)
    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r firstcapturedpackets.pcap -t ad > firstcapturedpackets.txt')
    # ExecuteCMD('"pushd C:\Program Files\Wireshark" & tail -c +25 firstcapturedpackets.txt >> A.txt')
    fin = open("C:/Program Files/Wireshark/firstcapturedpackets.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open("C:/Program Files/Wireshark/A.txt", "a")
    fout.write(data2)
    fout.close()
    files = ['C:/Program Files/Wireshark/A.txt', 'C:/Program Files/Wireshark/firstcapturedpackets.pcap','C:/Program Files/Wireshark/firstcapturedpackets.txt']
    for f in files:
        shutil.copy(f, 'D:/CapSyslog/')
    # ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r "firstcapturedpackets.pcap" -t ad > "firstcapturedpackets.txt"')
    # messagebox.showinfo('Message', 'Capture is Finished, please close the program and open the reader to analyse')
    print('Capture is Finished, please close the program and open the reader to analyse')
    with open("D:/CapSyslog/firstcapturedpackets.txt", "r") as file:
        # first_line = file.readline()
        for last_line in file:
            pass
    words = []
    words = last_line.split(' ')

    while ('' in words):
        words.remove('')
    return words[0]

def OpenTshark_Ethernet_Any(time_Cap):
    file = open("C:/Program Files/Wireshark/A.txt", 'w')
    Text = "Capture time:" + str(time_Cap)
    file.write(Text + ' \n')
    file.close()
    command = '"pushd C:\Program Files\Wireshark" & tshark -i Ethernet -w firstcapturedpackets.pcap -F pcap -a duration:' + str(time_Cap)
    ExecuteCMD(command)
    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r firstcapturedpackets.pcap -t ad > firstcapturedpackets.txt')
    # ExecuteCMD('"pushd C:\Program Files\Wireshark" & tail -c +25 firstcapturedpackets.txt >> A.txt')
    fin = open("C:/Program Files/Wireshark/firstcapturedpackets.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open("C:/Program Files/Wireshark/A.txt", "a")
    fout.write(data2)
    fout.close()
    files = ['C:/Program Files/Wireshark/A.txt', 'C:/Program Files/Wireshark/firstcapturedpackets.pcap','C:/Program Files/Wireshark/firstcapturedpackets.txt']
    for f in files:
        shutil.copy(f, 'D:/CapSyslog/')
    # ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r "firstcapturedpackets.pcap" -t ad > "A.txt"')
    # messagebox.showinfo('Message', 'Capture is Finished, please close the program and open the reader to analyse')
    print('Capture is Finished, please close the program and open the reader to analyse')
    with open("D:/CapSyslog/firstcapturedpackets.txt", "r") as file:
        # first_line = file.readline()
        for last_line in file:
            pass
    words = []
    words = last_line.split(' ')

    while ('' in words):
        words.remove('')
    return words[0]

def OpenTshark_Any_Any(interface, time_Cap):
    file = open("C:/Program Files/Wireshark/A.txt", 'w')
    Text = "Capture time:" + str(time_Cap)
    file.write(Text + ' \n')
    file.close()
    interface_index = interface.find('Capture Interface=', 0)
    interface_index += 18
    Name_Of_Interface = ""
    Length = len(interface) - 1
    while interface_index <= Length:
        Name_Of_Interface += interface[interface_index]
        interface_index += 1
    command = '"pushd C:\Program Files\Wireshark" & tshark -i ' + str(Name_Of_Interface) + ' -w firstcapturedpackets.pcap -F pcap -a duration:' + str(time_Cap)
    ExecuteCMD(command)
    ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -r firstcapturedpackets.pcap -t ad > firstcapturedpackets.txt')
    # ExecuteCMD('"pushd C:\Program Files\Wireshark" & tail -c +25 firstcapturedpackets.txt >> A.txt')
    fin = open("C:/Program Files/Wireshark/firstcapturedpackets.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open("C:/Program Files/Wireshark/A.txt", "a")
    fout.write(data2)
    fout.close()
    files = ['C:/Program Files/Wireshark/A.txt','C:/Program Files/Wireshark/firstcapturedpackets.pcap','C:/Program Files/Wireshark/firstcapturedpackets.txt']
    for f in files:
        shutil.copy(f, 'D:/CapSyslog/')

    # message.showinfo('Message', 'Capture is Finished, please close the program and open the reader to analyse')
    print('Capture is Finished, please close the program and open the reader to analyse')
    with open("D:/CapSyslog/firstcapturedpackets.txt", "r") as file:
        # first_line = file.readline()
        for last_line in file:
            pass
    words = []
    words = last_line.split(' ')

    while ('' in words):
        words.remove('')
    return words[0]

# This function is used to execute the command by using CMD
def ExecuteCMD(command):
    os.system(command)

@eel.expose
def reader():
    report = Reading()
    return report

eel.start('index.html')
