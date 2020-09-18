from scapy.all import *
from collections import Counter
import plotly
from prettytable import PrettyTable
import time
import pandas as pd
import plotly.express as px
import eel

eel.init('Web')

@eel.expose
def Graph():
    packets = rdpcap('D:/CapSyslog/firstcapturedpackets.pcap')
    # print(packets.show())

    srcIP = []
    for pkt in packets:
        if IP in pkt:
            try:
                srcIP.append(pkt[IP].src)
            except:
                pass

    cnt = Counter()

    for ip in srcIP:
        cnt[ip] += 1

    table = PrettyTable(["IP", "Count"])
    for ip, count in cnt.most_common():
        table.add_row([ip, count])

    print(table)

    xData = []
    yData = []
    for ip, count in cnt.most_common():
        xData.append(ip)
        yData.append(count)

    # Count of protocols
    protocol = []
    for pkt in packets:
        if IP in pkt:
            try:
                protocol.append(pkt[IP].proto)
            except:
                pass
            # pkt.show()

    cntProto = Counter()

    for protoc in protocol:
        cntProto[protoc] += 1

    table1 = PrettyTable(["Protocol", "Count"])

    for protoc, count in cntProto.most_common():
        table1.add_row([protoc, count])

    print(table1)
    print("17 - UDP\n 6 - TCP\n 1 - ICMP \n 2 - IGMP")

    plotly.offline.plot({"data": [plotly.graph_objs.Bar(x=xData, y=yData)],"layout": plotly.graph_objs.Layout(title="Source IP Occurrence", xaxis=dict(title="Src IP"),yaxis=dict(title="Count"))}, filename='Web/srcIPOccurance.html',auto_open=False)
    # time.sleep(5)
    x1Data = []
    y1Data = []
    for protoc, count in cntProto.most_common():
        if protoc == 17:
            protoc = 'UDP'
        elif protoc == 6:
            protoc = 'TCP'
        elif protoc == 1:
            protoc = 'ICMP'
        else:
            protoc = 'IGMP'
        x1Data.append(protoc)
        y1Data.append(count)
    plotly.offline.plot({"data": [plotly.graph_objs.Bar(x=x1Data, y=y1Data)],
                         "layout": plotly.graph_objs.Layout(title="Frequently Occured Protocol",
                                                            xaxis=dict(title="Protocols"), yaxis=dict(title="Count"))},
                        filename='Web/frequencyProtocol.html', auto_open=False)
    # plotly.offline.plot({"data":[plotly.graph_objs.Scatter(x=x1Data, y=y1Data)], "layout":plotly.graph_objs.Layout(title="Protocol Occurrence")},image='jpeg', image_filename='test1')
    # time.sleep(5)

    seconds = []

    file = open('D:/CapSyslog/firstcapturedpackets.txt')
    line = file.readline()
    while line != '':  # Equal to While not EOF
        words = []
        time = []
        min = []
        words = line.split(' ')
        while ('' in words):
            words.remove('')
        time = words[2].split(':')
        min = time[2].split('.')
        seconds.append(min[0])
        line = file.readline()

    seconds, type_names = pd.factorize(seconds)
    print(type_names)
    seconds = seconds.tolist()
    # print(seconds)

    # countPacketsInSeconds = []
    countPacketsInSeconds = [(el, seconds.count(el)) for el in seconds]
    unique_list = []

    # traverse for all elements
    for x in countPacketsInSeconds:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    for x in unique_list:
        print(x)

    xData = []
    yData = []
    for ip, count in unique_list:
        xData.append(ip)
        yData.append(count)

    # plotly.offline.plot({"data":[plotly.graph_objs.Scatter(x=xData, y=yData)], "layout":plotly.graph_objs.Layout(title="I/O Graph", xaxis=dict(title="Seconds"), yaxis=dict(title="No. of Packets"))},image='jpeg', image_filename='iograph')
    plotly.offline.plot({"data": [plotly.graph_objs.Scatter(x=xData, y=yData)],
                         "layout": plotly.graph_objs.Layout(title="I/O Graph", xaxis=dict(title="Seconds"),
                                                            yaxis=dict(title="No. of Packets"))},
                        filename='Web/iograph.html', auto_open=False)

# eel.start('index.html')