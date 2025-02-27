// Función para convertir de Hexadecimal a RGB
function hexToRgb(hex) {
    // Elimina el símbolo #
    hex = hex.replace('#', '');

    // Convertir el valor a R, G, B
    let r = parseInt(hex.substring(0, 2), 16);
    let g = parseInt(hex.substring(2, 4), 16);
    let b = parseInt(hex.substring(4, 6), 16);

    return { r, g, b };
}

// Función para convertir de RGB a HSL
function rgbToHsl(r, g, b) {
    r /= 255;
    g /= 255;
    b /= 255;

    let max = Math.max(r, g, b);
    let min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;

    if (max === min) {
        h = s = 0; // Es un gris
    } else {
        let d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r: h = (g - b) / d + (g < b ? 6 : 0); break;
            case g: h = (b - r) / d + 2; break;
            case b: h = (r - g) / d + 4; break;
        }
        h /= 6;
    }

    h = Math.round(h * 360);
    s = Math.round(s * 100);
    l = Math.round(l * 100);

    return { h, s, l };
}

// Función principal para convertir de Hex a HSL
function hexToHsl(hex) {
    // Convertir de Hex a RGB
    let { r, g, b } = hexToRgb(hex);

    // Convertir de RGB a HSL
    let { h, s, l } = rgbToHsl(r, g, b);

    return { h, s, l };
}

function convertHextoHsl() {
    let element = document.querySelector('.color-home a');
    const color = element.dataset.color
    let hslColor = hexToHsl(color);

    document.documentElement.style.setProperty('--btn-home-h', hslColor.h);
    document.documentElement.style.setProperty('--btn-home-s', `${hslColor.s}%`);
    document.documentElement.style.setProperty('--btn-home-l', `${hslColor.l}%`);
}

document.addEventListener('DOMContentLoaded', convertHextoHsl)