//preloader
document.addEventListener("DOMContentLoaded", function () {
    // El contenedor donde agregar los span
    const txtLoadingContainer = document.getElementById("txt-loading");
    if (txtLoadingContainer) {
        const title = txtLoadingContainer.dataset.title;

        // Crear un nuevo elemento style
        const style = document.createElement("style");
        document.head.appendChild(style);
        const sheet = style.sheet;

        // Separar el título en caracteres y crear un span para cada uno
        for (let i = 0; i < title.length; i++) {
            const char = title[i];
            const span = document.createElement("span");
            span.classList.add("characters");
            span.setAttribute("preloader-text", char);
            span.textContent = char;
            txtLoadingContainer.appendChild(span);

            // Agregar las reglas CSS para la animación
            const delay = (i * 0.05).toFixed(2);
            sheet.insertRule(`
            .th-preloader-2 .animation-preloader .txt-loading .characters:nth-child(${i + 1}):before {
                animation-delay: ${delay}s;
            }
            `, sheet.cssRules.length);
        }


        const words = title.split(' ')
        let charCount = 0;
        words.forEach((word, index) => {
            charCount += word.length;
            if (word.length >= 12) {
                // Antes de la palabra
                const longword = txtLoadingContainer.querySelector(`.txt-loading :nth-child(${charCount + index - word.length})`)
                // Despues de la palabra
                // const longword = txtLoadingContainer.querySelector(`.txt-loading :nth-child(${charCount + index + 1})`)
                const br = document.createElement("br");
                longword.appendChild(br);
            }
        });
    }

    window.addEventListener('load', function () {
        // Ocultar el pre-cargador después de 600 ms y luego desvanecerlo en 500 ms
        setTimeout(function () {
            const preLoadDev = document.getElementById("pre-load-dev");
            if (preLoadDev) {
                preLoadDev.style.transition = "opacity 500ms";
                preLoadDev.style.opacity = 0;
                preLoadDev.addEventListener('transitionend', function (event) {
                    if (event.propertyName === 'opacity') {
                        var computedStyle = window.getComputedStyle(preLoadDev);
                        var currentOpacity = computedStyle.getPropertyValue('opacity');
                        if (currentOpacity == 0) {
                            preLoadDev.style.display = 'none'
                        }
                    }
                });
            }

            const preLoader = document.querySelector(".pre-loader");
            if (preLoader) {
                preLoader.style.transition = "opacity 500ms";
                preLoader.style.opacity = 0;
                preLoader.addEventListener('transitionend', function (event) {
                    if (event.propertyName === 'opacity') {
                        var computedStyle = window.getComputedStyle(preLoader);
                        var currentOpacity = computedStyle.getPropertyValue('opacity');
                        if (currentOpacity == 0) {
                            preLoader.style.display = 'none'
                        }
                    }
                });
            }
        }, 600);
    });

});

