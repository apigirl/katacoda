Congratulations, your integration can now be parametrized!

It will also raise errors if things go wrong.

Let's add service check to notify Datadog when the integration is not working.

# Goals

- Submit a `github_repo.up` service check.
  - Submit `OK` state when everything is working as expected.
  - Submit `WARNING` state when Github API rate limit has been exceeded (`RateLimitExceededException` exception).
  - Submit `CRITICAL` state on any other issues.
- Add a unit test to make sure your service check is submitted.

# Hints

- Use the [aggregator stub](https://github.com/DataDog/integrations-core/blob/master/datadog_checks_base/datadog_checks/base/stubs/aggregator.py) to test service check submission.
- Check out the [integrations core Github repo](https://github.com/DataDog/integrations-core) for examples of existing integrations.
