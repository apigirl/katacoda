#!/usr/bin/env bash



echo "Cloning the workshop repository..."
mkdir /workshop
git clone git@github.com:gzussa/katacoda.git /workshop/

git clone git@github.com:gzussa/integrations-extras.git /integrations-extras
cd /integrations-extras
git checkout gzu/gr

echo "Creating workspaces..."

mkdir /workspace && cd /workspace
mkdir solution

echo "Cloning the integrations-extras repository..."
git clone git@github.com:DataDog/integrations-extras.git /workspace/integrations-extras
cd integration-extras

echo "Setup a python3 virtual environment..."
virtualenv venv -p python3
source venv/bin/active

echo "Install and configure the datadog-check-dev cli..."
pip install "datadog-checks-dev[cli]"
ddev config set extras "/workspace/integrations-extras"
ddev config set repo extras


