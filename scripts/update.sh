#!/usr/bin/env bash
# clean
chmod -R 777 $HOME/conv | rm -rf $HOME/conv
chmod -R 777 $HOME/stats | rm -rf $HOME/stats

# create fresh dir
mkdir $HOME/stats

# clone new code, start the system and stop
git clone https://github.com/jiashenC/conv.git $HOME/conv
