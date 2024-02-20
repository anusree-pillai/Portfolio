$('.navToggle').on('click', function (e) {
  e.preventDefault();
  $('body').toggleClass('navToggleActive');
});


$(window).scroll(function(){
  if ($(this).scrollTop() > 10) {
    $('body').addClass('fixedHeader');
  } else {
    $('body').removeClass('fixedHeader');
  }
});


var swiper = new Swiper(".testimonialSwiper", {
  navigation: {
    nextEl: ".test-swiper-button-next",
    prevEl: ".test-swiper-button-prev",
  },
});


var swiper = new Swiper(".certificatesSlider", {
  slidesPerView: 1,
  spaceBetween: 16,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".cert-swiper-button-next",
    prevEl: ".cert-swiper-button-prev",
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    1024: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
  },
});
// Initialize Swiper slider for projects
var projectSwiper = new Swiper(".projectSlider", {
  slidesPerView: 1, // Number of slides per view
  spaceBetween: 20, // Space between slides (adjust as needed)
  navigation: {
    nextEl: ".project-swiper-button-next", // Next button selector
    prevEl: ".project-swiper-button-prev", // Previous button selector
  },
  breakpoints: {
    // Responsive breakpoints for different screen sizes
    640: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});
document.addEventListener('DOMContentLoaded', function () {
  new Glide('.glide', {
      type: 'carousel',
      perView: 1,
      focusAt: 'center',
      autoplay: 3000, // Set to 0 for no autoplay
  }).mount();
});

