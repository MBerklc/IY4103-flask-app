document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");

  form.addEventListener("submit", function (event) {
    const name = document.getElementById("inputName").value.trim();
    const password = document.getElementById("inputPassword").value.trim();
    const marketing = document.getElementById("inputMarketing").checked; // ✅ checkbox check

    // Check if checkbox is ticked
    if (!marketing) {
      alert("Please tick the box and then submit.");
      event.preventDefault();
      return;
    }

    // Name max 25 characters
    if (name.length > 25) {
      alert("Username cannot exceed 25 characters!");
      event.preventDefault();
      return;
    }

    // Password max 25 characters
    if (password.length > 25) {
      alert("Password cannot exceed 25 characters!");
      event.preventDefault();
      return;
    }
  });
});
