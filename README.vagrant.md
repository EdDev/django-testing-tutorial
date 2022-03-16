# Overview

The instructions describe in this document focus on the usage of vagrant,
a tool that build and manage VM/s.

## Install

### Install virtualization

This Vagrant environemnt tested with VirtualBox virtualization  
installed refer:  
[VirtualBox install](https://www.virtualbox.org/manual/ch02.html)  
[VirtualBox download](https://www.virtualbox.org/wiki/Downloads#manual)  

### Install vagrant

Windows and Apple users should be able to install the tool, please review
the tool installation instructions.
[vagrant install](https://www.vagrantup.com/docs/installation)

## Run  

clone the repo

```bash
git clone https://github.com/EdDev/django-testing-tutorial.git`
cd django-testing-tutorial
```

To build the virtualization image, need to run vagrant up  
`cd vagrant`  
`vagrant up`  

*Note:* all vagrant commands at host level should run from project/vagrant directory

Wait for vagrant output to appear:
default: + nohup pipenv run python manage.py runserver 0.0.0.0:8000

## Test Django server

`curl http://127.0.0.1:8000/member`

You should receive this output:  
`{}`

## Development

This section targets contributors which need to run local checks before
posting a PR.

### Tests

[pytest](https://docs.pytest.org) is used to run tests.

### Arbitrary commands

During development, there may be a need to run various command,
like creating applications and running migrations.

These steps can be done by accessing the vagrant machine terminal,

- Accessing the vagrant terminal:
  Run this command from vagrant directory of this repo
  `vagrant ssh`
- Run django-pytest
  Inside the machine move to project shred directory:
  `cd /vagrant/vagrant`
- Sync dev packages:
  `pipenv sync --dev`
- Run the test exist in the project
  `cd /vagrant`
  `pipenv run pytest -v`  
