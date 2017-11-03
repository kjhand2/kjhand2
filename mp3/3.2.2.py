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

ip_list = []
ip_list2 = []

if (len(sys.argv) < 2):
	print "error: need argument"
	sys.exit(1)

filename = sys.argv[1]


f = open(filename)
pcap = dpkt.pcap.Reader(f)



for ts, buf in pcap:
	if(buf != 0):
		eth = dpkt.ethernet.Ethernet(buf)
	if(eth != 0):
		ip = eth.data
	if(ip != 0):
		tcp = ip.data
	if type(tcp) == UDP:
		break
#	test for ACK-SYN
	if (tcp.flags & dpkt.tcp.TH_ACK) != 0 and (tcp.flags & dpkt.tcp.TH_SYN) != 0:
		print ("made it to ack")
		if ip.dst not in s_a:
			s_a[ip.dst] = 1
		else:
			s_a[ip.dst] += 1
# add a zero if we find a ack-syn before a syn
		if ip.dst not in s:
			s[ip.dst] = 0
# test for SYN
	elif (tcp.flags & dpkt.tcp.TH_SYN) != 0:
		print ("made it to syn")
		if ip.dst not in s:
			s[ip.dst] = 1
		else:
			s[ip.dst] += 1
# add a zero if we find a syn before a ack-syn
		if ip.dst not in s_a:
			s_a[ip.dst] = 0
#append ip addresses to ip_lists for each iteration
	if ip.dst not in ip_list:
		ip_list.append(ip.dst)
		ip_list2.append(ip.src)
#run through list to find the IP address that works
x=0
for c_IP in ip_list:
	if s[c_IP] > 3*s_a[c_IP]:
		print socket.inet_ntoa(c_IP)
		print socket.inet_ntoa(ip_list2[x])
	x=x+1



f.close()

#	if (tcp not in d):
#		d.append(tcp)

#	print(tcp.TH_ACK)
#	print("End of packet")

	# syn_flag = ( tcp.flags & dpkt.tcp.TH_SYN )# | (dpkt.udp.flags(buf) & dpkt.udp.TH_SYN)
	# ack_flag = ( tcp.flags & dpkt.tcp.TH_ACK )# | (dpkt.udp.flags(buf) & dpkt.udp.TH_ACK)
