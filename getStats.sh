#!/usr/bin/env bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

# DEBUG Commands
CURRENT_DIR=$(dirname "$0")

cd $CURRENT_DIR 

# Execute Scripts to collect statistics
$HOME/.pyenv/versions/$(cat $CURRENT_DIR/.python-version)/bin/python asl-node-stats-api.py


