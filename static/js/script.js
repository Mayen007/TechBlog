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
} else {
  console.error("Subscription form or email input not found.");
}

// Event Listener for Closing Modal
if (closeButton) {
  closeButton.addEventListener('click', closeModal);
} else {
  console.error("Close button not found in the modal.");
}

// Close Modal on Clicking Outside the Content
if (modal) {
  window.addEventListener('click', (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });
}



// Comment Logic
// const commentForm = document.getElementById('comment-form');
// const usernameInput = document.getElementById('username');
// const commentInput = document.getElementById('comment');
// const commentList = document.getElementById('comment-list');

// function createComment(username, comment) {
//   const commentItem = document.createElement('div');
//   commentItem.classList.add('comment-item');

//   const timestamp = new Date().toLocaleString();

//   commentItem.innerHTML = `
//     <p class="username">${username}</p>
//     <p class="timestamp">${timestamp}</p>
//     <p class="comment-text">${comment}</p>
//   `;

//   return commentItem;
// }

// commentForm.addEventListener('submit', (event) => {
//   event.preventDefault();

//   const username = usernameInput.value.trim();
//   const comment = commentInput.value.trim();

//   if (username && comment) {
//     const newComment = createComment(username, comment);
//     commentList.appendChild(newComment);
//     usernameInput.value = '';
//     commentInput.value = '';
//   } else {
//     alert('Please fill in both fields.');
//   }
// });

// Toggle Menu
function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  navLinks.classList.toggle('show');
}

const commentForm = document.getElementById("comment-form");

commentForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.querySelector("[name='username']").value.trim();
  const content = document.querySelector("[name='content']").value.trim();

  if (!username || !content) {
    alert("Please fill out both fields.");
    return;
  }

  const commentList = document.getElementById("comment-list");

  // Create new comment element
  const newComment = document.createElement("div");
  newComment.classList.add("comment");
  newComment.innerHTML = `
      <div class="comment-header">
        <div class="avatar">${username[0].toUpperCase()}</div>
        <h3>${username}</h3>
      </div>
      <p class="comment-content">${content}</p>
      <p class="comment-date">${new Date().toLocaleString("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  })}</p>
    `;

  // Append the new comment to the list
  commentList.prepend(newComment);

  // Optionally clear the form inputs
  commentForm.reset();
});