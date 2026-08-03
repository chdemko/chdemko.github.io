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
    "ablog",
    "sphinx_design",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.plantuml",
    "sphinx_last_updated_by_git",
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

suppress_warnings = [
    #    "myst.xref_missing",
]

# Blog configuration
blog_title = "χristoφe Демко Blog"
blog_baseurl = "https://example.com"  # change later
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = ["blog/*.md"]

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

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "accent_color": "crimson",
    "nav_links": [
        {"title": "📰 Blog", "url": "blog/index"},
        {"title": "📚 Publications", "url": "publications"},
        {"title": "🏗️ Projects", "url": "projects"},
        {"title": "📖 Teaching", "url": "teaching"},
    ],
    "page_layout": "simple",
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

# ---------------------------------------------------------------------------
# Custom bibliography style: newest publication first
# ---------------------------------------------------------------------------

import pybtex.plugin
from pybtex.style.formatting.unsrtalpha import Style

MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


class DateDescendingStyle(Style):
    """
    Keep the standard unsrt formatting, but sort bibliography entries newest -> oldest.
    """
    def sort(self, entries):

        def sort_key(entry):
            fields = entry.fields

            # Year
            try:
                year = int(fields.get("year", "0"))
            except ValueError:
                year = 0

            # Month
            month_value = fields.get("month", "")

            if month_value:
                month_value = month_value.strip().lower()

                try:
                    month = int(month_value)
                except ValueError:
                    month = MONTHS.get(month_value, 0)
            else:
                month = 0

            # Day
            try:
                day = int(fields.get("day", "0"))
            except ValueError:
                day = 0

            return (year, month, day)

        # reverse=True gives newest -> oldest
        return sorted(entries, key=sort_key, reverse=True)


# Register the custom style with Pybtex.
pybtex.plugin.register_plugin(
    "pybtex.style.formatting",
    "date_descending",
    DateDescendingStyle,
)

# Use the custom style as the default bibliography style.
bibtex_default_style = "date_descending"


def copy_assets(app, exception):
    if exception is not None:
        return
    source = Path(app.srcdir) / "assets"
    destination = Path(app.outdir) / "assets"
    shutil.copytree(source, destination, dirs_exist_ok=True)


def setup(app):
    app.connect("build-finished", copy_assets)
