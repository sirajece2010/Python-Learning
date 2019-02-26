import sys,os
import re
import numpy as np
import netaddr

version = '1.0'
priv_min = ['10.0.0.0','172.16.0.0','192.168.0.0']
priv_max = ['10.255.255.255','172.31.255.255','192.168.255.255']
bin_ip = ''

def ConvertToBinary(deci):
    return bin(deci)[2:].rjust(8,'0')

def priv_range(ip_add):
    return netaddr.IPSet([ip_add])

def help():
    print('''Usage: ipcalc [-n|-h|-v|-help] <ADDRESS>[[/]<NETMASK>] [NETMASK]

ipcalc takes an IP address and netmask and calculates the resulting broadcast,
network, Cisco wildcard mask, and host range. By giving a second netmask, you
can design sub- and supernetworks. It is also intended to be a teaching tool
and presents the results as easy-to-understand binary values.

 -help Longer help text
 -v    Print Version

Examples:

ipcalc 192.168.0.1/24
ipcalc 192.168.0.1/255.255.128.0
ipcalc 192.168.0.1 255.255.128.0 255.255.192.0
ipcalc 192.168.0.1 0.0.63.255''')

if __name__ == '__main__':
    #ip = input('Enter the ip address:')
    if len(sys.argv) == 1:
        help()
        exit()
    if len(sys.argv) > 1:
        if sys.argv[1] == '-v':
            print (f'Version : {version}')
            exit()
        if sys.argv[1] == '-help':
            help()
            exit()
        if re.search('\/',sys.argv[1]):
            ip = sys.argv[1].split('/')[0]
            ip_mask = sys.argv[1].split('/')[1]
        else:
            ip = sys.argv[1]
    print(ip)
    split_ip=ip.split('.')
    split_ip = list(map(lambda x: int(x), split_ip))

    if len(split_ip) != 4:
        print("Please enter a valid IPv4 Address")
        exit()

    for oct in split_ip:
        if not (oct >= 0 and oct < 256):
            print("Entered IP {} is an Invalid IP".format(ip))
            exit()
        bin_ip += ConvertToBinary(oct)+'.'
    bin_ip = bin_ip[:-1]
    if split_ip[0] >= 0 and split_ip[0] < 128:
        ip_class = 'Class A'
        cidr = 8
    elif split_ip[0] >= 128 and split_ip[0] < 192:
        ip_class = 'Class B'
        cidr = 16
    elif split_ip[0] >= 192 and split_ip[0] < 224:
        ip_class = 'Class C'
        cidr = 24
    else:
        ip_class = 'Class D'
        cidr = 'not defined'

    print(f'Entered ip address is {ip} of {ip_class}')
    print(f'Binary ip address is {bin_ip} cidr is {cidr}')
    print (priv_range(ip))
