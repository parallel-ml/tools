from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key
from util import ssh_client_output
import os
import subprocess
import ConfigParser

HOME = os.environ['HOME']

# find all available hosts
hosts = []
with open("ip", "r") as f:
    for line in f:
        hosts.append(line.rstrip())

# ssh commands
pkey = load_private_key(HOME + '/.ssh/id_rsa_pis')
client = ParallelSSHClient(hosts, user='pi', pkey=pkey)

# terminate the running program by soft terminate signal
output = client.run_command('kill -15 "$(pgrep python)"')
ssh_client_output(output)

config = ConfigParser.ConfigParser()
config.read('node.ckg')

for n in range(1, int(config.get('Node Config', 'system', 1)) + 1):
    node_id = 'n' + str(n)
    ip = config.get('Node IP', node_id, 0)
    subprocess.Popen(['scp', '-i', 'pi@' + ip + ':/home/pi/stats', HOME + node_id])
