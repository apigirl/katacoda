#!/usr/bin/env bash

echo "Clean the solution folder..." | wall -n
rm -rf /workspace/solution/*
cp -r /workshop/katacoda/dd-workshop-dash-2019/solutions/5-packaging/github_repo /workspace/solution/
