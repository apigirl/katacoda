# Setup

Run the following commands to get started:
1. Clone the community driven integration repository:
  - `git clone git@github.com:DataDog/integrations-extras.git`
  - `cd integration-extras`
2. Setup a python virtual environment
  - `virtualenv venv -p python3`
  - `source venv/bin/active`
3. Install and configure the Datadog CLI
  - `pip install "datadog-checks-dev[cli]"`
  - `ddev config set extras "/root/dd/integrations-extras"`
  - `ddev config set repo extras`
4. [Create a Github Access Token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
5. Log in to your Datadog account and install the agent
  - [Installation Instructions](https://app.datadoghq.com/account/settings#agent/ubuntu)
  - [Check that you can see your instance running](https://app.datadoghq.com/infrastructure)

# Goals

- Read the "Github Repo" integration Specification
- Using the Python CLI, use `PyGithub` to print the `integrations-extras` repo fullname

