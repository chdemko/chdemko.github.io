from pybtex.richtext import Tag
from docutils import nodes


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