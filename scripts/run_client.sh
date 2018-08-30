#!/usr/bin/env bash
# create fresh dir
mkdir $HOME/node
mkdir $HOME/stats

# clone new code, start the system and stop
git clone https://github.com/jiashenC/conv.git $HOME
cd $HOME/conv && python -m system.client > $HOME/stats/"$(hostname)"
sleep 300
pgrep python | xargs kill

# clean
chmod -R 777 $HOME/conv
rm -rf $HOME/conv