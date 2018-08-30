#!/usr/bin/env bash
# start server and waits a few time
# if argument provided, then start the server
if [[ -n $1 ]]; then
    cd $HOME/conv && python -m system.server > $HOME/stats/"$(hostname)"
    sleep 300
else
    cd $HOME/conv && python -m system.client > $HOME/stats/"$(hostname)"
    sleep 120
fi
pgrep python | xargs kill
