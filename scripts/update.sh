#!/usr/bin/env bash
# clean
if [ -d "$HOME/conv" ]; then
    rm -rf $HOME/conv
fi

# clone new code, start the system and stop
git clone https://github.com/parallel-ml/conv.git $HOME/conv

if [ -d "$HOME/stand-alone" ]; then
    rm -rf $HOME/stand-alone
fi
git clone https://github.com/parallel-ml/stand-alone.git $HOME/stand-alone

if [ -d "$HOME/model-specific" ]; then
    rm -rf $HOME/model-specific
fi
git clone https://github.com/parallel-ml/model-specific.git $HOME/model-specific

