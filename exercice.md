# Liberty Global - Technology Data Services / Data Automation Technical Assessment
## Is it Friday Yet ? (estimate: 1h)

### Create a REST Backend


Create a REST API Python application that returns if *it is Friday yet*.

```sh
# On a Friday
$ curl http://localhost:5000
It is friday !

# On a non-Friday
$ curl http://localhost:5000
It is not friday yet :(
```

The project has to follow the below instructions:

- Make use of Poetry for dependencies
- Use [ruff](https://github.com/charliermarsh/ruff) as a Python Linter
- Use [pre-commit](https://pre-commit.com/)
  - Integrate `ruff` inside `pre-commit`
- Use Flask as backend


### Continuous-Integration

Once the REST API is set and properly written, it is expected to be packaged as a Docker image.

- Provide a best-effort Jenkinsfile for the CI/CD
  - Make sure to re-run `pre-commit` steps as a double-check
  - When we are on master branch or a tag, build the container and push it to `$DOCKER_REGISTRY`.
  - The Docker tag should be `master` or `1.0.0` if a git tag is `1.0.0`


_Best-Effort means that the Jenkinsfile doesn't necessary have to run correctly. Don't bother with any KubernetesPod file, `container` or `node` statement. Just issue the command you would run_


### Deliverable

Everything should be committed to a public GitHub repository. Any additional good practice is welcomed.
