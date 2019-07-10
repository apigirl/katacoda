from github import Github
from github.GithubException import BadCredentialsException, RateLimitExceededException, UnknownObjectException

from datadog_checks.base import AgentCheck, ConfigurationError


class GithubRepoCheck(AgentCheck):
    def __init__(self, name, init_config, agentConfig, instances=None):
        super(GithubRepoCheck, self).__init__(name, init_config, agentConfig, instances)

        # Fetch Config
        self.access_token = init_config.get('access_token')
        if not self.access_token:
            raise ConfigurationError('Configuration error, please set an access_token')

    def check(self, instance):
        repository_name = instance.get('repository_name')
        if not repository_name:
            raise ConfigurationError('Configuration error, please set a repository_name')

        tags = []

        # Get repository
        g = Github(self.access_token)

        try:
            repo = g.get_repo(repository_name)
            self.log.debug('Getting stats for: {}'.format(repo.full_name))
            tags.append("repository_name:{}".format(repository_name))

        except BadCredentialsException as e:
            self.handle_exception("Failed to authenticate to Github with given access_token", tags, e)
        except UnknownObjectException as e:
            self.handle_exception("Failed to access repository. Check your repository_name config", tags, e)
        except RateLimitExceededException as e:
            self.handle_exception("Rate limit exceeded. Make sure you provided an access_token", tags, e)

    def handle_exception(self, msg, tags, e):
        self.warning(msg)
        self.log.debug("{}: {}".format(msg, e))
        raise ConfigurationError(msg)
