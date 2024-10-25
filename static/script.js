document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

const subscribeForm = document.querySelector('.subscribe-form');
const subscribeMessage = document.getElementById('subscribe-message');

subscribeForm.addEventListener('submit', function (e) {
  e.preventDefault();  // Prevent the form from refreshing the page

  // Simulate subscription success
  subscribeMessage.textContent = 'Thanks for subscribing! Stay tuned for updates.';
  subscribeMessage.style.visibility = 'visible';
  subscribeMessage.style.opacity = '0';
  subscribeMessage.style.transition = 'opacity 0.5s ease-in-out';

  setTimeout(() => {
    subscribeMessage.style.opacity = '1'; // Fade in the success message
  }, 100);

  // Clear the input field
  document.getElementById('email').value = '';
});

function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  navLinks.classList.toggle('show');
}

document.querySelector('.blog-filter').addEventListener('click', function () {
  this.classList.toggle('active');
});
