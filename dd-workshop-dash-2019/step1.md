

# Getting Started

## Setup
Run the following commands to get started:
- `git clone git@github.com:DataDog/integrations-extras.git`
- `cd integration-extras`
- `virtualenv venv3 -p python3`
- `source venv3/bin/active`
- `pip install "datadog-checks-dev[cli]"`
- `ddev config set extras "/root/dd/integrations-extras"`
- `ddev config set repo extras`

At this point, you cloned the integartion-extras repository, created a python virtual environment, install the datadog cli and configured it.

Before we get into coding an integration we need to understand what we want to develop.
Usually you would write a specification. In this case we created one for you and you will have to implement it.


## Goals
- Read the specification document
- [Create a Github access token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
- Using Python CLI, use `PyGithub` to print the `integrations-extras` repo fullname

## References
- [How to create an integration](https://docs.datadoghq.com/developers/integrations/new_check_howto/)
