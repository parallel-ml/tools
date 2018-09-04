from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key
from util import ssh_client_output
import argparse
import os
from ConfigParser import RawConfigParser

# parse command line argument to adapt to different systems
parser = argparse.ArgumentParser(description='Configuration for distributed system.')
parser.add_argument('model', help='This argument specifies the eep learning model for the system. E.g, alexnet. ')
parser.add_argument('system', help='This argument specifies the system setting. E.g, node_8. ')
parser.add_argument('-u', '--update', help='This argument specifies whether to update code on host device or not. '
                                           'The value is default to False, but it should be True if the device is '
                                           'running for the first time. ', default=False)
args = parser.parse_args()

HOME, CUR = os.environ['HOME'], os.environ['PWD']
MODEL, SYSTEM = args.model, args.system
config_candidates = {
    'test_2': 2,
    'alexnet_7': 7,
}

# python config file parser
config_parser = RawConfigParser()

# find all available hosts
hosts = []
with open("ip", "r") as f:
    for line in f:
        hosts.append(line.rstrip())

# check if config is valid
cfg = MODEL + '_' + SYSTEM
if cfg not in config_candidates:
    raise BaseException('The program cannot find appropriate system setting with the model chosen.')
if len(hosts) < config_candidates[cfg]:
    raise BaseException('The system does not have enough devices. ')

config_parser.add_section('Node Config')
config_parser.set('Node Config', 'system', SYSTEM)
config_parser.set('Node Config', 'model', MODEL)

# map node to ip
node_ip_mapping = dict()
for n in range(1, config_candidates[cfg] + 1):
    node_ip_mapping.update({'n' + str(n): hosts[n - 1]})

# write ip to node mapping to config file
config_parser.add_section('Node IP')
config_parser.add_section('IP Node')
for node, ip in node_ip_mapping.items():
    config_parser.set('IP Node', ip, node)
    config_parser.set('Node IP', node, ip)
with open('node.cfg', 'wb') as configfile:
    config_parser.write(configfile)
hosts = node_ip_mapping.values()

# ssh commands
pkey = load_private_key(HOME + '/.ssh/id_rsa_pis')
client = ParallelSSHClient(hosts, user='pi', pkey=pkey)

# put node config
client.copy_file('node.cfg', 'node.cfg')

if args.update:
    output = client.run_command('bash $HOME/automate/tools/scripts/update.sh')
    ssh_client_output(output)

server_hosts = ParallelSSHClient(hosts[1:], user='pi', pkey=pkey)
server_hosts.run_command('bash $HOME/automate/tools/scripts/run_system server')

client_hosts = ParallelSSHClient(hosts[:1], user='pi', pkey=pkey)
server_hosts.run_command('bash $HOME/automate/tools/scripts/run_system')
