document.addEventListener('DOMContentLoaded', function () {
    function sendEmail(button) {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const { company, title, email } = this.dataset;

            const encodeTitle = encodeURIComponent('👷🏼 ' + title);
            const encondeMessage = encodeURIComponent(`👋🏼 Hello! \n\n👷🏼${company} \n\nI want to know more about your ${title}.\n\nCould you provide me with more details?`)
            const shareUrl = `mailto:${email}?subject=${encodeTitle}&body=${encondeMessage}`;

            window.open(shareUrl, '_blank').focus();
        })
    }

    document.querySelectorAll('.send-email').forEach(button => {
        sendEmail(button)
    });

});