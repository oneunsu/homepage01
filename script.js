document.addEventListener("DOMContentLoaded", function () {
    const textElement = document.querySelector('.welcome-text');
    const homepageText = document.querySelector('.homepage-text');
    const socialIcons = document.querySelector('.social-icons');
    const aboutHeader = document.querySelector('.header');
    const buttons = document.querySelector('.buttons');

    const path = window.location.pathname;
    const isHomePage =
        path.endsWith('/homepage01/') ||
        path.endsWith('/homepage01/index.html') ||
        path === '/' ||
        path.endsWith('/index.html');

    if (isHomePage) {
        if (textElement) {
            textElement.addEventListener('animationend', function (event) {
                if (event.animationName === 'typing') {
                    setTimeout(function () {
                        textElement.classList.add('move-up');

                        setTimeout(function () {
                            if (homepageText) homepageText.classList.add('fade-in');
                            if (socialIcons) socialIcons.classList.add('fade-in');
                        }, 500);

                        setTimeout(function () {
                            if (aboutHeader) {
                                aboutHeader.style.opacity = '1';
                                aboutHeader.style.visibility = 'visible';
                            }
                            if (buttons) {
                                buttons.style.opacity = '1';
                                buttons.style.visibility = 'visible';
                            }
                        }, 1000);
                    }, 500);
                }
            });
        }
    } else if (
        path.endsWith('about.html') ||
        path.endsWith('career.html') ||
        path.endsWith('goal.html')
    ) {
        if (aboutHeader) {
            aboutHeader.style.opacity = '1';
            aboutHeader.style.visibility = 'visible';
        }
        if (buttons) {
            buttons.style.opacity = '1';
            buttons.style.visibility = 'visible';
        }
    }

    const slides = document.querySelectorAll(".slide");
    let currentSlide = 0;

    function updateSlides() {
        if (!slides.length) return;

        slides.forEach((slide, index) => {
            slide.classList.remove("active");
            slide.style.transform = "scale(0.8)";
            slide.style.opacity = "0.5";

            if (index === currentSlide) {
                slide.classList.add("active");
                slide.style.transform = "scale(1)";
                slide.style.opacity = "1";
            }
        });
    }

    function nextSlide() {
        if (!slides.length) return;
        currentSlide = (currentSlide + 1) % slides.length;
        updateSlides();
    }

    function prevSlide() {
        if (!slides.length) return;
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        updateSlides();
    }

    window.nextSlide = nextSlide;
    window.prevSlide = prevSlide;

    updateSlides();
});
