document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Elements
const modal = document.getElementById('subscription-confirmation');
const closeButton = modal.querySelector('.close');
const subscribeForm = document.getElementById('subscribe-form');
const emailInput = document.getElementById('email');

// Function to Open Modal
function openModal() {
  modal.style.display = 'flex';
}

// Function to Close Modal
function closeModal() {
  modal.style.display = 'none';
}

// Function to Validate Email
function validateEmail(email) {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
  return emailPattern.test(email);
}

// Event Listener for Form Submission
subscribeForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission

  const email = emailInput.value.trim();

  if (validateEmail(email)) {
    openModal(); // Open modal if email is valid
    emailInput.value = ''; // Clear the input field
  } else {
    alert('Please enter a valid email address.');
    emailInput.focus(); // Focus the input field for correction
  }
});

// Event Listener for Closing Modal
closeButton.addEventListener('click', closeModal);

// Close Modal on Clicking Outside the Content
window.addEventListener('click', (event) => {
  if (event.target === modal) {
    closeModal();
  }
});


function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  navLinks.classList.toggle('show');
}

document.querySelector('.blog-filter').addEventListener('click', function () {
  this.classList.toggle('active');
});

// Elements
const commentForm = document.getElementById('comment-form');
const usernameInput = document.getElementById('username');
const commentInput = document.getElementById('comment');
const commentList = document.getElementById('comment-list');

// Function to Create Comment Element
function createComment(username, comment) {
  const commentItem = document.createElement('div');
  commentItem.classList.add('comment-item');

  const timestamp = new Date().toLocaleString(); // Get current timestamp

  commentItem.innerHTML = `
    <p class="username">${username}</p>
    <p class="timestamp">${timestamp}</p>
    <p class="comment-text">${comment}</p>
  `;

  return commentItem;
}

// Event Listener for Comment Submission
commentForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission

  const username = usernameInput.value.trim();
  const comment = commentInput.value.trim();

  // Validate inputs
  if (username && comment) {
    const newComment = createComment(username, comment);
    commentList.appendChild(newComment); // Add comment to the list
    usernameInput.value = ''; // Clear username input
    commentInput.value = ''; // Clear comment input
  } else {
    alert('Please fill in both fields.');
  }
});
function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  navLinks.classList.toggle('show');
}

// JavaScript for scroll-activated animation for the Journey Section

document.addEventListener('DOMContentLoaded', () => {
  const timelineEvents = document.querySelectorAll('.timeline-event');

  // Callback function for the Intersection Observer
  const revealTimelineEvent = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active'); // Add animation class
        observer.unobserve(entry.target); // Stop observing once activated
      }
    });
  };

  // Create an Intersection Observer instance
  const observer = new IntersectionObserver(revealTimelineEvent, {
    threshold: 0.5, // Trigger when 50% of the element is visible
  });

  // Observe each timeline event
  timelineEvents.forEach(event => {
    observer.observe(event);
  });
});

// Create a separate Intersection Observer for achievement cards
const achievementObserver = new IntersectionObserver(handleIntersection, {
  threshold: 0.5 // Trigger when 10% of the element is in view
});

// Observe each achievement card
const achievementCards = document.querySelectorAll('.achievement-card');
achievementCards.forEach(card => {
  achievementObserver.observe(card);
});