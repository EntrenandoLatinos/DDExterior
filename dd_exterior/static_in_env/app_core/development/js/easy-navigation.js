
function handleScrollTo(targetPosition) {
    window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
    });
}

function handleNavItemClick(event, containerMenu) {
    const { id: getId, url: getUrl, offsetScroll: getOffset } = event.target.dataset;
    if (containerMenu.dataset.work === 'true') {
        const target = document.getElementById(getId);
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - getOffset;
        handleScrollTo(targetPosition);
    } else {
        const section = document.querySelector('.easy-navigation');
        window.location.href = `${getUrl}#${section.id}`;
    }
}

function setupNavigation(containerMenu, navItems, sections) {
    if (containerMenu.dataset.work === 'true') {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) navItems.forEach(item => item.classList.toggle('active', item.dataset.id === entry.target.id));

            });
        }, {
            threshold: 1
        });

        sections.forEach(section => observer.observe(section));
    } else {
        const currentUrl = window.location.pathname;
        const elementLi = containerMenu.querySelector(`[data-url*="${currentUrl}"]`);
        if (elementLi) elementLi.classList.add('active-add');
    }

    navItems.forEach(item => item.addEventListener('click', (event) => handleNavItemClick(event, containerMenu)));
}

document.addEventListener("DOMContentLoaded", function () {
    const containerEasyNavigation = this.querySelectorAll('.container-easy-navigation')
    containerEasyNavigation.forEach(element => {
        const containerMenu = element.querySelector('.sidebar-easy-navigation');
        const navItems = containerMenu ? containerMenu.querySelectorAll('.item-easy-navigation') : null;
        const sections = element.querySelectorAll('.easy-navigation');

        if (containerMenu && navItems && sections)
            setupNavigation(containerMenu, navItems, sections);
    });


    window.addEventListener("load", () => {
        const hash = window.location.hash;
        if (hash != '') {
            const hashValue = hash.substring(1);
            const section = document.getElementById(hashValue);
            const menuItem = document.querySelector(`.item-easy-navigation[data-id*="${hashValue}"]`);
            if (section)
                setTimeout(() => handleScrollTo(section.getBoundingClientRect().top + window.scrollY - menuItem.dataset.offsetScroll), 200);
        }
    });
});
