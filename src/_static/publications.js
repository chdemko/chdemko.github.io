document.addEventListener("DOMContentLoaded", () => {
  const inputs = document.querySelectorAll(".pub-filter input");
  if (!inputs.length) {
    return;
  }

  const selected = (key) =>
    document.querySelector(`input[name="pub-${key}"]:checked`).value;

  const apply = () => {
    const audience = selected("audience");
    const type = selected("type");

    document.querySelectorAll(".citation").forEach((citation) => {
      const visible =
        (audience === "all" || citation.querySelector(`.audience-${audience}`)) &&
        (type === "all" || citation.querySelector(`.type-${type}`));
      citation.classList.toggle("pub-hidden", !visible);
    });

    // Hide years (and their entry in the "On this page" sidebar) that no
    // longer contain any visible entry.
    const tocLinks = document.querySelectorAll(".localtoc a[href^='#']");
    document.querySelectorAll("section:has(> h2)").forEach((year) => {
      const empty = !year.querySelector(".citation:not(.pub-hidden)");
      year.classList.toggle("pub-hidden", empty);
      tocLinks.forEach((link) => {
        if (link.getAttribute("href") === `#${year.id}`) {
          link.parentElement.classList.toggle("pub-hidden", empty);
        }
      });
    });
  };

  inputs.forEach((input) => input.addEventListener("change", apply));
  apply();
});
