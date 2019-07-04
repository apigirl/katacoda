# Configurations

## Goals
- Create an `access_token` and an `repository_name` config as per the specification document.
- Use them in your check to run the same code as before.
- Handle exceptions by raising `ConfigurationError` errors.
- Create a test to make sure that your code works.

## Hints
- Implement the __init__ method to retrieve `init_config` configurations.
  - Don't forget to instanciate the super AgentCheck class
- You can create methods to factorize code.
