document.addEventListener("DOMContentLoaded", function() {
    let xpBar = document.getElementById("xpBar");
    let xpValue = document.getElementById("xpValue");

    xpBar.addEventListener("click", function() {
        let newXp = parseInt(xpBar.value) + 10;
        if (newXp > 1100) newXp = 1100;
        xpBar.value = newXp;
        xpValue.textContent = newXp;
    });
});
