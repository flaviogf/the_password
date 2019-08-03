(() => {
  function toggleShowPassword(element) {
    const inputPassword = element.previousElementSibling;
    const current = inputPassword.type;
    inputPassword.type = current == "text" ? "password" : "text";
  }

  document.querySelectorAll("[data-show-password]").forEach(el => {
    el.onclick = _ => toggleShowPassword(el);
  });
})();
