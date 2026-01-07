(function(){
  const qs = sel => document.querySelector(sel);
  const qsa = sel => Array.from(document.querySelectorAll(sel));
  const toggleClass = (cls) => {
    document.body.classList.toggle(cls);
    localStorage.setItem('labficol-'+cls, document.body.classList.contains(cls) ? '1' : '0');
  };
  ['hc','big-text','low-motion'].forEach(cls => {
    if(localStorage.getItem('labficol-'+cls) === '1') document.body.classList.add(cls);
  });
  const hc = qs('#toggleHC');
  const bt = qs('#toggleBT');
  const lm = qs('#toggleLM');
  if(hc) hc.addEventListener('click', () => toggleClass('hc'));
  if(bt) bt.addEventListener('click', () => toggleClass('big-text'));
  if(lm) lm.addEventListener('click', () => toggleClass('low-motion'));

  // Tabs behavior
  const initTabs = () => {
    qsa('.tabs').forEach(tabsEl => {
      const btns = Array.from(tabsEl.querySelectorAll('.tab-btn'));
      const panels = Array.from(tabsEl.parentElement.querySelectorAll('.module-section[role="tabpanel"]'));
      const show = (id) => {
        panels.forEach(p => p.hidden = (p.id !== id));
        btns.forEach(b => b.setAttribute('aria-selected', (b.getAttribute('aria-controls') === id) ? 'true' : 'false'));
        btns.forEach(b => b.setAttribute('tabindex', (b.getAttribute('aria-controls') === id) ? '0' : '-1'));
      };
      // Click handlers
      btns.forEach(b => {
        b.addEventListener('click', () => {
          const target = b.getAttribute('aria-controls');
          show(target);
          // update hash for deep linking
          try { history.replaceState(null, '', '#'+target); } catch {}
          b.focus();
        });
      });
      // Keyboard navigation (Left/Right/Home/End)
      tabsEl.addEventListener('keydown', (e) => {
        const current = btns.findIndex(b => b.getAttribute('aria-selected') === 'true');
        let next = current;
        if(e.key === 'ArrowRight') next = (current + 1) % btns.length;
        else if(e.key === 'ArrowLeft') next = (current - 1 + btns.length) % btns.length;
        else if(e.key === 'Home') next = 0;
        else if(e.key === 'End') next = btns.length - 1;
        else return;
        e.preventDefault();
        const target = btns[next].getAttribute('aria-controls');
        show(target);
        btns[next].focus();
        try { history.replaceState(null, '', '#'+target); } catch {}
      });
      // Initial selection: honor hash or first
      const hash = (location.hash || '').replace('#','');
      const initial = btns.find(b => b.getAttribute('aria-controls') === hash) ? hash : (btns.find(b => b.getAttribute('aria-selected') === 'true')?.getAttribute('aria-controls') || btns[0]?.getAttribute('aria-controls'));
      if(initial) show(initial);
    });
  };
  window.addEventListener('hashchange', () => {
    const hash = (location.hash || '').replace('#','');
    const btn = document.querySelector(`.tabs .tab-btn[aria-controls="${hash}"]`);
    if(btn) btn.click();
  });
  try { initTabs(); } catch {}
})();
