First you need to install the PyGithub dependency:
- `pip install PyGithub`

Then, you can run the following script to print the repo full name:
- `python`
  ```python
  from github import Github
  g = Github()
  r = g.get_repo("Datadog/integrations-extras")
  r.full_name
  ```
