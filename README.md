# Scripts & SSH Tools
This repos is built for easier code update on IoT devices connected to the same domain. 

## Installation
**Python >= 2.7**
```bash
pip install -r requirements.txt
```
## Credentials
Set up SSH private key under `$HOME/.ssh/id_rsa_pis`

## How To Use
Collect all devices IP addresses.
```bash
./scripts/find_ip
```
Run Raspberry Pi setup through Python client.
```bash
python pi_setup.py
```