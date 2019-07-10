#!/usr/bin/env bash

echo "Clean the solution folder..." | wall -n
rm -rf /workspace/solution/*
cp -r /integrations-extra/github_repo /workspace/solution/
