# Getting Started - Solution

First you need to install PyGithub.
- `pip install PyGithub`

Then you can start python and print the repository fullname by running the following lines.

```python
from github import Github
g = Github()
r = g.get_repo("Datadog/integration-extras")
r.full_name
```

