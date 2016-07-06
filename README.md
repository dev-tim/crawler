[![Build Status](https://travis-ci.org/WorldBrain/crawler.svg?branch=master)](https://travis-ci.org/WorldBrain/crawler)

[![Python version](https://img.shields.io/badge/python-3.5-brightgreen.svg)](https://travis-ci.org/WorldBrain/crawler)

# crawler
A crawler which will retrieve web content which can later be used for data analysis.

# Outline
This project is a component of the [Worldbrain][wbrain] project.

Please refer there to better understand the big picture of what we are trying to achieve.

# Install
You'll need to get the system requirements installed first:

```
$ make sys_requirements
```

Then, get the python requirements installed. This project is using [Python3.5][py35].

It is highly recommended that you use a [virtual environment][venv]:

```
$ python3.5 -m venv .venv
$ . .venv/bin/activate
```

Then get everything installed with [pip][pypip]:

```
$ pip install -r requirements/dev.txt
```

# Testing
We use [py.test][pytest] for our testing.

```
$ py.test crawler
$ ptw crawler -- --testmon
```

# Requirements
We manage our requirements with [pip-tools][ptools].

You can build requirements by running:

```
$ make requirements
```

And you can rebuild them with:

```
$ make requirements_rebuild
```

# Contributing
We use [Github flow][flow] to manage our contributions. This means, you
can do the following steps to submit a pull request:

  1. Fork the project and clone a local copy
  2. Create a new branch and make your changes + add tests
  3. Push to your remote and submit your pull request

Your pull request will be merged when at least 1 other developer decides it is
ready to go. Your changes will be run against a [Travis][travis] build to make
sure you adhere to style guidelines and the changes pass the tests.

Please check the [issues][issues] for something to do!

[pytest]: http://pytest.org/latest/
[venv]: https://docs.python.org/3/library/venv.html
[pypip]: https://pip.pypa.io/en/stable/
[py35]: https://www.python.org/download/releases/3.3.5/
[pip-tools]: https://github.com/nvie/pip-tools
[flow]: https://guides.github.com/introduction/flow/
[travis]: https://guides.github.com/introduction/flow/
[issues]: https://github.com/WorldBrain/crawler/issues
[wbrain]: https://github.com/WorldBrain/Webmarks
