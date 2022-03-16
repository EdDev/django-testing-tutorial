# Using [podman](https://podman.io/)

## Overview
The instructions describe in this document focus on the usage of podman,
a container engine for Linux.

Windows and Apple users should be able to install podman, please review
the tool installation instructions.

Most of the instruction that follows should also work with *docker*, however,
no format testing have been performed to validate this claim.

## Build the container image locally
To build the container image, just execute the following command from
the project root folder:

`podman build -f dockerfile/Dockerfile -t beyond .`

## Run the Django project
Running the project is as simple as running the container image
without arguments:

`podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z -p 8000:8000 localhost/beyond`

The exposed pages should be available on the running host by accessing:
`http://localhost:8000`.

## Development
This section targets contributors which need to run local checks before
posting a PR.

### Format the codebase
[black](https://github.com/psf/black) is used to format the code
in an opinionated manner.

To perform a format that will mutate the code, run:
`podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z localhost/beyond black -S ./`

To perform a format check (without mutation), run:
`podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z localhost/beyond black -S --check --diff ./`

### Linters
[flake8](https://github.com/PyCQA/flake8) is used for static analysis.

To run the linter check, run:
`podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z localhost/beyond python3 -m flake8 --max-line-length 100`

### Tests
[pytest](https://docs.pytest.org) is used to run tests.

To run all available tests, run:
`podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z localhost/beyond pytest`

### Arbitrary commands
During development, there may be a need to run various command,
like creating applications and running migrations.

These steps can be done by either accessing the container terminal,
or adding the command at the tail (see below).

- Accessing the container terminal:
  `podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z localhost/beyond bash`
- Run a command directly:
  `podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z localhost/beyond <commands to execute>`

> **Note**: The commands that execute the container, can be aliased for easier usage:
>
> `alias run-beyond='podman run -ti --rm -v $(pwd):/workspace/django-testing-tutorial:Z localhost/beyond'`
>
> Then the running the tests for example is as simple as:
>
> `run-beyond pytest`
