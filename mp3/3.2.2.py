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


f = open(filename, "rb")
pcap = dpkt.pcap.Reader(f)


for ts, buf in pcap:
#	print(1)
	try:
		eth = dpkt.ethernet.Ethernet(buf)
	except dpkt.dpkt.UnpackError:
		continue
	if(len(buf) != 0):
#		print(2)
		if(isinstance(eth.data, dpkt.ip.IP)):
			ip = eth.data
#			print(3)
			if(isinstance(ip.data, dpkt.tcp.TCP)):
				tcp = ip.data
#				print(4)
#				print(tcp.flags & dpkt.tcp.TH_ACK)
				# sys.exit(1)
				# test for ACK-SYN
				if (tcp.flags & dpkt.tcp.TH_ACK) != 0 and (tcp.flags & dpkt.tcp.TH_SYN) != 0:
#					print ("made it to ack")
					if ip.dst not in s_a:
						s_a[ip.dst] = 0
#						if ip.dst not in ip_list:
#							ip_list.append(ip.dst)
					else:
						s_a[ip.dst] += 1
			# add a zero if we find a ack-syn before a syn
#					if ip.dst not in s:
#						s[ip.dst] = 0
			# test for SYN
				elif (tcp.flags & dpkt.tcp.TH_SYN) != 0:
#					print ("made it to syn")
					if ip.src not in s:
						s[ip.src] = 0
#						if ip.src not in ip_list:
#							ip_list.append(ip.src)
					else:
						s[ip.src] += 1
			# add a zero if we find a syn before a ack-syn
#					if ip.dst not in s_a:
#						s_a[ip.src] = 0

# #run through list to find the IP address that works
#x=0
for c_IP in s:

	if c_IP not in s_a:
		print socket.inet_ntoa(c_IP)
	elif s[c_IP] > 3*s_a[c_IP]:
 		print socket.inet_ntoa(c_IP)
# 		print socket.inet_ntoa(ip_list2[x])
# 	x=x+1



f.close()

# #	if (tcp not in d):
# #		d.append(tcp)

# #	print(tcp.TH_ACK)
# #	print("End of packet")

# 	# syn_flag = ( tcp.flags & dpkt.tcp.TH_SYN )# | (dpkt.udp.flags(buf) & dpkt.udp.TH_SYN)
# 	# ack_flag = ( tcp.flags & dpkt.tcp.TH_ACK )# | (dpkt.udp.flags(buf) & dpkt.udp.TH_ACK)
