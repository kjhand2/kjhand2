#!/usr/bin/python2.7
import dpkt
import socket
import sys
from collections import defaultdict
from dpkt.tcp import TH_SYN
from dpkt.tcp import TH_ACK 
from dpkt.ip import IP, IP_PROTO_UDP
from dpkt.udp import UDP
#d=defaultdict(list)
s = {}
s_a = {}

if (len(sys.argv) < 2):
	print "error: need argument"
	sys.exit(1)

filename = sys.argv[1]


f = open(filename, "rb")
pcap = dpkt.pcap.Reader(f)


for ts, buf in pcap:
	# print(1)
	try:
		eth = dpkt.ethernet.Ethernet(buf)
	except(dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
		continue
	# print(2)
	if(isinstance(eth.data, dpkt.ip.IP)):
		ip = eth.data
		# print(3)
	else:
		continue
	if(isinstance(ip.data, dpkt.tcp.TCP)):
		tcp = ip.data
		# print(4)
	else:
		continue
	# print(tcp.flags & dpkt.tcp.TH_ACK)
	# sys.exit(1)
	# test for ACK-SYN
	if ((tcp.flags & dpkt.tcp.TH_ACK) != 0 and (tcp.flags & dpkt.tcp.TH_SYN) != 0):
		# print ("made it to ack")
		if ip.dst not in s_a:
			s_a[ip.dst] = 1
		else:
			s_a[ip.dst] += 1
	# add a zero if we find a ack-syn before a syn
		if ip.dst not in s:
			s[ip.dst] = 0
			# test for SYN
	elif (tcp.flags == dpkt.tcp.TH_SYN): #!= 0:
		# print ("made it to syn")
		if ip.src not in s:
			s[ip.src] = 1
		else:
			s[ip.src] += 1
# add a zero if we find a syn before a ack-syn
		if ip.src not in s_a:
			s_a[ip.src] = 0



# #run through list to find the IP address that works
# x=0
for c_IP in s:
	# if(socket.inet_ntoa(c_IP) == "10.149.191.1"):
	# 	print(s[c_IP])
	# 	print(s_a[c_IP])
	# 	raw_input()
	if s[c_IP] > 3*s_a[c_IP]:
		print socket.inet_ntoa(c_IP)
		# print socket.inet_ntoa(ip_list2[x])
	# x=x+1
f.close()
