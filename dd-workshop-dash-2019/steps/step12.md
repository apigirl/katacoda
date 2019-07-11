You can find our complete solution in the `/workspace/solution` folder.

- See the `/workspace/solution/github_repo/manifest.json` file.
- See the `/workspace/solution/github_repo/metadata.csv` file.
- See the `/workspace/solution/github_repo/assets/service_checks.json` file.
- See the `/workspace/solution/github_repo/README.md` file.

# Build

To build and install the integration, run the following commands:
1. `cd github_repo && python setup.py bdist_wheel` to build the integration wheel.
2. `sudo -u dd-agent datadog-agent integration install -w dist/datadog_github_repo-0.0.1-py2-none-any.whl` to install the integration.
3. `cp /etc/datadog-agent/conf.d/github_repo/conf.yaml.example /etc/datadog-agent/conf.d/github_repo/conf.yaml` then edit the `conf.yaml` with your Github access token and repository name.
4. `sudo service datadog-agent restart` to restart the agent
5. `sudo datadog-agent status` to see if your integration is running correctly
6. `sudo -u dd-agent -- datadog-agent check github_repo` to run the check and see metrics submitted.
7. Log in to your Datadog account.
8. Go to the metrics explorer and check that you are receiving the `github_repo.contributors` metrics.
9. Create a new dashboard and display all metrics submitted.