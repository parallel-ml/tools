from pssh.pssh_client import ParallelSSHClient
from pssh.utils import load_private_key
from util import ssh_client_output
import argparse
import os
import time
from threading import Thread
from ConfigParser import RawConfigParser
from constants import IP_PATH, NODE_CONFIG

# parse command line argument to adapt to different systems
parser = argparse.ArgumentParser(description='Configuration for distributed system.')
parser.add_argument('model', help='This argument specifies the eep learning model for the system. E.g, alexnet. ')
parser.add_argument('system', help='This argument specifies the system setting. E.g, 8. ')
args = parser.parse_args()

HOME, CUR = os.environ['HOME'], os.environ['PWD']
MODEL, SYSTEM = args.model, args.system
config_candidates = {
    'test_2': 2,
    'alexnet_5': 5,
    'alexnet_6': 6,
    'alexnet_7': 7,
    'vgg16_9': 9,
    'vgg16_11': 11,
}

# python config file parser
config_parser = RawConfigParser()

# find all available hosts
hosts = []
with open(IP_PATH, "r") as f:
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
for node, ip in sorted(node_ip_mapping.items(), key=lambda x: x[0]):
    config_parser.set('IP Node', ip, node)
    config_parser.set('Node IP', node, ip)
with open(NODE_CONFIG, 'wb') as configfile:
    config_parser.write(configfile)
hosts = [pair[1] for pair in sorted(node_ip_mapping.items(), key=lambda x: x[0])]

# ssh commands
pkey = load_private_key(HOME + '/.ssh/id_rsa_pis')
client = ParallelSSHClient(hosts, user='pi', pkey=pkey)

# put node config
client.copy_file(NODE_CONFIG, 'node.cfg')


def start_server(ips):
    server_hosts = ParallelSSHClient(ips, user='pi', pkey=pkey)
    servers_outputs = server_hosts.run_command('bash $HOME/automate/tools/scripts/run_model_specific.sh server')
    ssh_client_output(servers_outputs)


def start_client(ips):
    client_host = ParallelSSHClient(ips, user='pi', pkey=pkey)
    client_outputs = client_host.run_command('bash $HOME/automate/tools/scripts/run_model_specific.sh')
    ssh_client_output(client_outputs)


client, servers = hosts[:1], hosts[1:]
for server in servers:
    Thread(target=start_server, args=([server],)).start()
time.sleep(50)
Thread(target=start_client, args=(client,)).start()

