
document.addEventListener("DOMContentLoaded", function() {
  const tocContainer = document.getElementById('toc');
  const content = document.querySelector('.post-content');

  if (!tocContainer || !content) {
    return;
  }

  const headings = content.querySelectorAll('h2, h3');
  if (headings.length === 0) {
    return;
  }

  let tocHTML = '<ul>';
  let currentLevel = 2;

  headings.forEach(function(heading, index) {
    const level = parseInt(heading.tagName.substring(1), 10);

    // Ensure headings have an ID
    let id = heading.getAttribute('id');
    if (!id) {
      id = 'toc-heading-' + index;
      heading.setAttribute('id', id);
    }

    if (level > currentLevel) {
      tocHTML += '<ul>';
    } else if (level < currentLevel) {
      tocHTML += '</ul>';
    }
    currentLevel = level;

    tocHTML += '<li><a href="#' + id + '">' + heading.textContent + '</a></li>';
  });

  // Close any open lists
  while (currentLevel > 2) {
    tocHTML += '</ul>';
    currentLevel--;
  }
  tocHTML += '</ul>';

  tocContainer.innerHTML = tocHTML;
});
