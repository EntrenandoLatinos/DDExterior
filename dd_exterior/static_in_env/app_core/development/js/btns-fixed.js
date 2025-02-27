function handleWindowScroll() {
    var scroll = window.pageYOffset || document.documentElement.scrollTop;
    if (scroll > 500) {
        groupBtnFixed.style.display = ''
        setTimeout(() => {
            groupBtnFixed.classList.add('active')
        }, 1);
    }
    else {
        groupBtnFixed.classList.remove('active')
    }
}

var groupBtnFixed = document.querySelector(".group-btn-fixed");

window.addEventListener('scroll', handleWindowScroll);

groupBtnFixed.addEventListener('transitionend', function (event) {
    if (event.propertyName === 'opacity') {
        var computedStyle = window.getComputedStyle(groupBtnFixed);
        var currentOpacity = computedStyle.getPropertyValue('opacity');
        if (currentOpacity == 0) {
            groupBtnFixed.style.display = 'none'
        }
    }
});

// Función para ajustar la cantidad de botones
function setButtonQuantity() {
    var elem = document.getElementById('group-btns-fixed');
    var multiplicador = elem.getAttribute('data-number-buttons');
    document.documentElement.style.setProperty('--cantidad-btns', multiplicador); 
}

function porcentaje() {
    var scrollTopBtn = document.querySelector('.btn-fixed-2.scrolltop');
    if (scrollTopBtn) {
    
        var progressPath = document.querySelector('.btn-fixed-2.scrolltop path');
        var pathLength = progressPath.getTotalLength();
    
        // Initial settings for the path
        progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
        progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
        progressPath.style.strokeDashoffset = pathLength;
        progressPath.getBoundingClientRect();
        progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
    
        // Update progress function
        var updateProgress = function () {
            var scroll = window.scrollY;
            var height = document.documentElement.scrollHeight - window.innerHeight;
            var progress = pathLength - (scroll * pathLength / height);
            progressPath.style.strokeDashoffset = progress;
        };
    
        updateProgress();
        window.addEventListener('scroll', updateProgress);
    
        // Show/hide scroll top button
        // var offset = 50;
        // var duration = 750;
    
        // window.addEventListener('scroll', function () {
        //     if (window.scrollY > offset) {
        //         scrollTopBtn.classList.add('show');
        //     } else {
        //         scrollTopBtn.classList.remove('show');
        //     }
        // });
    
    }
}


document.addEventListener('DOMContentLoaded', setButtonQuantity);
document.addEventListener('DOMContentLoaded', porcentaje);
