document.addEventListener("DOMContentLoaded", () => {
    if (!window.djangoData) {
        console.error("No Django data found!");
        return;
    }

    const { contact } = window.djangoData;

    function formatPhoneNumber(phoneNumberInput) {
        var cleanedPhoneNumber = phoneNumberInput.replace(/\D/g, '');
        var formattedPhoneNumber = '(' + cleanedPhoneNumber.substring(0, 3) + ') ' +
            cleanedPhoneNumber.substring(3, 6) + '-' +
            cleanedPhoneNumber.substring(6);

        return formattedPhoneNumber;
    }

    const telCliente = formatPhoneNumber(contact.phone1);
    const contactPhones = document.querySelectorAll(".contact-phone-1");
    contactPhones.forEach(function (item) {
        item.textContent = telCliente;
        item.href = "tel:" + contact.phone1;
    });

    const simplePhones = document.querySelectorAll(".number-phone-1");
    simplePhones.forEach(function (item) {
        item.textContent = telCliente;
    });

    const telCliente2 = formatPhoneNumber(contact.phone2);
    const contactPhones2 = document.querySelectorAll(".contact-phone-2");
    contactPhones2.forEach(function (item) {
        item.textContent = telCliente2;
        item.href = "tel:" + contact.phone2;
    });

    const simplePhones2 = document.querySelectorAll(".number-phone-2");
    simplePhones2.forEach(function (item) {
        item.textContent = telCliente2;
    });

    const hrfPhones = document.querySelectorAll(".hrf-phone");
    hrfPhones.forEach(function (item) {
        item.href = "tel:" + contact.phone1;
    });
})