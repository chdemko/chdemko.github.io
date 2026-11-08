# Personal site

## Introduction

This GitLab repository contains the source code for my personal website, which
is built using
[**Hatch**](https://hatch.pypa.io/) and
[**Sphinx**](https://www.sphinx-doc.org/) with the
[**Shibuya** theme](https://shibuya.lepture.com/) (`crimson`color).

The website is deployed on
[**GitLab Pages**](https://docs.gitlab.com/ee/user/project/pages/) using a GitLab runner
provided by La Rochelle University (`pagelab` tag).

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

The build produces English pages under `en/` and French pages under `fr/`.
The original URLs redirect to their English equivalents. Both GitHub Pages and
GitLab Pages use this same build.

English source pages are in `src/en/`; French pages are in `src/fr/`.
Each filename corresponds to its published slug. The mapping between pages and
legacy URLs is maintained in `src/site_languages.py`. When adding a page, add
its translation and mapping as well as the appropriate toctree entries in both
languages.

Run the bilingual build checks with:

```shell-session
$ hatch run python -m unittest discover -s tests
```

## Serve

```shell-session
$ hatch run serve
```
