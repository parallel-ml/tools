#!/usr/bin/env bash
# clean
if [ -d "$HOME/conv" ]; then
    rm -rf $HOME/conv
fi

# clone new code, start the system and stop
git clone https://github.com/parallel-ml/conv.git $HOME/conv
