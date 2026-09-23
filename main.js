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

  // ---------- Kopf: Hebel heben ihre Leistungen hervor, Zeile 2 klappt beim Runterscrollen weg ----------
  const head = $('#head'), row2 = $('#row2');
  $$('.lever').forEach(b => {
    const on = v => { row2.classList.toggle('focus', v); $$('.grp', row2).forEach(g => g.classList.toggle('hl', v && g.dataset.lever === b.dataset.lever)); b.classList.toggle('hl', v); if (v) head.classList.remove('compact'); };
    b.addEventListener('mouseenter', () => on(true)); b.addEventListener('focus', () => on(true));
    b.addEventListener('mouseleave', () => on(false)); b.addEventListener('blur', () => on(false));
    b.addEventListener('click', () => { const first = $(`.grp[data-lever="${b.dataset.lever}"] a`, row2); first && first.focus(); });
  });
  let lastY = scrollY;
  const onScrollHead = () => {
    const y = scrollY;
    if (!document.body.classList.contains('menu-open')) {
      if (y > 160 && y > lastY + 4) head.classList.add('compact');
      else if (y < lastY - 4 || y < 160) head.classList.remove('compact');
    }
    lastY = y;
    const sc = $('.sticky-cta'), sEnd = $('.scene') && $('.scene').offsetHeight; if (sc) sc.classList.toggle('show', y > (sEnd && root.classList.contains('js-motion') ? sEnd - innerHeight * .5 : 500));
  };
  addEventListener('scroll', onScrollHead, { passive: true });

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
    document.body.classList.add('menu-open'); menu.classList.add('open'); head.classList.remove('compact');
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

  // Späte Bilder (ab Bild 2 erst nach dem load-Ereignis)
  const late = () => $$('img[data-late]').forEach(i => { if (i.dataset.src) i.src = i.dataset.src; });
  if (document.readyState === 'complete') late(); else addEventListener('load', late);

  // ================= STARTSEITE =================
  const scene = $('.scene');
  if (scene && motion) {
    const H = () => innerHeight, W = () => innerWidth;
    const caps = $$('.cap', scene);
    // Perforationskante für den Abriss (Zähne entlang der Mitte)
    const teeth = (up) => { const n = 48, pts = []; for (let i = 0; i <= n; i++) { const x = i / n * 100; const y = 50 + (i % 2 ? 1.1 : -1.1); pts.push(`${x.toFixed(2)}% ${y}%`); } return up ? `polygon(0 0,100% 0,${pts.reverse().join(',')})` : `polygon(${pts.join(',')},100% 100%,0 100%)`; };
    $('.tear.top', scene).style.clipPath = teeth(true);
    $('.tear.bot', scene).style.clipPath = teeth(false);
    // Kurven-Wipe: gezackte Oberkante steigt von unten auf
    const f5 = $('.f5', scene), jag = [0, -6, 3, -9, -2, -12, 1, -7, -14, -4, -10, 0, -8];
    const wipe = p => { const base = 116 - p * 142; const pts = jag.map((j, i) => `${(i / (jag.length - 1) * 100).toFixed(2)}% ${(base + j).toFixed(2)}%`); f5.style.clipPath = `polygon(${pts.join(',')},100% 100%,0 100%)`; };
    wipe(0);
    const bpFill = $('.bp-fill', scene);

    const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: scene, start: 'top top', end: 'bottom bottom', scrub: .8, invalidateOnRefresh: true, onUpdate: s => gsap.set(bpFill, { scaleY: s.progress }) } });
    const capIn = (c, at) => { tl.set(c, { visibility: 'visible', opacity: 1 }, at); tl.fromTo($$('.w', c), { yPercent: 110 }, { yPercent: 0, stagger: .015, duration: .35, ease: 'power3.out' }, at); const a = $('.actions', c); if (a) tl.fromTo(a, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: .3 }, at + .2); };
    const capOut = (c, at) => { tl.to($$('.w', c), { yPercent: -110, stagger: .008, duration: .25, ease: 'power2.in' }, at); tl.set(c, { visibility: 'hidden' }, at + .36); };
    const bigBolt = $$('.big-bolt', scene);

    // Bild 1: Blitz steht, Text läuft ein (beim Laden automatisch, danach gescrubbt raus)
    gsap.fromTo(bigBolt, { scale: .82, opacity: 0, transformOrigin: '50% 50%' }, { scale: 1, opacity: 1, duration: 1.1, ease: 'expo.out', delay: introDelay });
    const c1 = caps[0];
    gsap.set(c1, { visibility: 'visible', opacity: 1 });
    gsap.from($$('.w', c1), { yPercent: 110, duration: 1, ease: 'expo.out', stagger: .035, delay: introDelay + .15 });
    tl.to({}, { duration: .5 });
    capOut(c1, .5);
    // Blende 1: Blitzschnitt – der Schirm reißt entlang der Zickzack-Linie auf
    tl.to('.half.a', { xPercent: -62, yPercent: -12, rotation: -5, duration: 1, ease: 'power2.in' }, .85);
    tl.to('.half.b', { xPercent: 62, yPercent: 12, rotation: 5, duration: 1, ease: 'power2.in' }, .85);
    tl.fromTo('.f2 .inv', { scale: .9, opacity: .4 }, { scale: 1, opacity: 1, duration: 1 }, .85);
    tl.fromTo('.tear.top .inv-row', { opacity: 0, x: -14 }, { opacity: 1, x: 0, stagger: .05, duration: .3 }, 1.4);
    capIn(caps[1], 1.75);
    tl.to({}, { duration: .5 }, 2.2);
    capOut(caps[1], 2.7);
    // Blende 2: Perforations-Abriss
    tl.to('.perf', { scaleX: 1, duration: .35, ease: 'power2.out' }, 3.0);
    tl.set('.perf', { opacity: 0 }, 3.4);
    tl.to('.tear.top', { yPercent: -100, rotation: -4, transformOrigin: '0% 50%', duration: .9, ease: 'power2.in' }, 3.4);
    tl.to('.tear.bot', { yPercent: 100, rotation: 3, transformOrigin: '100% 50%', duration: .9, ease: 'power2.in' }, 3.4);
    tl.fromTo('.c-line', { strokeDasharray: 3000, strokeDashoffset: 3000 }, { strokeDashoffset: 0, duration: 1.3, ease: 'power1.inOut' }, 3.6);
    tl.to('.buy', { scale: 1, stagger: .18, duration: .25, ease: 'back.out(3)' }, 4.2);
    capIn(caps[2], 4.3);
    tl.to({}, { duration: .5 }, 4.8);
    capOut(caps[2], 5.1);
    // Blende 3: Zählerwalze – Bild 3 rollt nach oben weg, Bild 4 rollt von unten nach
    tl.fromTo('.f3', { rotationX: 0 }, { rotationX: 90, duration: 1, ease: 'power2.inOut', transformOrigin: () => `50% 50% ${-H() / 2}px` }, 5.45);
    tl.fromTo('.f4', { rotationX: -90 }, { rotationX: 0, duration: 1, ease: 'power2.inOut', transformOrigin: () => `50% 50% ${-H() / 2}px` }, 5.45);
    // Kachel-Montage der Referenzlogos
    const tiles = $$('.tile', scene).sort(() => Math.random() - .5);
    tl.fromTo(tiles, { opacity: 0, scale: .8 }, { opacity: 1, scale: 1, stagger: .05, duration: .3, ease: 'back.out(2)' }, 6.3);
    capIn(caps[3], 6.5);
    tl.to({}, { duration: .5 }, 7.1);
    capOut(caps[3], 7.6);
    // Blende 4: Kurven-Wipe – gezackte Preiskurve steigt auf
    const wp = { p: 0 };
    tl.to(wp, { p: 1, duration: 1.1, ease: 'power2.inOut', onUpdate: () => wipe(wp.p) }, 7.95);
    tl.fromTo('.portrait', { scale: .7, rotation: -8 }, { scale: 1, rotation: 0, duration: 1.1, ease: 'power3.out' }, 8.4);
    capIn(caps[4], 8.8);
    tl.to({}, { duration: .9 }, 9.3);
  }

  // ---------- Kostenformel (Signature) ----------
  const formel = $('.formel');
  if (formel && motion) {
    const chs = $$('.ch', formel), terms = k => $$(`.formel-big .t-${k}`, formel);
    const all = $$('.formel-big .term', formel);
    const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: formel, start: 'top top', end: () => '+=' + innerHeight * 4.2, pin: '.formel-pin', scrub: .7, anticipatePin: 1, invalidateOnRefresh: true } });
    tl.fromTo('.formel-big .formula > *', { opacity: 0, y: 30 }, { opacity: 1, y: 0, stagger: .04, duration: .5, ease: 'power3.out' }, 0);
    let t = .9;
    chs.forEach((ch, i) => {
      const k = ch.dataset.term;
      tl.set(ch, { visibility: 'visible' }, t);
      tl.to(all, { opacity: .28, duration: .2 }, t);
      tl.to(terms(k), { opacity: 1, color: '#d00000', duration: .3, ease: 'power2.out' }, t);
      tl.fromTo(ch, { opacity: 0, y: 36 }, { opacity: 1, y: 0, duration: .35, ease: 'power3.out' }, t + .1);
      const paths = $$('.ch-draw path, .ch-draw rect, .ch-draw circle', ch);
      paths.forEach(p => { const L = (p.getTotalLength ? p.getTotalLength() : 400) + 2; gsap.set(p, { strokeDasharray: L, strokeDashoffset: L }); });
      tl.to(paths, { strokeDashoffset: 0, duration: .5, stagger: .06 }, t + .2);
      tl.to({}, { duration: .5 }, t + .45);
      if (i < chs.length - 1) {
        tl.to(ch, { opacity: 0, y: -30, duration: .25, ease: 'power2.in' }, t + .95);
        tl.set(ch, { visibility: 'hidden' }, t + 1.2);
        tl.to(terms(k), { color: '#1d1d1f', duration: .2 }, t + .95);
      }
      t += 1.25;
    });
    tl.to(all, { opacity: 1, duration: .3 }, t);
  }

  // ---------- Leistungs-Register: Linien ziehen sich durch ----------
  if (motion) $$('.reg-row').forEach(r => {
    gsap.to($('.rl', r), { scaleX: 1, ease: 'none', scrollTrigger: { trigger: r, start: 'top 92%', end: 'top 55%', scrub: .6 } });
    gsap.fromTo($$('.r-t, .r-d, .r-k', r), { opacity: 0, x: -24 }, { opacity: 1, x: 0, stagger: .06, ease: 'none', scrollTrigger: { trigger: r, start: 'top 90%', end: 'top 60%', scrub: .6 } });
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

  // ---------- Logo-Walze ----------
  const walze = $('.walze-sec');
  // Radius in Pixeln (Safari rechnet calc() in translateZ nicht)
  const ringSize = () => $$('.ring').forEach(r => {
    const cs = getComputedStyle(r.parentElement), w = parseFloat(cs.getPropertyValue('--w')), g = parseFloat(cs.getPropertyValue('--gap')), fs = $$('.face', r), n = fs.length;
    r.style.setProperty('--rad', (n * (w + g) / (2 * Math.PI)).toFixed(1) + 'px');
    fs.forEach((f, i) => f.style.setProperty('--ang', (i * 360 / n).toFixed(2) + 'deg'));
  });
  if (walze) { ringSize(); addEventListener('resize', ringSize); }
  if (walze && motion) {
    gsap.timeline({ scrollTrigger: { trigger: walze, start: 'top top', end: () => '+=' + innerHeight * 1.6, pin: '.walze-pin', scrub: .8, anticipatePin: 1 } })
      .fromTo('.ring.r1', { rotationY: 0 }, { rotationY: -200, ease: 'none' }, 0)
      .fromTo('.ring.r2', { rotationY: 12 }, { rotationY: 212, ease: 'none' }, 0);
  }

  // ---------- Blitz-Ausschnitt ----------
  const cut = $('.cutout');
  if (cut && motion) {
    const front = $('.cut-front', cut), pre = $('.cut-pre', cut);
    const B = [[63, 8], [54, 40.5], [78.5, 40.5], [67.5, 54.5], [33, 97], [46.5, 54.5], [24, 54.5]];
    const hole = s => {
      const w = front.offsetWidth, h = front.offsetHeight, size = Math.min(h * .42, w * .5) * s, cx = w / 2, cy = h * .45;
      const pts = B.map(([x, y]) => `${(cx + (x - 51) / 100 * size).toFixed(1)}px ${(cy + (y - 52) / 100 * size).toFixed(1)}px`);
      front.style.clipPath = `polygon(evenodd,0 0,100% 0,100% 100%,0 100%,0 0,${pts.join(',')},${pts[0]})`;
    };
    const o = { s: .9 };
    hole(o.s);
    gsap.timeline({ scrollTrigger: { trigger: cut, start: 'top top', end: () => '+=' + innerHeight * 1.4, pin: '.cut-pin', scrub: .7, anticipatePin: 1, invalidateOnRefresh: true, onRefresh: () => hole(o.s) } })
      .to(pre, { opacity: 0, y: -40, duration: .35 }, 0)
      .to(o, { s: 14, duration: 1, ease: 'power2.in', onUpdate: () => hole(o.s) }, .1)
      .fromTo('.cut-txt > *', { opacity: 0, y: 30 }, { opacity: 1, y: 0, stagger: .06, duration: .35 }, .55)
      .fromTo('.cut-person', { opacity: 0, x: 50 }, { opacity: 1, x: 0, duration: .35 }, .65)
      .set(front, { visibility: 'hidden' }, 1.1);
  }

  // ---------- Umschlag öffnet sich ----------
  $$('.envelope:not(.static)').forEach(env => {
    if (!motion) return;
    gsap.timeline({ scrollTrigger: { trigger: env, start: 'top 80%', end: 'top 30%', scrub: .7 } })
      .fromTo($('.env-flap', env), { rotationX: 0 }, { rotationX: 178, duration: .45, ease: 'power2.inOut' }, 0)
      .to($('.env-flap', env), { opacity: 0, duration: .15 }, .4)
      .fromTo($('.env-front', env), { yPercent: 0, opacity: 1 }, { yPercent: 40, opacity: 0, duration: .45, ease: 'power2.in' }, .35)
      .to($('.env-back', env), { opacity: 0, duration: .3 }, .55)
      .fromTo($('.letter', env), { y: 40, scale: .96 }, { y: 0, scale: 1, duration: .6, ease: 'power3.out' }, .3);
  });

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
