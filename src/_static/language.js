(() => {
  const language = document.documentElement.lang;
  if (language !== "en" && language !== "fr") {
    return;
  }

  const path = new URL("../../", document.currentScript.src).pathname;
  const secure = window.location.protocol === "https:" ? "; Secure" : "";
  document.cookie =
    `site_language=${language}; Path=${path}; Max-Age=31536000; SameSite=Lax` +
    secure;
})();
