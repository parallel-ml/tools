#!/bin/bash

MACAddress=""
MACAddress="${MACAddress}B8:27:EB:80:49:FC"
#MACAddress="${MACAddress}|"

sudo nmap -sP 192.168.1.0/24 | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | grep -i -E $MACAddress | sed -r 's:^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*:\1:g' | sort -V | tee $PWD/ip

echo "Total Numbers:"
wc -l $PWD/ip
