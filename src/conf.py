"""The configuration module for sphinx."""

import html
import os
import posixpath
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pybtex.plugin import register_plugin
from pybtex.richtext import Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from sphinx.errors import ConfigError

from custom_pybtex import BootstrapBadge, MyLabelStyle, RecentFirstSortingStyle
from site_languages import PAGES

html_theme = "shibuya"

# Get metadata
project = "χristoφe Демко"
author = project
project_copyright = f"1995-%Y, {author}"
html_title = project

# -- General configuration ------------------------------------------------

extensions = [
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
templates_path = [str(Path(__file__).parent / "_templates")]

# The master document.
master_doc = "404" if os.environ.get("SITE_ROOT") == "1" else "index"
if master_doc == "404":
    exclude_patterns = ["en/**", "fr/**"]

# The language for content by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = os.environ.get("SITE_LANGUAGE", "en")

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
html_static_path = [str(Path(__file__).parent / "_static")]
html_css_files = ["custom.css"]
html_js_files = ["publications.js"]
html_theme_options = {
    "accent_color": "crimson",
    "nav_links": [
        {"title": "📰 Blog", "url": "blog/index"},
        {"title": "📚 Publications", "url": "publications"},
        {
            "title": "📖 Enseignement" if language == "fr" else "📖 Teaching",
            "url": "enseignement" if language == "fr" else "teaching",
        },
        {
            "title": "🏗️ Projets" if language == "fr" else "🏗️ Projects",
            "url": "projets" if language == "fr" else "projects",
        },
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
    str(Path(__file__).parent / "refs.bib"),
]


# entry.type -> (badge label, sphinx-design color)
TYPE_BADGES = {
    "article": ("Journal", "journal"),
    "inproceedings": ("Conference", "info"),
    "conference": ("Conference", "info"),
    "misc": ("Communication", "warning"),
    "software": ("Software", "software"),
    "book": ("Book", "danger"),
    "inbook": ("Chapter", "danger"),
    "phdthesis": ("Thesis", "secondary"),
    "techreport": ("Report", "secondary"),
}

if language == "fr":
    TYPE_BADGES.update(
        {
            "article": ("Revue", "journal"),
            "inproceedings": ("Conférence", "info"),
            "conference": ("Conférence", "info"),
            "software": ("Logiciel", "software"),
            "book": ("Livre", "danger"),
            "inbook": ("Chapitre", "danger"),
            "phdthesis": ("Thèse", "secondary"),
            "techreport": ("Rapport", "secondary"),
        }
    )

SCOPE_BADGES = {
    "INT": "primary",
    "NAT": "secondary",
}


class MyStyle(UnsrtStyle):
    default_label_style = MyLabelStyle
    default_sorting_style = RecentFirstSortingStyle

    def format_entry(self, label, entry, bib_data=None):
        formatted = super().format_entry(label, entry, bib_data=bib_data)
        badges = []

        if entry.type in TYPE_BADGES:
            text, color = TYPE_BADGES[entry.type]
            badges.append(
                BootstrapBadge(
                    text,
                    css_class=color,
                    extra_classes=[f"type-{entry.type}"],
                )
            )

        scope = entry.fields.get("scope", "").upper()
        if scope in SCOPE_BADGES:
            badges.append(
                BootstrapBadge(
                    scope,
                    css_class=SCOPE_BADGES[scope],
                    extra_classes=[f"scope-{scope.lower()}"],
                )
            )

        if not badges:
            return formatted

        prefix = []
        for badge in badges:
            prefix.extend([badge, " "])
        formatted.text = Text(*prefix, formatted.text)
        return formatted


register_plugin(
    "pybtex.style.formatting",
    "my_style",
    MyStyle,
)

bibtex_default_style = "my_style"
bibtex_reference_style = "label"


def copy_assets(app, exception):
    if exception is not None:
        return
    source = Path(__file__).parent / "assets"
    destination = Path(app.outdir) / "assets"
    shutil.copytree(source, destination, dirs_exist_ok=True)


def validate_page_sources(app):
    root = Path(__file__).parent
    for language in ("en", "fr"):
        names = [page[language] for page in PAGES]
        if len(set(names)) != len(names):
            raise ConfigError(f"Duplicate {language} page in PAGES")
        for name in names:
            path = root / language / f"{name}.md"
            if not path.is_file():
                raise ConfigError(f"Missing {language} page: {path}")


def write_legacy_redirects(app, exception):
    if exception is not None or app.builder.format != "html":
        return
    if app.config.language != "en" or Path(app.outdir).name != "en":
        return
    output = Path(app.outdir).parent
    destination = output / "index.html"
    relative = os.path.relpath(Path(app.outdir) / "index.html", output)
    escaped = html.escape(relative, quote=True)
    destination.write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0; url={escaped}">'
        f'<link rel="canonical" href="{escaped}"></head>'
        f'<body><a href="{escaped}">Continue</a></body></html>\n',
        encoding="utf-8",
    )


def language_links(app, pagename, templatename, context, doctree):
    language = app.config.language
    pair = next((page for page in PAGES if page[language] == pagename), None)
    if pagename in {"search", "genindex"}:
        pair = {"en": pagename, "fr": pagename}
    if pair:
        current = posixpath.join(app.config.language, pagename + ".html")
        context["languages"] = [
            (
                label,
                posixpath.relpath(
                    f"{lang}/{pair[lang]}.html", posixpath.dirname(current)
                ),
                lang,
            )
            for label, lang in zip(
                ("🇬🇧 English", "🇫🇷 Français"), ("en", "fr")
            )
        ]


def setup(app):
    app.connect("builder-inited", validate_page_sources)
    app.connect("build-finished", copy_assets)
    app.connect("build-finished", write_legacy_redirects)
    app.connect("html-page-context", language_links)
