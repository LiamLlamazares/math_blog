
document.addEventListener("DOMContentLoaded", function() {
  const tocContainer = document.getElementById('toc');
  const content = document.querySelector('.post-content');

  if (!tocContainer || !content) {
    return;
  }

  const headings = Array.from(content.querySelectorAll('h1, h2, h3, h4, h5, h6'));
  if (headings.length === 0) {
    const tocSidebar = document.querySelector('.sidebar-toc');
    if(tocSidebar) {
        tocSidebar.style.display = 'none';
    }
    return;
  }

  // --- TOC Generation ---
  let tocHTML = '<ul>';
  let lastLevel = 0;
  const tocLinks = [];

  headings.forEach(function(heading, index) {
    const level = parseInt(heading.tagName.substring(1), 10);
    let id = heading.getAttribute('id');
    if (!id) {
      id = heading.textContent.trim().toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');
      let uniqueId = id;
      let counter = 1;
      while(document.getElementById(uniqueId)) {
          uniqueId = `${id}-${counter}`;
          counter++;
      }
      heading.setAttribute('id', uniqueId);
      id = uniqueId;
    }
    
    if (lastLevel > 0) {
        if (level > lastLevel) {
            tocHTML += '<ul>';
        } else if (level < lastLevel) {
            tocHTML += '</li></ul>'.repeat(lastLevel - level) + '</li>';
        } else {
            tocHTML += '</li>';
        }
    }

    tocHTML += `<li><a href="#${id}">${heading.textContent}</a>`;
    lastLevel = level;
  });

  if(lastLevel > 0) {
    tocHTML += '</li></ul>'.repeat(lastLevel);
  } else {
    tocHTML += '</ul>';
  }

  tocContainer.innerHTML = tocHTML;

  // --- Scroll-Spying Logic ---
  const tocLinkElements = tocContainer.querySelectorAll('a');

  const highlightTOCLink = () => {
    // Find the heading that is currently closest to the top of the viewport
    let currentHeadingId = '';
    
    // A small offset to activate the link a little before it hits the very top
    const offset = 150; 

    // Find the last heading that is above the viewport's middle
    const activeHeading = headings
        .filter(h => h.getBoundingClientRect().top < offset)
        .pop();
        
    if (activeHeading) {
        currentHeadingId = activeHeading.getAttribute('id');
    }

    // Remove 'active' from all links
    tocLinkElements.forEach(link => {
      link.classList.remove('active');
    });

    // Add 'active' to the current one
    if (currentHeadingId) {
      const activeLink = tocContainer.querySelector(`a[href="#${currentHeadingId}"]`);
      if (activeLink) {
        activeLink.classList.add('active');
      }
    } else if (tocLinkElements.length > 0) {
        // If no heading is active (i.e., we are at the top of the page), highlight the first one
        // tocLinkElements[0].classList.add('active');
        // Or do nothing, which might be better. Let's do nothing for now.
    }
  };

  // Run on load and on scroll
  highlightTOCLink();
  window.addEventListener('scroll', highlightTOCLink);
});
