You can find our solution in the `/workspace/solution` folder.

# Check 

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file and submit metrics collected as follow:

![github_repo-7](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/github_repo-7.png)

# Test

Create a new python file called `test_end_to_end.py` into `github_repo/tests/` to separate tests.

Below is a example on how we mocked `PyGithub` methods to test the integration. There are plenty of different ways to do this.

![test_github_repo-4](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/test_github_repo-4.png)

__NOTES:__
- Replace `<YOUR_ACCESS_TOKEN>` with your Github Access Token.
- The `aggregator` stub is created by default and can be used to assert what is being submitted by the check method.
- We use the `mock.patch` annotation to mock `PyGithub` methods.
- We call the `assert_all_metrics_covered()` method to make sure we asserted all metrics submitted.