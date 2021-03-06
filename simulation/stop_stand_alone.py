from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key
from util import ssh_client_output
import os
import subprocess
import ConfigParser
from time import strftime, localtime
import time
from constants import IP_PATH, NODE_CONFIG

HOME = os.environ['HOME']

# find all available hosts
hosts = []
with open(IP_PATH, "r") as f:
    for line in f:
        hosts.append(line.rstrip())

# ssh commands
pkey = load_private_key(HOME + '/.ssh/id_rsa_pis')
client = ParallelSSHClient(hosts, user='pi', pkey=pkey)

# terminate the running program by soft terminate signal
output = client.run_command('kill -15 "$(pgrep python)"')
ssh_client_output(output)

config = ConfigParser.ConfigParser()
config.read(NODE_CONFIG)

dir_name = '/' + strftime("%Y-%m-%d %H:%M:%S", localtime()) + '/'
subprocess.Popen(['mkdir', HOME + '/stats' + dir_name])

for n in range(1, len(list(config.items('Node IP'))) + 1):
    node_id = 'n' + str(n)
    ip = config.get('Node IP', node_id, 0)
    subprocess.Popen(
        ['scp', '-i', HOME + '/.ssh/id_rsa_pis', 'pi@' + ip + ':/home/pi/stats', HOME + '/stats' + dir_name + node_id])

# terminate the running program by soft terminate signal
output = client.run_command('kill -9 "$(pgrep python)"')
ssh_client_output(output)

time.sleep(5)

# clean stats from last time
output = client.run_command('rm $HOME/stats')
ssh_client_output(output)
