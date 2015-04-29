Github Art
==========

[![Build Status](https://travis-ci.org/ufocoder/py-GithubArt.svg)](https://travis-ci.org/ufocoder/py-GithubArt)
[![Coverage Status](https://coveralls.io/repos/ufocoder/py-GithubArt/badge.svg?branch=master)](https://coveralls.io/r/ufocoder/py-GithubArt?branch=master)

Python project to write string on Contributions Github account table

![Github Contributions](docs/contributions.png)

Usage
-----

Install from PIP:
```
pip install github_art
```

Create folder to build git project:
```
mkdir /Users/user/build
```

And run python github_art, there's an example of script usage:

```
python github_art \
    --string ufocoder \
    --path /Users/user/build \
    --project https://github.com/ufocoder/py2-Github-FakeContributions.git
```

Options
-------
* string - your string [required parameter]
* dictionary - alphanumeric or alphanumeric2x
* path - there's a path to your github project [required parameter]
* project - URL to your github project [required parameter]