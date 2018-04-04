#!/bin/python


# BASH Version: $ pssh -t 5 -h ips -l pi -A -i "uptime"


from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key


def print_per_host_ip_head(output):
    for host, host_output in output.items():
        print(host)
        for line in host_output.stdout:
            print(line)
        print
    print("---------------------------------------")
    print


def print_per_host_ip_line_start(output):
    for host, host_output in output.items(): 
        for line in host_output.stdout:
            print("Host [%s] - %s" % (host, line))
    print("---------------------------------------")
    print


hosts = []
with open("ips", "r") as f:
  for line in f:
    hosts.append(line.rstrip())

print(hosts)

pkey = load_private_key('/Users/ramyadhadidi/.ssh/id_rsa_pis')

client = ParallelSSHClient(hosts, user='pi', pkey=pkey)
output = client.run_command('mkdir -p automate/parallel-ml')
output = client.run_command('cd automate/parallel-ml; pwd')
output = client.run_command('cd automate/parallel-ml; git clone https://github.com/parallel-ml/tools.git')
output = client.run_command('cd automate/parallel-ml; git clone https://github.com/parallel-ml/conv.git') 
output = client.run_command('cd automate/parallel-ml; git clone https://github.com/parallel-ml/fc.git')
output = client.run_command('cd automate/parallel-ml; git clone https://github.com/parallel-ml/robot.git')
output = client.run_command('cd automate/parallel-ml; git clone https://github.com/parallel-ml/asplos2018-workshop.git')
output = client.run_command('cd automate/parallel-ml; ls -l')
print_per_host_ip_head(output)



