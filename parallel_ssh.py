from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key

hosts = []
with open("ip", "r") as f:
    for line in f:
        hosts.append(line.rstrip())

pkey = load_private_key('credentials/id_rsa_pis')
client = ParallelSSHClient(hosts, user='pi', pkey=pkey)
output = client.run_command('ls')

for host, host_output in output.items():
    for line in host_output.stdout:
        print line
