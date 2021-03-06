from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key
import os
from util import ssh_client_output
from constants import IP_PATH, NODE_CONFIG

HOME = os.environ['HOME']

# loop through all hosts
hosts = []
with open(IP_PATH, "r") as f:
    for line in f:
        hosts.append(line.rstrip())

# load ssh private key
pkey = load_private_key(HOME + '/.ssh/id_rsa_pis')
client = ParallelSSHClient(hosts, user='pi', pkey=pkey)

# execute commands to Pis
output = client.run_command('chmod -R 777 $HOME/automate | rm -rf $HOME/automate')
ssh_client_output(output)

output = client.run_command('git clone https://github.com/parallel-ml/tools.git $HOME/automate/tools')
ssh_client_output(output)

output = client.run_command('bash $HOME/automate/tools/scripts/setup.sh')
ssh_client_output(output)
