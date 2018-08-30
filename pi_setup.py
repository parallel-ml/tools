from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key
import os
from util import ssh_client_output

HOME = os.environ['HOME']

hosts = []
with open("ip", "r") as f:
    for line in f:
        hosts.append(line.rstrip())

pkey = load_private_key(HOME + '/.ssh/id_rsa_pis')
client = ParallelSSHClient(hosts, user='pi', pkey=pkey)
output = client.run_command('git clone https://github.com/parallel-ml/tools.git $HOME/automate')
ssh_client_output(output)

output = client.run_command('bash $HOME/automate/tools/scripts/setup.sh')
ssh_client_output(output)

