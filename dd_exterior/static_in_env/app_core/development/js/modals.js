var modal = document.getElementById("modal");
var openButton = document.getElementById("openModal");
var closeButton = document.getElementsByClassName("close-button")[0];

if (openButton)
    openButton.onclick = function () {
        modal.style.display = "block";
    };

if (closeButton)
    closeButton.onclick = function () {
        modal.classList.add("animate-out");
        setTimeout(function () {
            modal.style.display = "none";
            modal.classList.remove("animate-out");
        }, 500);
    };

window.onclick = function (event) {
    if (event.target == modal) {
        modal.classList.add("animate-out");
        setTimeout(function () {
            modal.style.display = "none";
            modal.classList.remove("animate-out");
        }, 500);
    }
};
