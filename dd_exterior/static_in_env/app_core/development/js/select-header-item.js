document.addEventListener("DOMContentLoaded", () => {
    if (!window.djangoData) {
        console.error("No Django data found!");
        return;
    }

    const { currentPath, urlName } = window.djangoData;

    var listMenuHeader = document.querySelectorAll('ul.list-menu'); // Ajustar acorde al template

    if (listMenuHeader) {
        listMenuHeader.forEach(element => {
            var elementA = element.querySelector(urlname == 'services_view' ? `a[href="javascript:;"]` : `a[href="${currentPath}"]`);
            var parentElement = elementA.parentElement;
            parentElement.classList.add('current'); // Ajustar acorde al template
        });
    }

})