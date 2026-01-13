// ===================================
// Smooth Scroll & Navigation
// ===================================

// Add scroll effect to navbar
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = target.offsetTop - navbarHeight;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ===================================
// Mobile Menu Toggle
// ===================================

const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('mobile-active');
        mobileMenuToggle.classList.toggle('active');

        // Toggle aria-expanded for accessibility
        const isExpanded = mobileMenuToggle.getAttribute('aria-expanded') === 'true';
        mobileMenuToggle.setAttribute('aria-expanded', !isExpanded);
    });

    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('mobile-active');
            mobileMenuToggle.classList.remove('active');
            mobileMenuToggle.setAttribute('aria-expanded', 'false');
        });
    });
}

// ===================================
// Intersection Observer for Animations
// ===================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe elements for animation
const animateOnScroll = document.querySelectorAll(
    '.service-card, .process-step, .case-study, .testimonial, .why-feature'
);

animateOnScroll.forEach(el => {
    observer.observe(el);
});

// ===================================
// Form Handling
// ===================================

const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Get form data
        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData.entries());

        // Get submit button
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.textContent;

        // Disable button and show loading state
        submitButton.disabled = true;
        submitButton.textContent = 'Sending...';

        try {
            // Simulate form submission (replace with actual API call)
            await simulateFormSubmission(data);

            // Show success message
            showSuccessMessage();

            // Reset form
            contactForm.reset();

            // Track conversion (if analytics is set up)
            if (typeof gtag !== 'undefined') {
                gtag('event', 'form_submission', {
                    'event_category': 'Contact',
                    'event_label': 'Consultation Request'
                });
            }

        } catch (error) {
            // Show error message
            showErrorMessage();
            console.error('Form submission error:', error);
        } finally {
            // Re-enable button
            submitButton.disabled = false;
            submitButton.textContent = originalButtonText;
        }
    });
}

// Simulate form submission (replace with actual API endpoint)
function simulateFormSubmission(data) {
    return new Promise((resolve) => {
        console.log('Form data submitted:', data);
        // In production, replace this with:
        // fetch('/api/contact', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(data)
        // });
        setTimeout(resolve, 1500);
    });
}

// Show success message
function showSuccessMessage() {
    const existingMessage = document.querySelector('.form-message');
    if (existingMessage) {
        existingMessage.remove();
    }

    const successMessage = document.createElement('div');
    successMessage.className = 'form-success form-message';
    successMessage.innerHTML = `
        <strong>Thank you!</strong> We've received your consultation request.
        Our team will reach out within 24 hours.
    `;

    contactForm.insertAdjacentElement('afterend', successMessage);

    // Scroll to message
    successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Remove message after 5 seconds
    setTimeout(() => {
        successMessage.remove();
    }, 5000);
}

// Show error message
function showErrorMessage() {
    const existingMessage = document.querySelector('.form-message');
    if (existingMessage) {
        existingMessage.remove();
    }

    const errorMessage = document.createElement('div');
    errorMessage.className = 'form-error form-message';
    errorMessage.style.cssText = `
        background: #ef4444;
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        margin-top: 20px;
    `;
    errorMessage.innerHTML = `
        <strong>Oops!</strong> Something went wrong. Please try again or email us directly at
        <a href="mailto:hello@spacecrafter.studio" style="color: white; text-decoration: underline;">
            hello@spacecrafter.studio
        </a>
    `;

    contactForm.insertAdjacentElement('afterend', errorMessage);

    // Remove message after 7 seconds
    setTimeout(() => {
        errorMessage.remove();
    }, 7000);
}

// ===================================
// Form Validation Enhancement
// ===================================

// Add real-time validation feedback
const formInputs = document.querySelectorAll('.cta-form input, .cta-form select, .cta-form textarea');

formInputs.forEach(input => {
    input.addEventListener('blur', function() {
        validateField(this);
    });

    input.addEventListener('input', function() {
        if (this.classList.contains('error')) {
            validateField(this);
        }
    });
});

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;

    // Check if required field is empty
    if (field.hasAttribute('required') && !value) {
        isValid = false;
    }

    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        isValid = emailRegex.test(value);
    }

    // Phone validation (optional, basic)
    if (field.type === 'tel' && value) {
        const phoneRegex = /^[\d\s\-\+\(\)]+$/;
        isValid = phoneRegex.test(value);
    }

    // Update field appearance
    if (!isValid) {
        field.classList.add('error');
        field.style.borderColor = '#ef4444';
    } else {
        field.classList.remove('error');
        field.style.borderColor = '';
    }

    return isValid;
}

// ===================================
// Stats Counter Animation
// ===================================

function animateCounter(element, target) {
    const duration = 2000; // 2 seconds
    const start = 0;
    const increment = target / (duration / 16); // 60fps
    let current = start;

    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current);
        }
    }, 16);
}

// Trigger counter animation when stats come into view
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statNumbers = entry.target.querySelectorAll('.stat-number');
            statNumbers.forEach(stat => {
                const text = stat.textContent;
                const number = parseInt(text.replace(/\D/g, ''));
                if (number && !stat.classList.contains('animated')) {
                    stat.classList.add('animated');
                    const suffix = text.replace(/[\d,]/g, '');
                    animateCounter(stat, number);
                    stat.textContent += suffix;
                }
            });
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const heroStats = document.querySelector('.hero-stats');
if (heroStats) {
    statsObserver.observe(heroStats);
}

// ===================================
// Client Logo Animation
// ===================================

const clientLogos = document.querySelector('.client-logos');
if (clientLogos) {
    // Add subtle parallax effect on hover
    clientLogos.addEventListener('mousemove', (e) => {
        const logos = clientLogos.querySelectorAll('.client-logo');
        const rect = clientLogos.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;

        logos.forEach((logo, index) => {
            const strength = (index + 1) * 2;
            logo.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
        });
    });

    clientLogos.addEventListener('mouseleave', () => {
        const logos = clientLogos.querySelectorAll('.client-logo');
        logos.forEach(logo => {
            logo.style.transform = 'translate(0, 0)';
        });
    });
}

// ===================================
// Lazy Loading Images
// ===================================

// When you add actual images, uncomment this section
/*
const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.add('loaded');
            imageObserver.unobserve(img);
        }
    });
});

document.querySelectorAll('img[data-src]').forEach(img => {
    imageObserver.observe(img);
});
*/

// ===================================
// Performance Optimization
// ===================================

// Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add passive event listeners for better scroll performance
if ('addEventListener' in window) {
    window.addEventListener('scroll', debounce(() => {
        // Scroll-dependent functions here
    }, 100), { passive: true });
}

// ===================================
// Accessibility Enhancements
// ===================================

// Keyboard navigation for cards
const interactiveCards = document.querySelectorAll('.service-card, .case-study, .testimonial');

interactiveCards.forEach(card => {
    card.setAttribute('tabindex', '0');

    card.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            card.click();
        }
    });
});

// Focus visible styles
document.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
        document.body.classList.add('keyboard-nav');
    }
});

document.addEventListener('mousedown', () => {
    document.body.classList.remove('keyboard-nav');
});

// ===================================
// Console Message (Optional - remove in production)
// ===================================

console.log('%cSpaceCrafter Studio', 'font-size: 24px; font-weight: bold; color: #2563eb;');
console.log('%cBuilt with care for coworking space operators', 'font-size: 14px; color: #64748b;');
console.log('%cInterested in working with us? Visit www.spacecrafter.studio', 'font-size: 12px; color: #94a3b8;');

// ===================================
// Initialize on DOM Load
// ===================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('SpaceCrafter Studio landing page loaded successfully');

    // Add loaded class for CSS animations
    document.body.classList.add('loaded');

    // Preload critical images (when you add them)
    // preloadImages(['hero.jpg', 'case-study-1.jpg']);
});
