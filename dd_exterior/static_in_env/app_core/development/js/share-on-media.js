// const socialMedia = ['facebook', 'whatsapp', 'twitter', 'linkedin'];

const socialMedia = ['facebook', 'whatsapp'];

function formatPhoneNumber(phoneNumberInput) {
    var cleanedPhoneNumber = phoneNumberInput.replace(/\D/g, '');
    var formattedPhoneNumber = '(' + cleanedPhoneNumber.substring(0, 3) + ') ' +
        cleanedPhoneNumber.substring(3, 6) + '-' +
        cleanedPhoneNumber.substring(6);

    return formattedPhoneNumber;
}

function createShareButton(media, baseButton) {
    const button = baseButton.cloneNode(true);

    const tagA = button.tagName == 'A' ? button : button.querySelector('a');
    const tagI = tagA.querySelector('i');

    tagA.className = tagA.dataset.class;
    tagI.className = `${tagI.dataset.class}${media}`;

    tagA.addEventListener('click', function () {
        const { title, description, id: idServices, phone, email } = this.dataset;
        const url = `${window.location.href.split('#')[0]}${idServices}`;

        const tempElement = document.createElement('div');
        tempElement.innerHTML = description;
        const plainText = tempElement.textContent || tempElement.innerText;

        var encodeTitle = '', encodeDescription = '', encodeUrl = '', encodePhone = '', encodeEmail = '', message = '';

        let shareUrl = '';
        switch (media) {
            case 'facebook':
                encodeTitle = encodeURIComponent('👷🏼 *' + title + '*:\n\n');
                encodeDescription = encodeURIComponent(plainText + '\n\n');
                encodePhone = `📱 *Call us*: ${encodeURIComponent('\n* ' + formatPhoneNumber(phone) + '\n\n')}`;
                encodeEmail = `📧 *Contact us*: ${encodeURIComponent('\n* ' + email)}`;
                message = `${encodeTitle}${encodeDescription}${encodePhone}${encodeEmail}`;
                shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}&quote=${message}`;
                break;
            case 'twitter':
                shareUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title + ':  ' + plainText + '  ')}`;
                break;
            case 'linkedin':
                shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}&summary=${encodeURIComponent(plainText + '  ')}`;
                break;
            case 'whatsapp':
                encodeTitle = encodeURIComponent('👷🏼 *' + title + '*:\n\n');
                encodeDescription = encodeURIComponent(plainText + '\n\n');
                encodeUrl = `👇 *Visit our page*: ${encodeURIComponent('\n* ' + url + '\n\n')}`;
                encodePhone = `📱 *Call us*: ${encodeURIComponent('\n* ' + formatPhoneNumber(phone) + '\n\n')}`;
                encodeEmail = `📧 *Contact us*: ${encodeURIComponent('\n* ' + email)}`;
                message = `${encodeTitle}${encodeDescription}${encodeUrl}${encodePhone}${encodeEmail}`;
                shareUrl = `https://api.whatsapp.com/send?text=${message}`;
                break;
        }
        window.open(shareUrl, '_blank').focus();
    });

    button.style.display = 'inline';

    return button;
}

document.addEventListener('DOMContentLoaded', function () {

    const shareButtons = document.querySelectorAll('.share-buttons');

    shareButtons.forEach(button => {

        socialMedia.forEach(element => {
            const newButton = createShareButton(element, button)
            button.parentNode.appendChild(newButton);
        });

        if (window.getComputedStyle(button).display === 'none')
            button.remove();
    });

});
