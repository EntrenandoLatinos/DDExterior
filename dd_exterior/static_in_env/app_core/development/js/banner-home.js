function bannerAnimation() {
    let bannerhome = document.querySelector('.banner-home');
    window.onload = (event) => {
        bannerhome.classList.add('animation')
    };
}

function bannerMobile() {
    const is_phone = isMobile();
    let bannerhome = document.querySelector('.banner-home');
    if (bannerhome) {
        bannerhome.style.height = is_phone ? 'calc(100vh - 55px)' : '';
    }
}

document.addEventListener('DOMContentLoaded', function () {
    bannerMobile();
    bannerAnimation();
});