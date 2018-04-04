#!/bin/python


# BASH Version: $ pssh -t 10 -h ips -l pi -A -i "uptime"


from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key

hosts = []
with open("ips", "r") as f:
  for line in f:
    hosts.append(line.rstrip())

print(hosts)

pkey = load_private_key('/Users/ramyadhadidi/.ssh/id_rsa_pis')

client = ParallelSSHClient(hosts, user='pi', pkey=pkey)
output = client.run_command('ls')


for host, host_output in output.items(): 
    for line in host_output.stdout:
        print("Host [%s] - %s" % (host, line))

'''
for host, host_output in output.items():
    print(host)
    for line in host_output.stdout:
        print(line)
    print
'''
