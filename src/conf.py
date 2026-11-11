"""The configuration module for sphinx."""

html_theme = "shibuya"

# Get metadata
project = "χristoφe Демко"
author = "Christophe Demko"
project_copyright = f"1995-%Y, {author}"

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
blog_title = "My Sphinx Blog"
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
        {
            "title": "blog",
            "url": "blog/index"
        },
        {
            "title": "publications",
            "url": "publications"
        },
        {
            "title": "projects",
            "url": "projects"
        },
        {
            "title": "teaching",
            "url": "teaching"
        },
    ]
}


# Bibtex
bibtex_bibfiles = [
    "refs.bib",
]
