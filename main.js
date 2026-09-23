/* Warin Energie GmbH – Skript. GSAP + ScrollTrigger + Lenis (CDN). Tweens nur auf transform/opacity (Blenden per clip-path). */
(() => {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const fmt = (n, d = 0) => n.toLocaleString('de-DE', { minimumFractionDigits: d, maximumFractionDigits: d });
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  const hasGsap = typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined';
  const motion = !reduce && hasGsap;
  if (motion) root.classList.add('js-motion'); else root.classList.add('no-motion');
  if (hasGsap) gsap.registerPlugin(ScrollTrigger);
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';

  // ---------- Lenis, gekoppelt an ScrollTrigger ----------
  let lenis;
  if (motion && typeof Lenis !== 'undefined') {
    lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  }

  // ---------- Kopfzeile: Leistungen-Menü, Verhalten beim Scrollen ----------
  const head = $('#head'), mega = $('#mega'), megaBtn = $('.has-mega > button');
  const setMega = open => { megaBtn.setAttribute('aria-expanded', open ? 'true' : 'false'); mega.classList.toggle('open', open); head.classList.toggle('mopen', open); };
  megaBtn.addEventListener('click', () => setMega(megaBtn.getAttribute('aria-expanded') !== 'true'));
  if (fine) { megaBtn.addEventListener('mouseenter', () => setMega(true)); head.addEventListener('mouseleave', () => setMega(false)); }
  document.addEventListener('click', e => { if (!head.contains(e.target)) setMega(false); });
  head.addEventListener('focusout', e => { if (!head.contains(e.relatedTarget)) setMega(false); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && mega.classList.contains('open')) { setMega(false); megaBtn.focus(); } });
  const sceneEl = $('.scene');
  let lastY = scrollY;
  const onScrollHead = () => {
    const y = scrollY;
    const overUntil = sceneEl && root.classList.contains('js-motion') ? sceneEl.offsetHeight - innerHeight - 8 : 40;
    const over = document.body.classList.contains('home') && y < overUntil;
    head.classList.toggle('over', over);
    head.classList.toggle('solid', !over && y > 4);
    if (!document.body.classList.contains('menu-open') && !mega.classList.contains('open')) {
      if (!over && y > 300 && y > lastY + 6 && y - lastY < 400) head.classList.add('hide');
      else if (y < lastY - 6 || over || y < 300) head.classList.remove('hide');
    }
    lastY = y;
    const sc = $('.sticky-cta'); if (sc) sc.classList.toggle('show', y > (sceneEl && root.classList.contains('js-motion') ? sceneEl.offsetHeight - innerHeight * .5 : 500));
  };
  addEventListener('scroll', onScrollHead, { passive: true });
  onScrollHead();
  // Menü (Handy)
  const menu = $('#menu'), menuBtn = $('.menu-btn');
  $$('li', menu).forEach((li, i) => li.style.setProperty('--i', i));
  let lastFocus;
  const closeMenu = () => {
    if (!menu.classList.contains('open')) return;
    document.body.classList.remove('menu-open'); menu.classList.remove('open');
    menuBtn.setAttribute('aria-expanded', 'false'); $('.lbl', menuBtn).textContent = 'Menü';
    lenis && lenis.start(); lastFocus && lastFocus.focus();
  };
  const openMenu = () => {
    lastFocus = document.activeElement;
    document.body.classList.add('menu-open'); menu.classList.add('open'); head.classList.remove('hide');
    menuBtn.setAttribute('aria-expanded', 'true'); $('.lbl', menuBtn).textContent = 'Schließen';
    lenis && lenis.stop(); setTimeout(() => $('a', menu).focus(), 350);
  };
  menuBtn.addEventListener('click', () => menu.classList.contains('open') ? closeMenu() : openMenu());
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && menu.classList.contains('open')) { closeMenu(); menuBtn.focus(); }
    if (e.key === 'Tab' && menu.classList.contains('open')) {
      const f = $$('a', menu); const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); menuBtn.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); menuBtn.focus(); }
      else if (!e.shiftKey && document.activeElement === menuBtn) { e.preventDefault(); first.focus(); }
    }
  });
  addEventListener('resize', () => { if (innerWidth > 1020) closeMenu(); });

  // ---------- Wort-für-Wort ----------
  $$('.split').forEach(el => {
    const words = el.textContent.trim().split(/\s+/);
    el.setAttribute('aria-label', words.join(' '));
    el.innerHTML = words.map(w => `<span class="split-line" aria-hidden="true"><span class="w">${w}</span></span>`).join(' ');
  });

  // ---------- Vorhang: Intro beim ersten Besuch, Blende beim Seitenwechsel ----------
  let seen = false; try { seen = sessionStorage.getItem('warin-intro'); } catch (e) {}
  const intro = $('.curtain.intro');
  let introDelay = 0;
  if (!seen && motion) {
    try { sessionStorage.setItem('warin-intro', '1'); } catch (e) {}
    document.body.classList.add('intro-on');
    const svg = $('svg', intro), bolt = $('polygon', intro);
    gsap.fromTo(svg, { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .5, ease: 'power3.out' });
    gsap.fromTo(bolt, { yPercent: -30, opacity: 0 }, { yPercent: 0, opacity: 1, duration: .35, delay: .25, ease: 'power4.out' });
    gsap.to(intro, { yPercent: -101, duration: .7, ease: 'power3.inOut', delay: .95, onComplete: () => document.body.classList.remove('intro-on') });
    introDelay = 1.25;
  }
  document.addEventListener('click', e => {
    const a = e.target.closest('a'); if (!a || !motion) return;
    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('tel:') || href.startsWith('mailto:') || a.target === '_blank' || e.metaKey || e.ctrlKey || e.shiftKey) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || (url.pathname === location.pathname && url.hash)) return;
    e.preventDefault(); document.body.classList.add('leaving'); setTimeout(() => location.href = a.href, 420);
  });
  addEventListener('pageshow', e => { if (e.persisted) document.body.classList.remove('leaving'); });
  // Anker-Links weich scrollen
  $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const id = a.getAttribute('href'); if (id.length < 2) { if (id === '#') { e.preventDefault(); lenis ? lenis.scrollTo(0) : scrollTo({ top: 0, behavior: 'smooth' }); } return; }
    const t = $(id); if (!t) return; e.preventDefault();
    lenis ? lenis.scrollTo(t, { offset: -80, duration: 1.4 }) : t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
  }));

  // ---------- Fortschrittsbalken ----------
  const prog = $('#progress');
  if (hasGsap) gsap.to(prog, { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: .3 } });

  // ---------- Magnetische Buttons mit Lichtreflex ----------
  if (fine && motion) $$('.mag').forEach(b => {
    const xTo = gsap.quickTo(b, 'x', { duration: .4, ease: 'power3' }), yTo = gsap.quickTo(b, 'y', { duration: .4, ease: 'power3' });
    b.addEventListener('pointermove', e => { const r = b.getBoundingClientRect(); const x = e.clientX - r.left, y = e.clientY - r.top; b.style.setProperty('--mx', x + 'px'); b.style.setProperty('--my', y + 'px'); xTo((x - r.width / 2) * .22); yTo((y - r.height / 2) * .3); });
    b.addEventListener('pointerleave', () => { xTo(0); yTo(0); });
  });
  // 3D-Neigung auf Karten
  if (fine && motion) $$('.more-list a, .lw, .pt, .tm').forEach(c => {
    const rx = gsap.quickTo(c, 'rotationX', { duration: .5, ease: 'power3' }), ry = gsap.quickTo(c, 'rotationY', { duration: .5, ease: 'power3' });
    gsap.set(c, { transformPerspective: 900 });
    c.addEventListener('pointermove', e => { const r = c.getBoundingClientRect(); ry(((e.clientX - r.left) / r.width - .5) * 6); rx(-((e.clientY - r.top) / r.height - .5) * 6); });
    c.addEventListener('pointerleave', () => { rx(0); ry(0); });
  });

  // ---------- Reveals ----------
  if (motion) {
    ScrollTrigger.batch('.reveal', { start: 'top 88%', once: true, onEnter: els => gsap.to(els, { opacity: 1, y: 0, duration: .9, ease: 'expo.out', stagger: .08 }) });
    $$('.split').forEach(el => {
      if (el.closest('.cap')) return;
      gsap.from($$('.w', el), { yPercent: 110, duration: .9, ease: 'expo.out', stagger: .045, delay: el.closest('.fh') ? introDelay * .8 : 0, scrollTrigger: { trigger: el, start: 'top 90%', once: true } });
    });
  } else if (hasGsap && reduce) {
    // Stufe 2: kurze Blende ohne Weg
    $$('.reveal').forEach(el => gsap.fromTo(el, { opacity: 0 }, { opacity: 1, duration: .15, scrollTrigger: { trigger: el, start: 'top 95%', once: true } }));
  }

  // Ersatzfassung der Szene (reduzierte Bewegung): Fotos nur dann laden, wenn sie gezeigt wird
  if (!motion) $$('img[data-st-src]').forEach(i => { i.srcset = i.dataset.stSrcset; i.src = i.dataset.stSrc; });
  else { const st = $('.scene-static'); if (st) st.remove(); }
  // Späte Bilder (ab Bild 2 erst nach dem load-Ereignis)
  const late = () => $$('img[data-late]').forEach(i => { if (i.dataset.srcset) i.srcset = i.dataset.srcset; if (i.dataset.src) i.src = i.dataset.src; $$('.half img').forEach(h => { if (h.dataset.srcset) h.srcset = h.dataset.srcset; if (h.dataset.src) h.src = h.dataset.src; }); });
  if (document.readyState === 'complete') late(); else addEventListener('load', late);

  // ================= STARTSEITE =================
  // Szene „Der Weg einer Kilowattstunde“: Einstieg → Markt → Übertragungsnetz → Verteilnetz → Ihr Betrieb → Rechnung.
  // Fester Zeitplan: Text raus → Weiterfahren → neue Rechnungszeile + neuer Text rein. Nie zwei Texte gleichzeitig.
  const scene = $('.scene');
  if (scene && motion) {
    const fr = $$('.frame', scene), caps = $$('.cap', scene), bill = $('.bill', scene), lines = $$('.bl', scene);
    const route = $('.route', scene), stops = $$('.rt-s', scene), dot = $('.rt-dot', scene), fill = $('.rt-line i', scene), dim = $('.dim', scene);
    const jag = [0, -5, 2, -8, -2, -11, 1, -6, -13, -3, -9, 0, -7];
    const wipe = p => { const base = 116 - p * 142; fr[1].style.clipPath = `polygon(${jag.map((j, i) => `${(i / (jag.length - 1) * 100).toFixed(2)}% ${(base + j).toFixed(2)}%`).join(',')},100% 100%,0 100%)`; };
    wipe(0);
    const T = { in: .3, out: .3, hold: .75, move: .9 };
    const arrive = []; // Zeitpunkt, an dem Station k erreicht ist
    const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: scene, start: 'top top', end: 'bottom bottom', scrub: .6, invalidateOnRefresh: true,
      onUpdate: () => { const tt = tl.time(); let cur = -1; stops.forEach((s, k) => { const on = tt >= arrive[k] - .01; s.classList.toggle('on', on); if (on) cur = k; }); stops.forEach((s, k) => s.classList.toggle('cur', k === cur)); bill.classList.toggle('live', tt >= arrive[stops.length - 1]); } } });
    const capIn = (c, at) => tl.fromTo(c, { autoAlpha: 0, y: 36 }, { autoAlpha: 1, y: 0, duration: T.in, ease: 'power2.out', immediateRender: false }, at);
    const capOut = (c, at) => tl.to(c, { autoAlpha: 0, y: -36, duration: T.out, ease: 'power2.in' }, at);
    const lineIn = (k, at) => { const ls = lines.filter(l => +l.dataset.at === k); if (!ls.length) return; tl.to(ls.map(l => $('.ph', l)), { autoAlpha: 0, duration: T.in * .6, stagger: .12 }, at); tl.fromTo(ls.map(l => $('a', l)), { autoAlpha: 0, x: 24 }, { autoAlpha: 1, x: 0, duration: T.in, stagger: .12, ease: 'power2.out', immediateRender: false }, at + .06); };
    const moveDot = (k, at) => { const p = (k / (stops.length - 1) * 100) + '%'; tl.to(dot, { left: p, duration: T.move, ease: 'power2.inOut' }, at); tl.to(fill, { scaleX: k / (stops.length - 1), duration: T.move, ease: 'power2.inOut' }, at); };
    // Einstieg: Text steht beim Laden
    gsap.fromTo(caps[0], { autoAlpha: 0, y: 30 }, { autoAlpha: 1, y: 0, duration: 1, ease: 'expo.out', delay: introDelay + .1 });
    gsap.fromTo($('img', fr[0]), { scale: 1.12 }, { scale: 1.05, duration: 2.2, ease: 'power2.out', delay: introDelay });
    let t = .6;
    tl.to(caps[0], { autoAlpha: 0, y: -36, duration: T.out, ease: 'power2.in', immediateRender: false }, t); t += T.out;
    // Zum Markt: Preiskurve steigt als Kante auf
    const w = { p: 0 };
    tl.set(fr[1], { visibility: 'visible' }, t);
    tl.to(w, { p: 1, duration: T.move, ease: 'power2.inOut', onUpdate: () => wipe(w.p) }, t);
    tl.fromTo($('img', fr[1]), { scale: 1.12 }, { scale: 1, duration: T.move + T.in + T.hold }, t);
    tl.fromTo([route, bill], { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, duration: .35, immediateRender: false }, t + T.move - .35);
    t += T.move; arrive[0] = t;
    lineIn(1, t); capIn(caps[1], t); t += T.in + T.hold; capOut(caps[1], t); t += T.out;
    // Weiterfahren entlang der Leitung: nächstes Foto schiebt sich von rechts herein
    for (let k = 1; k <= 3; k++) {
      const a = fr[k], b = fr[k + 1];
      tl.set(b, { visibility: 'visible' }, t);
      tl.fromTo(b, { xPercent: 100 }, { xPercent: 0, duration: T.move, ease: 'power2.inOut', immediateRender: false }, t);
      tl.to(a, { xPercent: -35, duration: T.move, ease: 'power2.inOut' }, t);
      tl.fromTo($('img', b), { scale: 1.1 }, { scale: 1, duration: T.move + T.in + T.hold, ease: 'none', immediateRender: false }, t);
      moveDot(k, t);
      t += T.move; arrive[k] = t;
      tl.set(a, { visibility: 'hidden' }, t);
      lineIn(k + 1, t); capIn(caps[k + 1], t); t += T.in + T.hold; capOut(caps[k + 1], t); t += T.out;
    }
    // Rechnung: Foto tritt zurück, die Rechnung wird zum Schlussbild
    moveDot(4, t);
    tl.to(dim, { opacity: 1, duration: T.move }, t);
    tl.to($('img', fr[4]), { scale: 1.08, duration: T.move }, t);
    tl.to(bill, { scale: innerWidth > 700 ? 1.12 : 1, y: innerWidth > 700 ? innerHeight * .04 : 0, duration: T.move, ease: 'power2.inOut' }, t);
    t += T.move; arrive[4] = t;
    lineIn(5, t); capIn(caps[5], t); t += T.in;
    tl.to({}, { duration: 1 }, t);
  }

  // ---------- Fünf Hebel: klebende Formel links markiert den Abschnitt rechts ----------
  const stack = $('.stack');
  if (stack) $$('.lv').forEach(lv => {
    const li = $('.st-' + lv.dataset.term, stack);
    if (hasGsap) ScrollTrigger.create({ trigger: lv, start: 'top 55%', end: 'bottom 55%', onToggle: s => li.classList.toggle('on', s.isActive) });
  });
  // ---------- Kostenhebel-Rechner ----------
  const calc = $('[data-calc]');
  if (calc) {
    const st = { kwh: 500000, ct: 1, y: 2 };
    const own = $('input[name=kwh]', calc);
    const draw = () => {
      const year = st.kwh * st.ct / 100;
      $('#c-year').textContent = fmt(Math.round(year)) + ' €';
      $('#c-total').textContent = fmt(Math.round(year * st.y)) + ' €';
      $('#c-eq').textContent = `${fmt(st.kwh)} kWh × ${fmt(st.ct, st.ct % 1 ? 1 : 0)} ct = ${fmt(Math.round(year))} € netto pro Jahr`;
    };
    $$('.chips', calc).forEach(g => $$('.chip', g).forEach(c => c.addEventListener('click', () => {
      $$('.chip', g).forEach(x => { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); }); c.classList.add('on'); c.setAttribute('aria-pressed', 'true');
      st[g.dataset.k] = +c.dataset.v; if (g.dataset.k === 'kwh') own.value = ''; draw();
    })));
    $$('.chip', calc).forEach(c => c.setAttribute('aria-pressed', c.classList.contains('on') ? 'true' : 'false'));
    own.addEventListener('input', () => {
      const v = parseInt(own.value.replace(/\D/g, ''), 10);
      if (v > 0) { st.kwh = Math.min(v, 1e9); $$('[data-k=kwh] .chip', calc).forEach(x => { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); }); draw(); }
    });
    draw();
    if (motion) {
      gsap.fromTo(calc, { scale: .92, y: 60 }, { scale: 1, y: 0, ease: 'none', scrollTrigger: { trigger: '.calc-sec', start: 'top 85%', end: 'top 25%', scrub: .7 } });
      gsap.fromTo('.calc-intro', { x: -40 }, { x: 0, ease: 'none', scrollTrigger: { trigger: '.calc-sec', start: 'top 85%', end: 'top 25%', scrub: .7 } });
    }
  }

  // ---------- Referenzen: Logo-Reihen laufen mit dem Scrollen gegeneinander ----------
  const refs = $('.refs');
  if (refs && motion) {
    const r1 = $('.lr.r1', refs), r2 = $('.lr.r2', refs);
    const dist = el => Math.max(0, el.scrollWidth - innerWidth) * .55;
    gsap.fromTo(r1, { x: 0 }, { x: () => -dist(r1), ease: 'none', scrollTrigger: { trigger: refs, start: 'top bottom', end: 'bottom top', scrub: .6, invalidateOnRefresh: true } });
    gsap.fromTo(r2, { x: () => -dist(r2) }, { x: 0, ease: 'none', scrollTrigger: { trigger: refs, start: 'top bottom', end: 'bottom top', scrub: .6, invalidateOnRefresh: true } });
  }
  // ---------- Über uns: Foto bewegt sich langsamer als die Seite ----------
  if (motion && $('.about-photo img')) gsap.fromTo('.about-photo img', { yPercent: -5 }, { yPercent: 5, ease: 'none', scrollTrigger: { trigger: '.about', start: 'top bottom', end: 'bottom top', scrub: .6 } });
  // ================= KERNSEITEN =================
  // Beschaffungsmodell-Umschalter
  const model = $('[data-model]');
  if (model) {
    const set = m => {
      model.dataset.m = m;
      $$('.model-ctl .chip', model).forEach(c => { const on = c.dataset.m === m; c.classList.toggle('on', on); c.setAttribute('aria-pressed', on); });
      $$('.model-txt p', model).forEach(p => p.hidden = p.dataset.m !== m);
      if (m === 'spot' && hasGsap) { const p = $('.m-spot', model); const L = p.getTotalLength(); gsap.fromTo(p, { strokeDasharray: L, strokeDashoffset: L }, { strokeDashoffset: 0, duration: reduce ? .01 : 1.1, ease: 'power2.out' }); }
    };
    $$('.model-ctl .chip', model).forEach(c => c.addEventListener('click', () => set(c.dataset.m)));
    set('tranchen');
    if (motion) gsap.fromTo($('.m-curve', model), { strokeDasharray: 3000, strokeDashoffset: 3000 }, { strokeDashoffset: 0, ease: 'none', scrollTrigger: { trigger: model, start: 'top 80%', end: 'top 35%', scrub: .6 } });
  }

  // Fristen-Rechner
  const frist = $('[data-frist]');
  if (frist) {
    const inp = $('#fr-end', frist); let mon = 3;
    const d0 = new Date(); d0.setHours(0, 0, 0, 0);
    const def = new Date(d0.getFullYear() + 1, 11, 31); // Standard: Jahresende nächstes Jahr
    const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
    inp.value = iso(def);
    const addM = (d, m) => { const x = new Date(d); const day = x.getDate(); x.setDate(1); x.setMonth(x.getMonth() + m); const last = new Date(x.getFullYear(), x.getMonth() + 1, 0).getDate(); x.setDate(Math.min(day, last)); return x; };
    const de = d => d.toLocaleDateString('de-DE', { day: 'numeric', month: 'long', year: 'numeric' });
    const rel = d => { const n = Math.round((d - d0) / 864e5); return n < 0 ? `vor ${fmt(-n)} Tagen verstrichen` : n === 0 ? 'heute' : `in ${fmt(n)} Tagen`; };
    const draw = () => {
      if (!inp.value) return;
      const end = new Date(inp.value + 'T00:00:00');
      const c = addM(end, -mon), b = new Date(c - 28 * 864e5), a = addM(end, -12);
      [['a', a], ['b', b], ['c', c]].forEach(([k, d]) => { $('#fr-' + k).textContent = de(d); $('#fr-' + k + 'n').textContent = rel(d); $('#fr-' + k).closest('li').classList.toggle('late', d < d0); });
    };
    inp.addEventListener('input', draw);
    $$('.chip', frist).forEach(c => c.addEventListener('click', () => { $$('.chip', frist).forEach(x => { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); }); c.classList.add('on'); c.setAttribute('aria-pressed', 'true'); mon = +c.dataset.v; draw(); }));
    draw();
  }

  // Musterrechnung
  const inv = $('[data-invoice]');
  if (inv) {
    $$('.iv-row button', inv).forEach(b => b.addEventListener('click', () => {
      const open = b.getAttribute('aria-expanded') === 'true';
      const info = $('#' + b.getAttribute('aria-controls'));
      b.setAttribute('aria-expanded', !open); info.hidden = open;
      if (!open && hasGsap) gsap.fromTo(info, { opacity: 0, y: -6 }, { opacity: 1, y: 0, duration: reduce ? .15 : .35, ease: 'power3.out' });
      $('.iv-hint', inv).textContent = `${$$('[aria-expanded=true]', inv).length} von ${$$('.iv-row', inv).length} Positionen geöffnet`;
    }));
    if (motion) gsap.from($$('.iv-row', inv), { opacity: 0, x: -20, stagger: .05, duration: .6, ease: 'expo.out', scrollTrigger: { trigger: inv, start: 'top 80%', once: true } });
  }

  // Antrags-Matrix
  const mx = $('[data-matrix]');
  if (mx) {
    const draw = () => {
      const art = $('[data-g=art] .chip.on', mx).dataset.v;
      const on = new Set($$('[data-g=traeger] .chip.on, [data-g=extra] .chip.on', mx).map(c => c.dataset.v));
      let n = 0;
      $$('.mx-list li', mx).forEach(li => {
        const ok = li.dataset.if.split(' ').every(k => on.has(k)) && li.dataset.art.split(' ').includes(art);
        if (ok && li.hidden) { li.classList.remove('in'); void li.offsetWidth; li.classList.add('in'); }
        li.hidden = !ok; if (ok) n++;
      });
      $('#mx-n', mx).textContent = n;
      $('.mx-count', mx).lastChild.textContent = n === 1 ? ' mögliche Entlastung' : ' mögliche Entlastungen';
      $('.mx-empty', mx).hidden = n > 0;
    };
    $$('.chips', mx).forEach(g => $$('.chip', g).forEach(c => c.addEventListener('click', () => {
      if (g.classList.contains('multi')) { c.classList.toggle('on'); }
      else { $$('.chip', g).forEach(x => x.classList.remove('on')); c.classList.add('on'); }
      $$('.chip', g).forEach(x => x.setAttribute('aria-pressed', x.classList.contains('on')));
      draw();
    })));
    draw();
  }

  // EnEfG-Pflichten-Check
  const pf = $('[data-pflicht]');
  if (pf) {
    let mwh = 3000, kmu = true;
    const own = $('input[name=mwh]', pf);
    const draw = () => {
      const act = new Set();
      if (mwh > 7500) act.add('ems');
      if (mwh > 2500) { act.add('plan'); act.add('abw'); }
      if (!kmu && mwh <= 7500) act.add('audit');
      if (!act.size) act.add('frei');
      $$('.pf-list li', pf).forEach(li => li.classList.toggle('on', act.has(li.dataset.p)));
      const f = Math.min(1, mwh <= 2500 ? mwh / 2500 * .25 : mwh <= 7500 ? .25 + (mwh - 2500) / 5000 * .5 : .75 + Math.min(1, (mwh - 7500) / 7500) * .25);
      $('.pf-fill', pf).style.setProperty('--f', Math.max(.02, f));
    };
    $$('.pf-in > fieldset:first-child .chip', pf).forEach(c => c.addEventListener('click', () => { $$('.pf-in > fieldset:first-child .chip', pf).forEach(x => { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); }); c.classList.add('on'); c.setAttribute('aria-pressed', 'true'); mwh = +c.dataset.v; own.value = ''; draw(); }));
    $$('[data-g=kmu] .chip', pf).forEach(c => c.addEventListener('click', () => { $$('[data-g=kmu] .chip', pf).forEach(x => { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); }); c.classList.add('on'); c.setAttribute('aria-pressed', 'true'); kmu = c.dataset.v === 'kmu'; draw(); }));
    own.addEventListener('input', () => { const v = parseInt(own.value.replace(/\D/g, ''), 10); if (v >= 0 && own.value) { mwh = v; $$('.pf-in > fieldset:first-child .chip', pf).forEach(x => { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); }); draw(); } });
    draw();
  }

  // Waage Eigeninvestition / Contracting
  const wg = $('[data-waage]');
  if (wg) {
    const beam = $('.wg-beam', wg), pl = $('.wg-pan.l', wg), pr = $('.wg-pan.r', wg), out = $('.wg-out', wg);
    const draw = () => {
      const c = $$('input:checked[data-side=c]', wg).length, e = $$('input:checked[data-side=e]', wg).length;
      const a = Math.max(-14, Math.min(14, (c - e) * 4.5));
      beam.style.transform = `rotate(${a}deg)`;
      pl.style.transform = pr.style.transform = `rotate(${-a}deg)`;
      pl.style.transformOrigin = '80px 110px'; pr.style.transformOrigin = '520px 110px'; pl.style.transformBox = pr.style.transformBox = 'view-box';
      out.textContent = !c && !e ? 'Wählen Sie aus, was Ihnen wichtig ist.' : c > e ? `Für Sie spricht mehr für Contracting (${c} zu ${e}). Wir rechnen es gern für Ihre Anlage durch.` : e > c ? `Für Sie spricht mehr für die eigene Anlage (${e} zu ${c}). Wir helfen auch bei Planung und Förderung.` : 'Ausgeglichen. Dann entscheidet die Wirtschaftlichkeitsrechnung – die machen wir mit Ihnen.';
    };
    $$('input', wg).forEach(i => i.addEventListener('change', draw));
    draw();
  }

  // Bündelungs-Baukasten
  const bd = $('[data-bundle]');
  if (bd) {
    const names = { mfh: 'Mehrfamilienhaus', anl: 'Wohnanlage', weg: 'Eigentümer­gemeinschaft', gew: 'Gewerbe­einheit' };
    const ico = { mfh: '<path d="M6 30V12l11-7 11 7v18z"/><rect x="11" y="15" width="4" height="4"/><rect x="19" y="15" width="4" height="4"/><rect x="11" y="22" width="4" height="4"/><rect x="19" y="22" width="4" height="4"/>', anl: '<path d="M3 30V14l8-5 8 5v16zM19 30V10l6-4 6 4v20z"/>', weg: '<path d="M5 30V14L17 5l12 9v16z"/><path d="M13 30v-8h8v8"/>', gew: '<path d="M4 30V16l8 5v-5l8 5v-5l10 6v8z"/>' };
    const list = $('.bd-houses', bd); let count = 0;
    const draw = () => {
      $('#bd-n', bd).textContent = count; $('#bd-f', bd).textContent = count; $('#bd-r', bd).textContent = count * 12;
      $('#bd-one-t', bd).textContent = count ? `${count} ${count === 1 ? 'Liegenschaft' : 'Liegenschaften'}, ein Ansprechpartner, eine Frist` : 'Fügen Sie Liegenschaften hinzu';
      const one = $('.bd-one', bd); one.classList.remove('bump'); void one.offsetWidth; if (count && !reduce) one.classList.add('bump');
    };
    $$('[data-t]', bd).forEach(b => b.addEventListener('click', () => {
      if (count >= 12) return; count++;
      const li = document.createElement('li'); li.innerHTML = `<svg viewBox="0 0 34 34" aria-hidden="true">${ico[b.dataset.t]}</svg>${names[b.dataset.t]}<span class="doc">Vertrag ${count}</span>`;
      list.appendChild(li); draw();
    }));
    $('[data-reset]', bd).addEventListener('click', () => { list.innerHTML = ''; count = 0; draw(); });
    ['mfh', 'weg', 'gew'].forEach(t => $(`[data-t=${t}]`, bd).click());
  }

  // Perspektiv-Wechsel
  const ps = $('[data-persp]');
  if (ps) {
    const tabs = $$('.ps-tab', ps);
    const set = (b, focus) => {
      tabs.forEach(t => { const on = t === b; t.classList.toggle('on', on); t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1; $('#' + t.getAttribute('aria-controls')).hidden = !on; });
      ps.classList.toggle('alt', b.dataset.v === 'm'); if (focus) b.focus();
    };
    tabs.forEach((t, i) => { t.addEventListener('click', () => set(t)); t.addEventListener('keydown', e => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); set(tabs[(i + 1) % tabs.length], true); } }); });
    set(tabs[0]);
  }

  // Formel-Kopf der Unterseiten: Term wird nach dem Laden markiert
  const fhOn = $$('.fh-formula .term.on');
  if (fhOn.length && motion) { fhOn.forEach(t => t.classList.remove('on')); setTimeout(() => fhOn.forEach(t => t.classList.add('on')), introDelay * 1000 + 450); }

  // ---------- Formular: Vorwahl per ?thema=, Prüfung, Versand ----------
  $$('.form').forEach(form => {
    const thema = new URLSearchParams(location.search).get('thema');
    const sel = $('select[name=thema]', form);
    if (thema && sel && [...sel.options].some(o => o.value === thema)) sel.value = thema;
    const fields = $$('[required]', form);
    const check = el => { const f = el.closest('.field'); const ok = el.type === 'checkbox' ? el.checked : el.type === 'email' ? /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value.trim()) : el.value.trim().length > 1; f.classList.toggle('invalid', !ok); el.setAttribute('aria-invalid', !ok); return ok; };
    fields.forEach(el => el.addEventListener(el.type === 'checkbox' ? 'change' : 'input', () => el.closest('.field').classList.contains('invalid') && check(el)));
    const file = $('input[type=file]', form);
    if (file) file.addEventListener('change', () => { const f = file.files[0]; const bad = f && f.size > 8 * 1024 * 1024; file.closest('.field').classList.toggle('invalid', bad); if (bad) { file.value = ''; alert('Die Datei ist größer als 8 MB. Bitte schicken Sie sie per E-Mail.'); } });
    form.addEventListener('submit', e => {
      const bad = fields.filter(el => !check(el));
      if (bad.length) { e.preventDefault(); bad[0].focus(); return; }
      const local = location.protocol === 'file:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1' || location.hostname.endsWith('github.io');
      if (local) { e.preventDefault(); document.body.classList.add('leaving'); setTimeout(() => location.href = 'danke.html', motion ? 420 : 0); }
    });
  });

  // ---------- Karte erst per Klick ----------
  const mapBtn = $('#map-btn');
  if (mapBtn) mapBtn.addEventListener('click', () => {
    const m = $('#map'); m.classList.add('loaded');
    m.innerHTML = '<iframe title="Karte: Auf dem Hügel 21, 52249 Eschweiler" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=6.2586%2C50.8297%2C6.2786%2C50.8377&amp;layer=mapnik&amp;marker=50.83367%2C6.26860"></iframe>';
  });

  // ---------- Neu messen nach Schrift- und Bild-Load ----------
  if (hasGsap) {
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => ScrollTrigger.refresh());
    addEventListener('load', () => setTimeout(() => ScrollTrigger.refresh(), 200));
  }
  if (location.hash && lenis) { const t = $(location.hash); if (t) setTimeout(() => lenis.scrollTo(t, { offset: -80, immediate: true }), 120); }
})();
