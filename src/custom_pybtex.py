from docutils import nodes
from pybtex.richtext import Tag
from pybtex.style.labels import BaseLabelStyle
from pybtex.style.sorting import BaseSortingStyle


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


class BootstrapBadge(Tag):
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
                    classes=[
                        "sd-badge",
                        f"sd-bg-{self.css_class}",
                        f"sd-bg-text-{self.css_class}",
                        *self.extra_classes,
                    ],
                )
            ]
        return rendered
