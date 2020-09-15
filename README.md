MN^2 is a packet sniffing tool which captures the packet based on the specific time give by the user.
This is a windows project. This tool is developed using python. The UI is developed using tkinter.

**Characterstics of this tool**
1. Capture packets
2. Stores as pcap file as well as text file.
3. Gives the statistics based on the text file
4. Visualization is performed based on the pcap file

    4.1 Count of SrcIP
     
    4.2 Count of frequently used protocol
    
    4.3 I/O Graph (No. packets per second)

**Modules**
1. Login - SHA512 hashing is performed at the time of login.
    
    1.1 The user can change the password
    
2. Network_diagnosticer - Can capture the packets and read the packets
3. main_user_interface - It consist of an option to change the interface and bandwidth if required. And if everything is fine they can go to network_diagnosticer page.
4. Reader.py - will take the captured packet text file, read the captured packets, provide the statistics and provide the visualization for the pcap file.

  
    