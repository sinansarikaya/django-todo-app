document.addEventListener("DOMContentLoaded", () => {
  const alertDivs = document.querySelectorAll(".alert");
  alertDivs.forEach((alertDiv)  => {
    alertDiv.classList.add("active");

    setTimeout(() => {
      alertDiv.classList.remove("active");
    }, 3000);
  });
});
