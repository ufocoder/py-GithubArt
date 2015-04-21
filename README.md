Github Art
==========

Python project to write string on Contributions Github account table

![Github Contributions](docs/contributions.png)

Install
------
pip install -r requirements/base.txt


Usage
-----

There's an example of script usage:

```
mkdir build
python github_art/github_art/main.py \
    --string ufoworker \
    --size 2 \
    --path build \
    --account https://github.com/ufocoder/py2-Github-FakeContributions.git
```

Options
-------

* string - your string [required]
* size - 1 or 2
* path - there's a path to your github project [required]
* account - URL to your github project