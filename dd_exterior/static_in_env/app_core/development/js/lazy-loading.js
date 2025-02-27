function lazyLoading() {
    const lazyImages = document.querySelectorAll(".lazy-loading");
    const lazyIcons = document.querySelectorAll(".loading-icon");

    const lazyLoad = (image) => {
        const imageView = image.parentElement.tagName === 'A' ? image.parentElement : image;
        const loadingIcon = imageView.nextElementSibling;

        if (image.dataset.lazySrc) {
            image.addEventListener("load", () => {
                image.style.opacity = 1;
                if (loadingIcon) {
                    loadingIcon.parentElement.style.position = '';
                    loadingIcon.style.display = "none";
                }
            });
            image.src = image.dataset.lazySrc;
        }
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                lazyLoad(entry.target);
                observer.unobserve(entry.target);
            }
        });
    });

    lazyImages.forEach(img => observer.observe(img));
    lazyIcons.forEach(icon => icon.parentElement.style.position = 'relative');
}

document.addEventListener("DOMContentLoaded", lazyLoading);
