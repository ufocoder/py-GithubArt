Github Art
==========

[![Build Status](https://travis-ci.org/ufocoder/py-GithubArt.svg)](https://travis-ci.org/ufocoder/py-GithubArt)

Python project to write string on Contributions Github account table

![Github Contributions](docs/contributions.png)

Usage
-----

Install github_art
```
pip install github_art
```

```
mkdir /Users/user/build
```

There's an example of script usage:

```
python github_art/github_art/main.py \
    --string demo \
    --path /Users/user/build \
    --project https://github.com/ufocoder/py2-Github-FakeContributions.git
```

Options
-------
* string - your string [required]
* dictionary - letters or letters2x
* path - there's a path to your github project [required parameter]
* project - URL to your github project [required parameter]