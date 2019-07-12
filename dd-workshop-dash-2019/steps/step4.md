You can find our solution in the `/workspace/solution` folder.

# Create the integration 

Run the following command `ddev create "Github Repo"`{{execute}} and provide the requested information.

# Dependency

Add the `PyGitHub` dependency to the `github_repo/requirements.in` file.

# Check

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file with the following code:

![github_repo.py](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/github_repo-1.png)

# Test

Edit the `github_repo/tests/test_github_repo.py` file with the following code:

![test_github_repo-1.py](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/test_github_repo-1.png)

__NOTES:__

- The `test_check` takes a parameter called `instance` as an argument. This parameter is defined in `github_repo/tests/conftest.py`.

To run tests, execute the following command `ddev test github_repo -dv`{{execute}}.