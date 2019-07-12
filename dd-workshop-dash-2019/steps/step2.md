First, you need to install the PyGithub dependency:
- `pip install PyGithub`{{execute}}

Then, you can run the following script to print the repo name:
- `python`
  ```python
  from github import Github
  g = Github("<YOUR_ACCESS_TOKEN>")
  r = g.get_repo("Datadog/integrations-extras")
  r.name
  ```
