const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');
const modal = document.getElementById('subscription-confirmation');
const closeBtn = modal ? modal.querySelector('.close') : null;
const subscribeForm = document.getElementById('subscribe-form');
const emailInput = subscribeForm ? subscribeForm.querySelector('input[type="email"]') : null;

// Mobile menu functionality
if (hamburger && navLinks) {
  hamburger.addEventListener('click', function () {
    navLinks.classList.toggle('active');
  });

  document.addEventListener('click', function (event) {
    if (!hamburger.contains(event.target) && !navLinks.contains(event.target)) {
      navLinks.classList.remove('active');
    }
  });
}

// Theme toggling functionality
const themeToggle = document.getElementById('theme-toggle');
if (themeToggle) {
  const icon = themeToggle.querySelector('i');
  const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
  const savedTheme = localStorage.getItem('theme');

  if (savedTheme === 'dark' || (!savedTheme && prefersDarkScheme.matches)) {
    document.body.classList.add('dark-theme');
    if (icon) icon.classList.replace('fa-moon', 'fa-sun');
  }

  themeToggle.addEventListener('click', function () {
    document.body.classList.toggle('dark-theme');

    // Update icon
    if (icon) {
      if (document.body.classList.contains('dark-theme')) {
        icon.classList.replace('fa-moon', 'fa-sun');
        localStorage.setItem('theme', 'dark');
      } else {
        icon.classList.replace('fa-sun', 'fa-moon');
        localStorage.setItem('theme', 'light');
      }
    }
  });
}

// Query for filter items across all pages
const filterItems = document.querySelectorAll('[data-category], [data-filter]');
const filterableCards = document.querySelectorAll('[data-category], [data-type]');

if (filterItems.length > 0 && filterableCards.length > 0) {
  filterItems.forEach(item => {
    item.addEventListener('click', function (event) {
      // Find all related filter buttons in the same container
      if (event.target.tagName === 'A' ||
        event.target.closest('a') ||
        event.target.classList.contains('fa-chevron-right')) {
        return;
      }
      const filterContainer = findFilterContainer(this);
      const relatedFilters = filterContainer ?
        filterContainer.querySelectorAll('[data-category], [data-filter]') :
        document.querySelectorAll('[data-category], [data-filter]');

      // Update active class
      relatedFilters.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      // Get filter value (support both data-category and data-filter attributes)
      const filterValue = this.getAttribute('data-category') || this.getAttribute('data-filter');

      // Find cards that should be affected by this filter
      const targetCards = getTargetCards(this);

      // Apply filtering
      targetCards.forEach(card => {
        // Get card's category (support both data-category and data-type)
        const cardCategory = card.getAttribute('data-category') || card.getAttribute('data-type');
        // Get card's natural display style
        const naturalDisplay = card.dataset.naturalDisplay ||
          (getComputedStyle(card).display === 'none' ? 'flex' : getComputedStyle(card).display);

        // Store natural display value if not already stored
        if (!card.dataset.naturalDisplay) {
          card.dataset.naturalDisplay = naturalDisplay;
        }

        // Show/hide based on filter
        if (filterValue === 'all' || cardCategory === filterValue) {
          card.style.display = naturalDisplay;
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Helper function to find the parent filter container
  function findFilterContainer(filterItem) {
    let parent = filterItem.parentElement;
    while (parent) {
      if (parent.classList.contains('filter-options') ||
        parent.classList.contains('events-filter') ||
        parent.classList.contains('filter-container') ||
        parent.classList.contains('blog-filter-section')) {
        return parent;
      }
      parent = parent.parentElement;
    }
    return null;
  }

  // Helper function to find cards that should be filtered by this button
  function getTargetCards(filterItem) {
    // Determine which cards to filter based on context
    if (filterItem.closest('.blog-filter-section')) {
      return document.querySelectorAll('.blog-card');
    } else if (filterItem.closest('.events-filter')) {
      return document.querySelectorAll('.event-card');
    } else {
      // Find closest common parent or fallback to all filterable cards
      const section = filterItem.closest('section');
      return section ?
        section.querySelectorAll('[data-category], [data-type]') :
        filterableCards;
    }
  }

  // Initialize filters - activate the first "all" filter if present
  const allFilterButtons = document.querySelectorAll('[data-category="all"], [data-filter="all"]');
  if (allFilterButtons.length > 0) {
    // For each filter group, activate the "all" button
    const processedContainers = new Set();

    allFilterButtons.forEach(button => {
      const container = findFilterContainer(button);
      if (container && !processedContainers.has(container)) {
        button.click(); // Simulate click to apply filtering
        processedContainers.add(container);
      }
    });
  }
}


// Modal functionality
function openModal() {
  if (modal) modal.style.display = 'flex';
}

function closeModal() {
  if (modal) modal.style.display = 'none';
}

// Function to Validate Email
const validateEmail = (email) => {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);
};

// Subscription form handling
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
}

// Modal close button
if (closeBtn) {
  closeBtn.addEventListener('click', closeModal);
}

// Close modal when clicking outside
if (modal) {
  window.addEventListener('click', (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });
}