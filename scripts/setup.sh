#!/usr/bin/env bash
if [ -d "$HOME/automate" ]; then
   rm -rf $HOME/automate
   git clone https://github.com/parallel-ml/tools.git $HOME/automate/tools
fi

