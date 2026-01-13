// SpaceCrafter Landing Page - Shopify Compatible JavaScript

(function() {
  'use strict';

  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    setupSmoothScroll();
    setupIntersectionObserver();
    setupFormValidation();
    console.log('SpaceCrafter landing page initialized');
  }

  // Smooth scroll for anchor links
  function setupSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#sc-"]');

    links.forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const target = document.querySelector(targetId);

        if (target) {
          const offset = 80; // Shopify header offset
          const targetPosition = target.offsetTop - offset;

          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  // Intersection Observer for scroll animations
  function setupIntersectionObserver() {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // Observe elements
    const animateElements = document.querySelectorAll(
      '.sc-service-card, .sc-process-step, .sc-case-study, .sc-testimonial'
    );

    animateElements.forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
      observer.observe(el);
    });
  }

  // Form validation
  function setupFormValidation() {
    const form = document.querySelector('.sc-cta-form');
    if (!form) return;

    const inputs = form.querySelectorAll('input, select, textarea');

    inputs.forEach(input => {
      input.addEventListener('blur', function() {
        validateField(this);
      });

      input.addEventListener('input', function() {
        if (this.classList.contains('sc-error')) {
          validateField(this);
        }
      });
    });
  }

  function validateField(field) {
    const value = field.value.trim();
    let isValid = true;

    // Check required fields
    if (field.hasAttribute('required') && !value) {
      isValid = false;
    }

    // Email validation
    if (field.type === 'email' && value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      isValid = emailRegex.test(value);
    }

    // Phone validation
    if (field.type === 'tel' && value) {
      const phoneRegex = /^[\d\s\-\+\(\)]+$/;
      isValid = phoneRegex.test(value);
    }

    // Update field appearance
    if (!isValid) {
      field.classList.add('sc-error');
      field.style.borderColor = '#ef4444';
    } else {
      field.classList.remove('sc-error');
      field.style.borderColor = '';
    }

    return isValid;
  }

  // Stats counter animation (if stats are visible)
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const statNumbers = entry.target.querySelectorAll('.sc-stat-number');
        statNumbers.forEach(stat => {
          animateCounter(stat);
        });
        statsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  const heroStats = document.querySelector('.sc-hero-stats');
  if (heroStats) {
    statsObserver.observe(heroStats);
  }

  function animateCounter(element) {
    const text = element.textContent;
    const number = parseInt(text.replace(/\D/g, ''));

    if (!number || element.classList.contains('animated')) return;

    element.classList.add('animated');
    const suffix = text.replace(/[\d,]/g, '');
    const duration = 2000;
    const increment = number / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= number) {
        element.textContent = number + suffix;
        clearInterval(timer);
      } else {
        element.textContent = Math.floor(current) + suffix;
      }
    }, 16);
  }

})();
