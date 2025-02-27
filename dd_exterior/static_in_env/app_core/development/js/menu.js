document.addEventListener("DOMContentLoaded", () => {
    if (!window.djangoData) {
        console.error("No Django data found!");
        return;
    }

    const { logo, currentPath, urlName, static_urls, dynamic_urls } = window.djangoData;

    if (isMobile()) {
        const contentSnippets = document.getElementById('content_snippets');
        const headerDesktop = document.getElementById('header_desktop');

        if (!contentSnippets || !headerDesktop) return;

        // Ocultar header y ajustar estilos del contenido principal
        headerDesktop.style.display = 'none';
        contentSnippets.style.overflowY = 'scroll';
        contentSnippets.style.overflowX = 'hidden';
        contentSnippets.style.height = 'calc(100vh - 60px)';

        // ------------------------ Crear modal submenu ------------------------ //

        const modalSubmenuSontainer = document.createElement('div');
        modalSubmenuSontainer.className = 'container-modal-mobile';
        modalSubmenuSontainer.innerHTML = `
            <div class="backdrop"></div>
            <div class="modal-content-mobile">
                <div class="close-modal">
                    <span></span>
                </div>
                <h2>Discover each of our services.</h2>
            </div>
        `;

        const listModalSubmenu = document.createElement('div');
        listModalSubmenu.className = 'button-group-container';

        dynamic_urls.forEach((info) => {
            const tagA = document.createElement("a");
            tagA.href = `/services/${info.slug}/`;
            tagA.className = "button-container";
            tagA.innerHTML = `
                <div class="icon-btn" style="background-image: url('${info.icon}')"></div>
                <p>${info.name}</p>
            `;
            listModalSubmenu.appendChild(tagA);
        });

        const modalContentModal = modalSubmenuSontainer.querySelector('.modal-content-mobile');
        modalContentModal.appendChild(listModalSubmenu);

        // ------------------------ Crear menu version mobile ------------------------ //

        const visualContainer = document.createElement('div');
        visualContainer.className = 'visual-container';
        const transition = 'transition-1';

        visualContainer.innerHTML = `
            <div id="mobile_menu" class="${transition}">
                <div id="burgerBtn"></div>
                <ul id="menu_list">
                    <img src="${logo}"></img>
                    <li data-url="${static_urls.index}"><p>Home</p></li>
                    <li data-url="${static_urls.about}"><p>About</p></li>
                    <li data-url="javascript:;"><p>Services</p></li>
                    <li data-url="${static_urls.works}"><p>Works</p></li>
                    <li data-url="${static_urls.faqs}"><p>Faq's</p></li>
                    <li data-url="${static_urls.contact}"><p>Contact</p></li>
                    <li data-url="${static_urls.privacy}"><p>Privacy</p></li>
                    <li data-url="${static_urls.admin_index}" data-target="_blank"><p>Login</p></li>
                </ul>
                <div id="mobileBodyContent">
                    <div id="mobile_header"></div>
                </div>
                
            </div>
        `;

        const mobile_menu = visualContainer.querySelector('#mobile_menu');
        mobile_menu.appendChild(modalSubmenuSontainer);

        const mobileBodyContent = visualContainer.querySelector('#mobileBodyContent');
        mobileBodyContent.appendChild(contentSnippets);

        document.getElementById('mobile-container-reference').appendChild(visualContainer);

        // ------------------------ Funcionalidad Menu ------------------------ //

        const mobileMenu = document.getElementById('mobile_menu');
        const burgerBtn = mobileMenu.querySelector('#burgerBtn');

        if (burgerBtn) {
            burgerBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('open-menu');

                if (mobileMenu.classList.contains('open-menu')) {
                    const closeMenu = () => {
                        mobileMenu.classList.remove('open-menu');
                        mobileBodyContent.removeEventListener('click', closeMenu);
                    };

                    mobileBodyContent.addEventListener('click', closeMenu);
                }
            });
        }

        const menuList = mobileMenu.querySelector('#menu_list');
        const activeItemSelector = urlName === 'services_view'
            ? `li[data-url="javascript:;"]`
            : `li[data-url="${currentPath}"]`;

        const activeItem = menuList.querySelector(activeItemSelector);
        if (activeItem) activeItem.classList.add('item-active');

        menuList.addEventListener('click', (event) => {
            const element = event.target.closest('li');
            if (!element || !element.dataset.url) return;

            menuList.querySelectorAll('li').forEach((item) => {
                item.classList.remove('item-active');
            });
            element.classList.add('item-active');

            const linkPath = element.dataset.url;
            if (window.location.pathname !== linkPath && linkPath) {
                element.addEventListener('transitionend', (transitionEvent) => {
                    if (transitionEvent.propertyName === 'background-position-x') {
                        window.location.href = linkPath;
                    }
                }, { once: true });
            } else {
                mobileMenu.classList.toggle('open-menu');
            }
        });

        // ------------------------ Funcionalidad modal submenu ------------------------ //

        document.querySelector('li[data-url="javascript:;"]').addEventListener('click', () => {
            document.querySelector('.container-modal-mobile').classList.add('show-modal');
        });

        document.querySelectorAll('.close-modal, .backdrop').forEach((element) => {
            element.addEventListener('click', () => {
                document.querySelector('.container-modal-mobile').classList.remove('show-modal');
                menuList.querySelectorAll('li').forEach((item) => {
                    item.classList.remove('item-active');
                });
                activeItem.classList.add('item-active');
            });
        });

        var listItemModal = document.querySelectorAll('.button-group-container');

        if (listItemModal) {
            listItemModal.forEach(element => {
                var elementA = element.querySelector(`a[href="${currentPath}"]`);
                if (elementA)
                    elementA.classList.add('active');
            });
        }

    }
})
