You can find our solution in the `/workspace/solution` folder.

# Edit Configuration file

Edit the `github_repo/datadog_checks/github_repo/data/conf.yaml.example` file with the following content.

![conf.yaml.example](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/conf_yaml_example.png)

# Init

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file.  
- Add an `__init__` method to retrieve your `access_token` from the `init_config` section of your configuration.
- Check the `access_token` is set properly otherwise raise a `ConfigurationError` error.

![github_repo-2](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/github_repo-2.png)

# Check

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file. 
- Similarly to what you did in the `__init__` method, fetch and validate the `repository_name` parameter.

![github_repo-3](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/github_repo-3.png)

- Use both parameter in your logic. Catch exceptions that may be raised by the `PyGithub` library.

![github_repo-4](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/github_repo-4.png)

We created the following method to avoid code duplication.

![github_repo-5](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/github_repo-5.png)

# Test

Edit the `github_repo/tests/test_github_repo.py` file with the following code.

![test_github_repo-2](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/test_github_repo-2.png)

__NOTES:__ 
- Replace `<YOUR_ACCESS_TOKEN>` with your Github Access Token.


We are using the `instance` parameter in the test method `def test_check_invalid_configs(instance):`
As a consequence, you need to set the `repository_name` parameter for that instance.

Edit the `github_repo/tests/conftest.py` file with the following code.

![conftest](https://raw.githubusercontent.com/gzussa/katacoda/master/dd-workshop-dash-2019/assets/conftest.png)
