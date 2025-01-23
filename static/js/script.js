// document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//   anchor.addEventListener('click', function (e) {
//     const targetId = this.getAttribute('href');
//     if (targetId === "#") {
//       return;
//     }

//     e.preventDefault();
//     const targetElement = document.querySelector(targetId);

//     if (targetElement) {
//       targetElement.scrollIntoView({
//         behavior: 'smooth',
//       });
//     }
//   });
// });

// Elements
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
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
  return emailPattern.test(email);
};

// Event Listener for Form Submission
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

// const commentForm = document.getElementById("comment-form");

// commentForm.addEventListener("submit", function (event) {
//   event.preventDefault();

//   const username = document.querySelector("[name='username']").value.trim();
//   const content = document.querySelector("[name='content']").value.trim();

//   if (!username || !content) {
//     alert("Please fill out both fields.");
//     return;
//   }

//   const commentList = document.getElementById("comment-list");

//   const newComment = document.createElement("div");
//   newComment.classList.add("comment");
//   newComment.innerHTML = `
//       <div class="comment-header">
//         <div class="avatar">${username[0].toUpperCase()}</div>
//         <h3>${username}</h3>
//       </div>
//       <p class="comment-content">${content}</p>
//       <p class="comment-date">${new Date().toLocaleString("en-US", {
//     month: "long",
//     day: "numeric",
//     year: "numeric",
//     hour: "2-digit",
//     minute: "2-digit",
//   })}</p>
//     `;
//   commentList.prepend(newComment);

//   commentForm.reset();
// });

// Function to toggle theme

const themeToggleButton = document.querySelector('.theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const savedTheme = localStorage.getItem('theme');

// Apply saved theme on page load
if (savedTheme === 'dark') {
  document.body.classList.add('dark');
  themeIcon.className = 'fa-solid fa-sun'; // Update to sun for dark mode
  themeToggleButton.classList.add('dark'); // Change button style
}

// Attach event listener to the button
themeToggleButton.addEventListener('click', function () {
  const isDarkMode = document.body.classList.toggle('dark');
  themeIcon.className = isDarkMode ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  themeToggleButton.classList.toggle('dark');
  localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
});