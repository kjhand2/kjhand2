#!/usr/bin/python2.7
import dpkt
import sys
from collections import defaultdict

d=defaultdict(list)


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
print(tcp.flags)
	# syn_flag = ( tcp.flags & dpkt.tcp.TH_SYN )# | (dpkt.udp.flags(buf) & dpkt.udp.TH_SYN)
	# ack_flag = ( tcp.flags & dpkt.tcp.TH_ACK )# | (dpkt.udp.flags(buf) & dpkt.udp.TH_ACK)
