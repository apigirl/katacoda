import logging

import pytest

from datadog_checks.base import ConfigurationError
from datadog_checks.github_repo import GithubRepoCheck

log = logging.getLogger('test_github_repo')


def test_check_invalid_configs(instance):
    # Test missing access_token
    with pytest.raises(ConfigurationError):
        GithubRepoCheck('github_repo', {}, {})

    # Test missing repository_name
    check = GithubRepoCheck('github_repo', {'access_token': "foo"}, {})
    with pytest.raises(ConfigurationError):
        check.check({})

    # Test invalid access_token
    check = GithubRepoCheck('github_repo', {'access_token': "invalid"}, {})
    with pytest.raises(ConfigurationError):
        check.check({"repository_name": "bar"})

    check = GithubRepoCheck('github_repo', {'access_token': "<YOUR_ACCESS_TOKEN>"}, {})
    check.check(instance)


def test_check_service_checks(instance, aggregator):
    check = GithubRepoCheck('github_repo', {'access_token': "foo"}, {})
    with pytest.raises(ConfigurationError):
        check.check({"repository_name": "bar"})

    sc = aggregator.service_checks(GithubRepoCheck.SERVICE_CHECK_NAME)
    assert sc[0].status == check.CRITICAL

    check = GithubRepoCheck('github_repo', {'access_token': "<YOUR_ACCESS_TOKEN>"}, {})
    check.check(instance)
    assert sc[0].status == check.OK
