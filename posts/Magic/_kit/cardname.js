/* Card names in running text ({{< cn id >}}): hovering, focusing or tapping a name shows the card beside it.
   The cards come from <template class="mk-cn-tpl"> elements the shortcode adds at the end of the page. */
(function () {
  'use strict';
  var pop = null, current = null, cache = {};

  function cardHtml(id) {
    if (!(id in cache)) {
      var t = document.querySelector('template.mk-cn-tpl[data-id="' + id + '"]');
      cache[id] = t ? t.innerHTML : '';
    }
    return cache[id];
  }
  function nameAt(target) {
    return target && target.closest ? target.closest('.mk-cn') : null;
  }
  function show(el) {
    var html = cardHtml(el.getAttribute('data-mk-card'));
    if (!html) return;
    if (!pop) {
      pop = document.createElement('div');
      pop.className = 'mk-pop';
      pop.setAttribute('aria-hidden', 'true');
      document.body.appendChild(pop);
    }
    if (current !== el) pop.innerHTML = html;
    current = el;
    var r = el.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight, m = 8;
    var x = Math.min(Math.max(m, r.left + r.width / 2 - w / 2), window.innerWidth - w - m);
    var y = r.top - h - m;
    if (y < m) y = Math.min(r.bottom + m, window.innerHeight - h - m);
    pop.style.left = Math.max(m, x) + 'px';
    pop.style.top = Math.max(m, y) + 'px';
    pop.classList.add('mk-on');
  }
  function hide() {
    if (pop) pop.classList.remove('mk-on');
    current = null;
  }

  document.addEventListener('mouseover', function (e) { var el = nameAt(e.target); if (el) show(el); });
  document.addEventListener('mouseout', function (e) { if (nameAt(e.target)) hide(); });
  document.addEventListener('focusin', function (e) { var el = nameAt(e.target); if (el) show(el); });
  document.addEventListener('focusout', function (e) { if (nameAt(e.target)) hide(); });
  document.addEventListener('click', function (e) { var el = nameAt(e.target); if (el) show(el); else hide(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hide(); });
  window.addEventListener('scroll', hide, { passive: true });
})();
