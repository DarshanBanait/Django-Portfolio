document.addEventListener('DOMContentLoaded', function() {
    const introSection = document.getElementById('intro');
    introSection.style.opacity = 0;
    introSection.style.transition = 'opacity 2s';

    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY;
        if (scrollPosition > 50) {
            introSection.style.opacity = 1;
        } else {
            introSection.style.opacity = 0;
        }
    });
});