Now that we created the basis for our integration, we are going to add configurations.

# Goals

- Create an `access_token` configuration parameter into the `init_config` section of the integration configuration file.
- Create an `repository_name` configuration parameter into the `instances` section of the integration configuration file.
- Use both parameter in your `check` function logic.
- Handle exceptions by raising `ConfigurationError` errors. 
  - Check parameters are set and valid.
- Create a test to make sure that your code works.

# Hints

- Implement the `__init__` method to retrieve `init_config` configurations.
  - You still need to instanciate the super `AgentCheck` class
- You can create methods to factorize code.
- You can take example on official open source [Datadog integrations](https://github.com/DataDog/integrations-core).
- Take a look at the [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#configuration-file) to see how to edit your configuration file.
