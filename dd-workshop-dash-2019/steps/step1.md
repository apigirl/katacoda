# Setup
Before to get started, wait for the setup script to finish.
The setup script prints this message in the terminal when the setup is complete:

```
Your workspace setup is done! Enjoy the workshop :)
```

The setup script did the following things for you:
1. Clone the community-driven integration repository into the workspace directory:
  - `git clone git@github.com:DataDog/integrations-extras.git /workspace/integration-extras`

2. Setup a python virtual environment
  - `virtualenv venv -p python2`
  - `source venv/bin/activate`

3. Install and configure the Datadog CLI
  - `pip install "datadog-checks-dev[cli]"`
  - `ddev config set extras "/workspace/integrations-extras"`
  - `ddev config set repo extras`

# Getting started

Make sure that your terminal is in the correct folder and that your virtual environment is activated. 
To do so run the following commands:
- `cd /workspace/integration-extras/`{{execute}}
- `source venv/bin/activate`{{execute}}
    
Now that you are fully set up, you can start your first assignments.

# Goals
1. [Create a Github Access Token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
2. Log in to your Datadog account and install the agent
  - [Installation Instructions](https://app.datadoghq.com/account/settings#agent/ubuntu)
  - [Check that you can see your instance running](https://app.datadoghq.com/infrastructure)
3. In your terminal and using python CLI, install `PyGithub` and write a script to return `Datadog/integrations-extras` repository name.

