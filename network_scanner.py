#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(psdt=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_request = broadcast/arp_request
    print(final_request.summary())


scan("192.168.43.1/24")
