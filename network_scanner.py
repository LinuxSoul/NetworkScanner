#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_request = broadcast/arp_request
    ans_list = scapy.srp(final_request, timeout=1, verbose=False)[0]
    print("IP\t\t\tMAC ADDRESS\n---------------------------------------------")

    for element in ans_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


scan("192.168.43.1/24")
