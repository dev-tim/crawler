[![Build Status](https://travis-ci.org/WorldBrain/crawler.svg?branch=master)](https://travis-ci.org/WorldBrain/crawler)
[![Python version](https://img.shields.io/badge/python-3.5-brightgreen.svg)](https://travis-ci.org/WorldBrain/crawler)

# crawler
A web crawler/parser with the purpose of indexing and parsing all articles for
a given domain. This project is a component of the [Worldbrain][wbrain] project.
Please refer there to better understand the big picture of what we are trying
to achieve.

We are currently planning the execution of this crawler. To add your 2 cents, please go to issue [#1][issue1].

**Input:**
  - List of domains trusted by the scientific community

**Processing:**
 1. Produce a list of all URLs for a given domain
 2. Process that list to find all URLs that are likely to be articles
 3. Retrieve the HTML for each article
 4. Run parser logic over that HTML

**Output:**
  - JSON containing all the content elements of each article
    - title, text, keywords, NLP summary, official summary,
    - publish date, tags, urls, authors, domainname, parse_time


# Install
You'll need to get the system requirements installed first:

```
$ make system_requirements
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

# Running spiders
Refer to the `crawler/` folder for more in depth details.

# Testing
We use [py.test][pytest] for our testing.

```
$ make test
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
[ptools]: https://github.com/nvie/pip-tools
[flow]: https://guides.github.com/introduction/flow/
[travis]: https://guides.github.com/introduction/flow/
[issues]: https://github.com/WorldBrain/crawler/issues
[wbrain]: https://github.com/WorldBrain/Webmarks
[issue1]: https://github.com/WorldBrain/crawler/issues/1
