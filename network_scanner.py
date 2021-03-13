#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(psdt=ip)
    print(arp_request.summary())


scan("192.168.43.1/24")
