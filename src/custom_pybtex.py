from pybtex.richtext import Tag
from docutils import nodes


class BootstrapBadge(Tag):

    def __init__(self, label, css_class="secondary", title=""):
        super().__init__("span", label)
        self.css_class = css_class
        self.title = title

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
                    classes=["sd-badge", f"sd-badge sd-bg-{self.css_class} sd-bg-text-{self.css_class}"],
                )
            ]
        return rendered