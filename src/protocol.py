import pandas as pd
import plotly
from collections import OrderedDict
import numpy as np
seconds = []

file=open('D:/CapSyslog/firstcapturedpackets.txt')
line=file.readline()
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

seconds,type_names = pd.factorize(seconds)
print(type_names)
seconds = seconds.tolist()
# print(seconds)

# countPacketsInSeconds = []
countPacketsInSeconds =  [(el, seconds.count(el)) for el in seconds]
unique_list = []

# traverse for all elements
for x in countPacketsInSeconds:
    # check if exists in unique_list or not
    if x not in unique_list:
        unique_list.append(x)
        # print list
for x in unique_list:
    print(x)

xData=[]
yData=[]
for ip, count in unique_list:
    xData.append(ip)
    yData.append(count)

plotly.offline.plot({"data":[plotly.graph_objs.Scatter(x=xData, y=yData)], "layout":plotly.graph_objs.Layout(title="IO Graph", xaxis=dict(title="Seconds"), yaxis=dict(title="No. of Packets"))},image='jpeg', image_filename='iograph')