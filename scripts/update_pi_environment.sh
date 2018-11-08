#!/usr/bin/env bash

sudo pip uninstall -y tensorflow
sudo pip install --upgrade https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.5.0/tensorflow-1.5.0-cp27-none-linux_armv7l.whl
sudo pip install -r $HOME/automate/tools/config/requirements.txt
