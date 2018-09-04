#!/usr/bin/env bash
# clean
rm -rf $HOME/conv
rm -rf $HOME/stats

# clone new code, start the system and stop
git clone https://github.com/parallel-ml/conv.git $HOME/conv
