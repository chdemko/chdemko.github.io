from docutils import nodes
from pybtex.database import Person
from pybtex.richtext import HRef, Tag
from pybtex.style.labels import BaseLabelStyle
from pybtex.style.names.plain import NameStyle
from pybtex.style.sorting import BaseSortingStyle
from pybtex.style.template import field, href, node, tag
from pybtex_docutils import Backend as DocutilsBackend


BOLD_NAMES = (
    "Demko, Christophe",
)

AUTHOR_LINKS = {
    "Guillaume, Jean-Loup": "https://jlguillaume.fr/",
    "Bertet, Karell": "https://kbertet.pagelab.univ-lr.fr/",
    "Waffo Kemgne, Martin": "https://martinwaffo.github.io/",
}

MONTHS = {}
for number, name in enumerate(
    (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ),
    start=1,
):
    MONTHS.update({name.casefold(): number, name[:3].casefold(): number})
    MONTHS[str(number)] = number


class RecentFirstSortingStyle(BaseSortingStyle):
    def sorting_key(self, entry):
        year = entry.fields.get("year", "")
        month = entry.fields.get("month", "").strip().casefold()
        if month and month not in MONTHS:
            raise ValueError(f"Invalid month {month!r} in entry {entry.key!r}")
        return year, MONTHS[month] if month else 13

    def sort(self, entries):
        return sorted(entries, key=self.sorting_key, reverse=True)


class MyLabelStyle(BaseLabelStyle):
    def format_labels(self, sorted_entries):
        counters = {}
        labels = []

        for entry in reversed(list(sorted_entries)):
            if entry.type == "article":
                prefix = "J"
            elif entry.type in ("inproceedings", "conference"):
                prefix = "C"
            elif entry.type == "software":
                prefix = "S"
            elif entry.type == "inbook":
                prefix = "H"
            elif entry.type == "book":
                prefix = "B"
            elif entry.type == "phdthesis":
                prefix = "P"
            elif entry.type == "techreport":
                prefix = "R"
            else:
                prefix = "W"

            year = entry.fields.get("year", "????")
            key = (prefix, year)
            counters[key] = counters.get(key, 0) + 1
            labels.append(f"{prefix}-{year}-{counters[key]}")

        yield from reversed(labels)


class HighlightNameStyle(NameStyle):
    def format(self, person, abbr=False):
        formatted = super().format(person, abbr=abbr)
        if any(person == Person(name) for name in BOLD_NAMES):
            formatted = tag("strong")[formatted]
        for name, url in AUTHOR_LINKS.items():
            if person == Person(name):
                return href(url)[formatted]
        return formatted


def badge_classes(color, extra_classes=()):
    return [
        "sd-badge",
        f"sd-bg-{color}",
        f"sd-bg-text-{color}",
        *extra_classes,
    ]


class LinkBadge(HRef):
    def render(self, backend):
        rendered = super().render(backend)
        if isinstance(backend, DocutilsBackend):
            for link in rendered:
                link["classes"].extend(
                    badge_classes(
                        self.color, ("link-badge", f"{self.color}-link-badge")
                    )
                )
        return rendered


class DOIButton(LinkBadge):
    color = "primary"


class URLButton(LinkBadge):
    color = "info"


@node
def doi_button(children, context):
    doi = field("doi", raw=True).format_data(context)
    return DOIButton(f"https://doi.org/{doi}", "DOI")


@node
def url_button(children, context):
    url = field("url", raw=True).format_data(context)
    return URLButton(url, "URL")


class SimpleBadge(Tag):
    def __init__(self, label, css_class="secondary", extra_classes=()):
        super().__init__("span", label)
        self.css_class = css_class
        self.extra_classes = list(extra_classes)

    def render(self, backend):
        rendered = backend.render_sequence(
            [part.render(backend) for part in self.parts]
        )
        if backend.name == "docutils":
            return [
                nodes.inline(
                    "",
                    "",
                    *rendered,
                    classes=badge_classes(self.css_class, self.extra_classes),
                )
            ]
        return rendered
