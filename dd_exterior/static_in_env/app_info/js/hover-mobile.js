document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.toggle('enable-hover', !isMobile());
    if (isMobile()) {
        const buttons = document.querySelectorAll('.follo-us ul li');
        const totalButtons = buttons.length;
        window.addEventListener('scroll', function () {
            var scroll = window.scrollY;
            var height = document.documentElement.scrollHeight - window.innerHeight;
            var scrollPercentage = (scroll / height) * 100;
            scrollPercentage = scrollPercentage >= 99.99 ? 99.98 : scrollPercentage;
            var percentagePerButton = 100 / totalButtons;

            buttons.forEach(function (button, index) {
                var startRange = index * percentagePerButton;
                var endRange = (index + 1) * percentagePerButton;

                button.classList.toggle('active', scrollPercentage >= startRange && scrollPercentage < endRange)
            });
        });
    }
});