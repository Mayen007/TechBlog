var calendarEl = document.getElementById('calendar');
if (calendarEl) {
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    events: '/api/events'
  });
  calendar.render();
} else {
  console.error("Calendar element not found!");
}

const filterItems = document.querySelectorAll(".filter-item");
const postCards = document.querySelectorAll(".post-card");

filterItems.forEach((filter) => {
  filter.addEventListener("click", (e) => {
    filterItems.forEach((item) => item.classList.remove("active"));

    e.target.classList.add("active");

    const selectedCategory = e.target.getAttribute("data-category");

    postCards.forEach((post) => {
      const postCategory = post.getAttribute("data-category");

      if (selectedCategory === "all" || postCategory === selectedCategory) {
        post.style.display = "block";
      } else {
        post.style.display = "none";
      }
    });
  });
});

// Carousel Functionality
document.addEventListener('DOMContentLoaded', () => {
  const carousel = document.querySelector('.events-carousel');
  const slides = document.querySelectorAll('.event-slide');
  const dots = document.querySelectorAll('.dot');
  const prevButton = document.querySelector('.carousel-control.prev');
  const nextButton = document.querySelector('.carousel-control.next');
  let currentIndex = 0;
  let autoPlayInterval;

  function updateCarousel() {
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
    dots.forEach(dot => dot.classList.remove('active'));
    dots[currentIndex].classList.add('active');
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateCarousel();
  }

  function startAutoPlay() {
    autoPlayInterval = setInterval(nextSlide, 5000);
  }

  function stopAutoPlay() {
    clearInterval(autoPlayInterval);
  }

  // Event Listeners
  nextButton.addEventListener('click', () => {
    stopAutoPlay();
    nextSlide();
  });

  prevButton.addEventListener('click', () => {
    stopAutoPlay();
    prevSlide();
  });

  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      stopAutoPlay();
      currentIndex = index;
      updateCarousel();
    });
  });

  // Pause on hover
  carousel.addEventListener('mouseenter', stopAutoPlay);
  carousel.addEventListener('mouseleave', startAutoPlay);

  // Initialize autoplay
  startAutoPlay();
});

// Elements
const modal = document.getElementById('subscription-confirmation');
const closeButton = modal ? modal.querySelector('.close') : null;
const subscribeForm = document.getElementById('subscribe-form');
const emailInput = document.getElementById('email');

// Function to Open Modal
const openModal = () => {
  if (modal) {
    modal.style.display = 'flex';
  } else {
    console.error("Modal element with ID 'subscription-confirmation' not found.");
  }
};

// Function to Close Modal
const closeModal = () => {
  if (modal) {
    modal.style.display = 'none';
  }
};

// Function to Validate Email
const validateEmail = (email) => {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);
};

if (subscribeForm && emailInput) {
  subscribeForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const email = emailInput.value.trim();

    if (validateEmail(email)) {
      openModal();
      emailInput.value = '';
    } else {
      alert('Please enter a valid email address.');
      emailInput.focus();
    }
  });
} else {
  console.error("Subscription form or email input not found.");
}

if (closeButton) {
  closeButton.addEventListener('click', closeModal);
} else {
  console.error("Close button not found in the modal.");
}

if (modal) {
  window.addEventListener('click', (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });
}

// Toggle Menu
function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  navLinks.classList.toggle('show');
}

const themeToggleButton = document.querySelector('.theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const savedTheme = localStorage.getItem('theme');

// Apply saved theme on page load
if (savedTheme === 'dark') {
  document.body.classList.add('dark');
  themeIcon.className = 'fa-solid fa-sun';
  themeToggleButton.classList.add('dark');
}

// Attach event listener to the button
themeToggleButton.addEventListener('click', function () {
  const isDarkMode = document.body.classList.toggle('dark');
  themeIcon.className = isDarkMode ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  themeToggleButton.classList.toggle('dark');
  localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
});
