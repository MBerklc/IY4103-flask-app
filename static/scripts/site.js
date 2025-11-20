document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");
  if (!form) return;

  form.addEventListener("submit", function (event) {
    const name = document.getElementById("inputName").value.trim();
    const password = document.getElementById("inputPassword").value.trim();
    const marketing = document.getElementById("inputMarketing").checked;

    // Require checkbox
    if (!marketing) {
        alert("Please tick the box before submitting.");
        event.preventDefault();
        return;
    }

    if (name.length < 5 || name.length > 25) {
        alert("Username must be between 5-25 characters!");
        event.preventDefault();
        return;
    }

    if (password.length < 5 || password.length > 25) {
        alert("Password must be between 5-25 characters!");
        event.preventDefault();
        return;
    }


    // this form will now be sent to Flask auto
  });
});