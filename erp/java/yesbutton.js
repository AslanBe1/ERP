document.addEventListener("DOMContentLoaded", function() {
    const logoutButton = document.getElementById("logoutButton");
    const logoutModal = document.getElementById("logoutModal");
    const confirmLogout = document.getElementById("confirmLogout");
    const cancelLogout = document.getElementById("cancelLogout");

    logoutButton.addEventListener("click", function(event) {
        event.preventDefault(); // Logoutni to'g'ridan-to'g'ri bosilishidan saqlaydi
        logoutModal.style.display = "block";
    });

    confirmLogout.addEventListener("click", function() {
        window.location.href = logoutButton.getAttribute("href"); // Logout URL-ga o'tkazadi
    });

    cancelLogout.addEventListener("click", function() {
        logoutModal.style.display = "none"; // Modalni yopadi
    });
});
