#!/usr/bin/env bash
# start server and waits a few time
# if argument provided, then start the server
if [[ -n $1 ]]; then
    cd $HOME/model-specific && python server.py
else
    cd $HOME/model-specific && python client.py
fi
