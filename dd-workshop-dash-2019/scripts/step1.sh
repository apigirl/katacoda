#!/usr/bin/env bash

echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config

echo "Cloning the workshop repository..." | wall -n
mkdir /workshop && cd /workshop
git clone -q git@github.com:gzussa/katacoda.git

git clone -q git@github.com:gzussa/integrations-extras.git /integrations-extras
cd /integrations-extras && cd /integrations-extras
git checkout gzu/gr

echo "Creating workspaces..." | wall -n

mkdir /workspace && cd /workspace
mkdir /workspace/solution

echo "Cloning the integrations-extras repository..." | wall -n
git clone -q git@github.com:DataDog/integrations-extras.git /workspace/integration-extras

echo "Setup a python3 virtual environment..." | wall -n
cd /workspace/integration-extras
virtualenv venv -p python3
source venv/bin/active

#echo "Install and configure the datadog-check-dev cli..." | wall -n
#pip install "datadog-checks-dev[cli]"
#ddev config set extras "/workspace/integrations-extras"
#ddev config set repo extras


