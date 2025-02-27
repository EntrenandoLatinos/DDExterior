
const updateProgress = (element, percent) => element.textContent = `${percent}%`;


function animateProgress(_elements, _percents, _interval = 50) {
    const maxTargetPercent = Math.max(..._percents);
    let currentPercent = 0;

    const interval = setInterval(() => {
        currentPercent++;
        _elements.forEach((element, index) => {
            const targetPercent = _percents[index];
            const progress = (currentPercent / maxTargetPercent) * targetPercent;
            updateProgress(element, parseInt(progress));
        });

        if (currentPercent >= maxTargetPercent) {
            clearInterval(interval);
        }
    }, _interval);
}

window.addEventListener('load', () => {
    const container = document.getElementById('section_counters_one');
    if (container) {
        const targetInterval = parseInt(container.getAttribute('data-target-interval'));
        const progressRings = document.querySelectorAll('.progress-value');
        const targetPercents = Array.from(progressRings).map(
            (container) => parseInt(container.getAttribute('data-target-percent'))
        );

        animateProgress(progressRings, targetPercents, targetInterval);
    }
    else return true

});