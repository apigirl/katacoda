import logging

import pytest

from datadog_checks.base import ConfigurationError
from datadog_checks.github_repo import GithubRepoCheck

log = logging.getLogger('test_github_repo')


def test_check_invalid_configs(instance):
    with pytest.raises(ConfigurationError):
        GithubRepoCheck('github_repo', {}, {})

    check = GithubRepoCheck('github_repo', {'access_token': "foo"}, {})
    with pytest.raises(ConfigurationError):
        check.check({"repository_name": "bar"})

    check = GithubRepoCheck('github_repo', {'access_token': "foo"}, {})
    with pytest.raises(ConfigurationError):
        check.check({})

    check = GithubRepoCheck('github_repo', {'access_token': "foo"}, {})
    with pytest.raises(ConfigurationError):
        check.check({"repository_name": "bar"})

    # check = GithubRepoCheck('github_repo', {'access_token': "<YOUR_TOKEN>"}, {})
    # check.check(instance)
