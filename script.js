document.addEventListener("DOMContentLoaded", function() {
    const textElement = document.querySelector('.welcome-text');
    const homepageText = document.querySelector('.homepage-text');
    const aboutHeader = document.querySelector('.header'); // ABOUT 페이지의 헤더
    const buttons = document.querySelector('.buttons'); // 버튼
    const goalCards = document.querySelectorAll('.goal-card'); 
    let currentGoalIndex = 0;


    // HOME 페이지의 애니메이션
    if (window.location.pathname.endsWith('index.html')) { // HOME 페이지 확인
        // 타이핑 애니메이션이 끝났을 때 0.5초 후 서서히 더 많이 위로 이동
        textElement.addEventListener('animationend', function(event) {
            if (event.animationName === 'typing') {
                setTimeout(function() {
                    textElement.classList.add('move-up');
                    setTimeout(function() {
                        homepageText.classList.add('fade-in'); // 0.5초 후 'Jang Eunsu's Homepage' 나타남
                    }, 500);
                }, 500);
            }
        });

        // 페이지 로드 후 애니메이션 실행
        window.onload = function() {
            // Welcome 문구 타이핑 완료 후 이동
            setTimeout(function() {
                document.querySelector('.welcome-text').classList.add('move-up');
            }, 2500);

            // 'Jang Eunsu's Homepage'와 소셜 아이콘을 페이드인
            setTimeout(function() {
                document.querySelector('.homepage-text').classList.add('fade-in');
                document.querySelector('.social-icons').classList.add('fade-in');
            }, 3000); // 타이핑이 끝난 후 0.5초 후에 페이드인

            // JANG EUNSU 문구를 소셜 아이콘과 홈페이지 텍스트가 나타난 후 1초 뒤에 나타나게 설정
            setTimeout(function() {
                aboutHeader.style.opacity = '1'; // JANG EUNSU 문구를 즉시 나타나게 설정
                aboutHeader.style.visibility = 'visible'; // JANG EUNSU 문구를 항상 보이도록 설정
                buttons.style.opacity = '1'; // 버튼을 즉시 나타나게 설정
                buttons.style.visibility = 'visible'; // 버튼을 항상 보이도록 설정
            }, 4000);
        };
    } else if (window.location.pathname.endsWith('about.html')) { // ABOUT 페이지 확인
        // ABOUT 페이지는 즉시 나타나도록 설정
        aboutHeader.style.opacity = '1';
        aboutHeader.style.visibility = 'visible';
        buttons.style.opacity = '1';
        buttons.style.visibility = 'visible';
    } else if (window.location.pathname.endsWith('career.html')) { // CAREER 페이지 확인
        // CAREER 페이지는 즉시 나타나도록 설정
        aboutHeader.style.opacity = '1';
        aboutHeader.style.visibility = 'visible';
        buttons.style.opacity = '1';
        buttons.style.visibility = 'visible';
    } else if (window.location.pathname.endsWith('goal.html')) { // CAREER 페이지 확인
        // CAREER 페이지는 즉시 나타나도록 설정
        aboutHeader.style.opacity = '1';
        aboutHeader.style.visibility = 'visible';
        buttons.style.opacity = '1';
        buttons.style.visibility = 'visible';
    }
});

// script.js

const slides = document.querySelectorAll(".slide");
let currentSlide = 0;

function updateSlides() {
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
    currentSlide = (currentSlide + 1) % slides.length;
    updateSlides();
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    updateSlides();
}

// Initialize
updateSlides();
