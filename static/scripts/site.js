document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");

  form.addEventListener("submit", function (event) {
    const name = document.getElementById("inputName").value.trim();
    const phone = document.getElementById("inputPhone").value.trim();
    const email = document.getElementById("inputEmail").value.trim();

    // Name max 25 characters
    if (name.length > 25) {
      alert("Name cannot exceed 25 characters!");
      event.preventDefault();
      return;
    }

    // Phone only digits and max 15
    if (!/^\d+$/.test(phone)) {
      alert("Phone number must contain digits only!");
      event.preventDefault();
      return;
    }

    if (phone.length > 15) {
      alert("Phone number cannot exceed 15 digits!");
      event.preventDefault();
      return;
    }

    // Email simple validation
    if (!email.includes("@") || email.length > 50) {
      alert("Please enter a valid email (max 50 characters)!");
      event.preventDefault();
      return;
    }
  });
});
