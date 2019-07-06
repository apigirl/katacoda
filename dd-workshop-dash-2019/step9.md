# Goals

- Submit metrics as per the specification document.
- Create a test to assert metric submission.

# Hints

- Use `self.gauge` to [submit metrics](https://docs.datadoghq.com/developers/metrics/gauges/).
- Use `import mock` to [mock PyGithub objects and methods](https://docs.python.org/3/library/unittest.mock.html#).
- If you don't want to use your github token, you can introduce a testing config in your check. eg `_ship_access_token`.

