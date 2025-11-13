document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");

  form.addEventListener("submit", function (event) {
    const name = document.getElementById("inputName").value.trim();
    const password = document.getElementById("inputPassword").value.trim();
    const marketing = document.getElementById("inputMarketing").checked;

    if (!marketing) {
      alert("Please tick the box before submitting.");
      event.preventDefault();
      return;
    }

    if (name.length > 25) {
      alert("Username cannot exceed 25 characters!");
      event.preventDefault();
      return;
    }

    if (password.length > 25) {
      alert("Password cannot exceed 25 characters!");
      event.preventDefault();
      return;
    }

    // this form will now be sent to Flask auto
  });
});
