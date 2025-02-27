document.querySelectorAll(".scrolltop").forEach(function (element) {
    element.addEventListener("click", function (event) {
        event.preventDefault();
        var linkPath = this.getAttribute('href');
        if (window.location.pathname != linkPath && linkPath != null) {
            window.location.href = linkPath;
        } else {
            window.scrollTo({
                top: 0,
                behavior: 'smooth',
                duration: 1100
            });
        }
    });
});
