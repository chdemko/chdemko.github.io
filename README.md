# Personal site

## Introduction

This GitLab repository contains the source code for my personal website, which is built using
[**Hatch**](https://hatch.pypa.io/latest/) and [**Sphinx**](https://www.sphinx-doc.org/)
with the [**Shibuya** theme](https://shibuya.lepture.com/).

The website is deployed on
[**GitLab Pages**](https://docs.gitlab.com/ee/user/project/pages/) using a GitLab runner
provided by La Rochelle University (using the `pagelab` tag).

The extensions used in this project are listed in the `pyproject.toml` file:

* [myst-parser](https://myst-parser.readthedocs.io/) for parsing Markdown files with
  MyST syntax.
* [sphinx-design](https://sphinx-design.readthedocs.io/) for creating responsive and
  visually appealing designs in Sphinx documentation.
* [sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/) for managing
  bibliographies and citations in Sphinx documentation.

## Build

```shell-session
$ hatch run build
```

To choose an output directory, append it after `--`:

```shell-session
$ hatch run build -- public
```

## Serve

```shell-session
$ hatch run serve
```
