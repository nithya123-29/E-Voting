touch "firstcapturedpackets.pcap"
tshark -D
# tshark -i 1
# tshark -i 1 -c 30
tshark -i 2 -a duration:10
# tshark -i 1 -c 5 -p
tshark -i 1 -w "firstcapturedpackets.pcap" -F pcap -a duration:10
# tshark -F
# tshark -i 1 -c 10 -f "tcp port 80" 
# tshark -r "firstcapturedpackets.pcap"
tshark -r "firstcapturedpackets.pcap" -z conv,ip
# tshark -i 1 -w "secondcapture.pcap" -a filesize:1
tshark -r "firstcapturedpackets.pcap" -t ad > "firstcapturedpackets.txt"
xdg-open "firstcapturedpackets.txt"
xdg-open "firstcapturedpackets.pcap"