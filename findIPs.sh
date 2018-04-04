#!/bin/bash

MACAddress=""
MACAddress="${MACAddress}B8:27:EB:5F:AD:65"
MACAddress="${MACAddress}|B8:27:EB:E1:AB:24"
MACAddress="${MACAddress}|B8:27:EB:81:9D:94"
MACAddress="${MACAddress}|B8:27:EB:5B:25:25"
MACAddress="${MACAddress}|B8:27:EB:5E:7C:C2"
MACAddress="${MACAddress}|B8:27:EB:B2:1F:18"
MACAddress="${MACAddress}|B8:27:EB:7E:5F:2A"
MACAddress="${MACAddress}|B8:27:EB:DD:34:B2"
MACAddress="${MACAddress}|B8:27:EB:BD:B6:34"
MACAddress="${MACAddress}|B8:27:EB:1A:C5:E4"
MACAddress="${MACAddress}|B8:27:EB:C8:62:3B"
MACAddress="${MACAddress}|B8:27:EB:CE:4D:28"
MACAddress="${MACAddress}|B8:27:EB:EF:71:26"
#MACAddress="${MACAddress}|"


sudo nmap -sP 192.168.1.0/24 | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | grep -i -E $MACAddress | sed -r 's:^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*:\1:g' | sort -V | tee ips 

echo "Total Numbers:"
wc -l ips
