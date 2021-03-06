from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key
from util import ssh_client_output
import os
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

output = client.run_command('bash $HOME/automate/tools/scripts/update_pi_environment.sh')
ssh_client_output(output)
