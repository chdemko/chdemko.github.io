"""The configuration module for sphinx."""

from pathlib import Path
import shutil

html_theme = "shibuya"

# Get metadata
project = "χristoφe Демко"
author = project
project_copyright = f"1995-%Y, {author}"
html_title = project

# -- General configuration ------------------------------------------------

extensions = [
    "sphinx.ext.graphviz",
    "myst_parser",
    "sphinx_design",
    "sphinxcontrib.bibtex",
]

myst_enable_extensions = [
    "colon_fence",
    "attrs_inline",
    "attrs_block",
    "deflist",
    "tasklist",
    "fieldlist",
    "dollarmath",
    "amsmath",
]

graphviz_output_format = "svg"

plantuml_output_format = "svg"

suppress_warnings = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The master document.
master_doc = "index"

# The language for content by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# The name of the (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Theme options are theme-specific and customise the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "accent_color": "crimson",
    "nav_links": [
         {"title": "📰 Blog", "url": "blog/index"},
         {"title": "📚 Publications", "url": "publications"},
         {"title": "📖 Teaching", "url": "teaching"},
         {"title": "🏗️ Projects", "url": "projects"},
    ],
    "page_layout": "compact",
    "hide_breadcrumbs": True,
    "nav_socials": [],
    "foot_socials": ["github", "linkedin", "bluesky", "mastodon", "x"],
    # Development platforms
    "github_url": "https://github.com/chdemko",
    # Chat & Community
    # Social & Microblogging
    "x_url": "https://x.com/chdemko",
    "mastodon_url": "https://mastodon.social/@chdemko",
    "bluesky_url": "https://bsky.app/profile/chdemko.bsky.social",
    # Content & Professional
    "linkedin_url": "https://www.linkedin.com/in/chdemko",
}

# Bibtex
bibtex_bibfiles = [
    "refs.bib",
]

# Use the unsrtalpha style as the default bibliography style.
bibtex_default_style = "unsrtalpha"


def copy_assets(app, exception):
    if exception is not None:
        return
    source = Path(app.srcdir) / "assets"
    destination = Path(app.outdir) / "assets"
    shutil.copytree(source, destination, dirs_exist_ok=True)


def setup(app):
    app.connect("build-finished", copy_assets)
