#!/usr/bin/env bash
if [ -d "$HOME/automate" ]; then
   chmod -R 777 $HOME/automate
   rm -rf $HOME/automate
   git clone https://github.com/parallel-ml/tools.git $HOME/automate
fi

