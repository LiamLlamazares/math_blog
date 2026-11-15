/* Click-through duel for the mana kit.  Each .mk-duel holds one game as JSON plus
   card templates (put there by the duel shortcode), so it has no globals and any
   number of duels can share a page.  The three zones always keep the height of the
   fullest step of that game, so nothing below the figure jumps when you step. */
(function () {
  'use strict';

  function h(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function has(list, id) { return !!list && list.indexOf(id) >= 0; }

  function init(root) {
    if (root.getAttribute('data-mk-ready')) return;
    root.setAttribute('data-mk-ready', '1');

    var game = JSON.parse(root.querySelector('.mk-data').textContent).games[0];
    var frames = game.frames, n = frames.length;
    var tpl = {};
    Array.prototype.forEach.call(root.querySelectorAll('template[data-id]'), function (t) {
      tpl[t.getAttribute('data-id')] = t.innerHTML;
    });
    var play = root.querySelector('.mk-play');
    var fin = root.querySelector('.mk-final');
    var step = 0, zmax = [0, 0, 0], smax = 0;

    var stage = h('div', 'mk-stage');
    var say = h('p', 'mk-say');
    say.setAttribute('aria-live', 'polite');
    var ctrl = h('div', 'mk-ctrl');
    var prev = h('button', 'mk-btn', '&larr; Back');
    var next = h('button', 'mk-btn', 'Next &rarr;');
    prev.type = next.type = 'button';
    prev.setAttribute('aria-label', 'Previous step');
    next.setAttribute('aria-label', 'Next step');
    var dots = h('span', 'mk-dots');
    dots.setAttribute('aria-hidden', 'true');
    var count = h('span', 'mk-count');
    ctrl.appendChild(prev); ctrl.appendChild(next); ctrl.appendChild(dots); ctrl.appendChild(count);
    play.appendChild(stage); play.appendChild(say); play.appendChild(ctrl);

    function zone(label, ids, f, kind) {
      var z = h('div', 'mk-zone');
      z.appendChild(h('span', 'mk-zl', label));
      var row = h('div', 'mk-row mk-row-sm');
      ids.forEach(function (id, i) {
        var cls = 'mk-mk', cap = '&nbsp;';
        if (kind === 'lands' && has(f.used, id)) { cls += ' mk-used'; cap = 'used for mana'; }
        if (has(f['new'], id) && i === ids.lastIndexOf(id)) { cls += ' mk-new'; cap = 'new this turn'; }
        if (kind === 'hand' && has(f.stuck, id)) { cls += ' mk-stuck'; cap = 'stuck in hand'; }
        row.appendChild(h('figure', cls, tpl[id] + '<figcaption>' + cap + '</figcaption>'));
      });
      z.appendChild(row);
      return z;
    }
    function fill(into, f) {
      into.innerHTML = '';
      into.appendChild(zone('Lands in play', f.lands, f, 'lands'));
      into.appendChild(zone('Spells cast', f.cast, f, 'cast'));
      into.appendChild(zone('Hand', f.hand, f, 'hand'));
    }
    function sayHtml(f) { return '<b>' + f.title + '.</b> ' + f.say; }

    /* ---- reserve the height of the fullest step, per zone and for the caption ---- */
    function reserve() {
      var w = stage.getBoundingClientRect().width;
      if (!w) return;
      var probe = h('div', 'mk-probe');
      probe.style.width = root.getBoundingClientRect().width + 'px';
      var ps = h('div', 'mk-stage');
      var pp = h('p', 'mk-say');
      probe.appendChild(ps); probe.appendChild(pp);
      root.appendChild(probe);
      zmax = [0, 0, 0]; smax = 0;
      frames.forEach(function (f) {
        fill(ps, f);
        pp.innerHTML = sayHtml(f);
        Array.prototype.forEach.call(ps.children, function (z, i) { zmax[i] = Math.max(zmax[i], z.offsetHeight); });
        smax = Math.max(smax, pp.offsetHeight);
      });
      root.removeChild(probe);
      apply();
    }
    function apply() {
      Array.prototype.forEach.call(stage.children, function (z, i) { z.style.minHeight = zmax[i] + 'px'; });
      say.style.minHeight = smax + 'px';
    }

    function renderStep() {
      var f = frames[step];
      fill(stage, f);
      say.innerHTML = sayHtml(f);
      apply();
      dots.innerHTML = '';
      for (var i = 0; i < n; i++) dots.appendChild(h('i', i === step ? 'mk-on' : ''));
      count.textContent = 'Step ' + (step + 1) + ' of ' + n;
      prev.disabled = step === 0;
      next.disabled = step === n - 1;
    }

    function go(delta) {
      var s = step + delta;
      if (s < 0 || s >= n) return;
      step = s;
      renderStep();
      // a button that just became disabled would drop keyboard focus
      if (document.activeElement === prev && prev.disabled) next.focus();
      if (document.activeElement === next && next.disabled) prev.focus();
    }
    prev.addEventListener('click', function () { go(-1); });
    next.addEventListener('click', function () { go(1); });
    root.addEventListener('keydown', function (e) {
      if (e.altKey || e.ctrlKey || e.metaKey) return;
      if (e.key === 'ArrowRight') { go(1); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { go(-1); e.preventDefault(); }
    });

    /* print shows the last step only */
    var fs = h('div', 'mk-stage');
    fill(fs, frames[n - 1]);
    fin.appendChild(fs);
    fin.appendChild(h('p', 'mk-say', sayHtml(frames[n - 1])));

    root.classList.add('mk-live');
    reserve();
    renderStep();
    var lastW = root.getBoundingClientRect().width;
    window.addEventListener('resize', function () {
      var w = root.getBoundingClientRect().width;
      if (w !== lastW) { lastW = w; reserve(); }
    });
    window.addEventListener('load', reserve);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(reserve);
    root.mkReserve = reserve;
  }

  Array.prototype.forEach.call(document.querySelectorAll('[data-mk-duel]'), init);
})();
