#!/usr/bin/env bash

echo "Clean the solution folder..." | wall -n
rm -rf /workspace/solution/*
cp -r /workshop/dd-workshop-dash-2019/solutions/4-metrics/github_repo /workspace/solution/
