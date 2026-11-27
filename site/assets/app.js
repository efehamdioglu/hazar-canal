(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
  };
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Üst bar: kaydırınca zemin */
  const top = $('.top');
  const onScroll = () => top && top.classList.toggle('is-solid', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Koleksiyon paneli (masaüstünde açılır panel, mobilde tam menü) */
  const mega = $('#mega');
  const openers = $$('[aria-controls="mega"]');
  const setMega = (open) => {
    if (!mega) return;
    mega.hidden = !open;
    top.classList.toggle('is-open', open);
    openers.forEach((b) => b.setAttribute('aria-expanded', String(open)));
  };
  openers.forEach((b) => b.addEventListener('click', () => setMega(mega.hidden)));
  addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mega && !mega.hidden) {
      setMega(false);
      (openers.find((b) => b.offsetParent) || openers[0]).focus();
    }
  });
  document.addEventListener('click', (e) => {
    if (mega && !mega.hidden && !e.target.closest('#mega, [aria-controls="mega"]')) setMega(false);
  });

  /* Mağaza: Türkiye / International */
  const setStore = (v) => {
    document.documentElement.dataset.store = v;
    store.set('hc-store', v);
    $$('[data-set-store]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.setStore === v)));
  };
  $$('[data-set-store]').forEach((b) => b.addEventListener('click', () => setStore(b.dataset.setStore)));
  setStore(document.documentElement.dataset.store === 'int' ? 'int' : 'tr');

  /* Ses: Şahmaran — Hazar Canal */
  const audio = $('#hc-audio');
  const soundBtns = $$('.sound');
  if (audio) {
    const sync = () => soundBtns.forEach((b) => b.setAttribute('aria-pressed', String(!audio.paused)));
    soundBtns.forEach((b) => b.addEventListener('click', () => {
      if (audio.paused) { audio.volume = 0.6; audio.play().catch(() => {}); } else audio.pause();
    }));
    audio.addEventListener('play', sync);
    audio.addEventListener('pause', sync);
  }

  /* Videolar: yalnızca görünürken oynat */
  const vids = $$('video[data-src]');
  if (reduced) {
    vids.forEach((v) => { v.src = v.dataset.src; v.controls = true; v.preload = 'none'; });
  } else if ('IntersectionObserver' in window) {
    const vo = new IntersectionObserver((es) => es.forEach((e) => {
      const v = e.target;
      if (e.isIntersecting) {
        if (!v.src) v.src = v.dataset.src;
        v.play().catch(() => {});
      } else if (v.src) v.pause();
    }), { threshold: 0.15 });
    vids.forEach((v) => vo.observe(v));
  }

  /* Görünme hareketi */
  document.documentElement.classList.add('js');
  if ('IntersectionObserver' in window && !reduced) {
    const ro = new IntersectionObserver((es) => es.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); }
    }), { rootMargin: '0px 0px -8% 0px' });
    $$('.rv').forEach((el) => ro.observe(el));
  } else $$('.rv').forEach((el) => el.classList.add('in'));

  /* Mobil satın alma çubuğu: girişteki düğmeler ekrandan çıkınca görünür */
  const buybar = $('.buybar');
  const heroBuy = $('.phero__buy');
  if (buybar && heroBuy && 'IntersectionObserver' in window) {
    document.body.classList.add('has-buybar');
    new IntersectionObserver(([e]) => buybar.classList.toggle('is-on', !e.isIntersecting)).observe(heroBuy);
  }

  /* ---------- Kişilik testi ---------- */
  const quiz = $('#quiz');
  if (quiz) {
    const data = JSON.parse($('#quiz-data').textContent);
    const qs = $$('.q', quiz);
    const intro = $('.quiz__intro', quiz);
    const result = $('.quiz__result', quiz);
    const bar = $('.quiz__bar i', quiz);
    const back = $('#q-back');
    const next = $('#q-next');
    const nav = $('.quiz__nav', quiz);
    let i = -1;

    const show = (n) => {
      i = n;
      intro.hidden = n !== -1;
      result.hidden = n !== qs.length;
      qs.forEach((q, k) => (q.hidden = k !== n));
      nav.hidden = n < 0 || n >= qs.length;
      bar.style.width = (Math.max(0, n) / qs.length) * 100 + '%';
      if (n >= 0 && n < qs.length) {
        back.disabled = n === 0;
        next.disabled = !$('input:checked', qs[n]);
        next.firstChild.textContent = n === qs.length - 1 ? 'Sonucumu Göster' : 'Devam';
        const first = $('input:checked', qs[n]) || $('input', qs[n]);
        first.focus({ preventScroll: true });
      }
      scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
    };

    const finish = () => {
      const scores = { Devil: 0, Barbaros: 0, Sahmaran: 0, Atlas: 0, Arora: 0 };
      $$('input:checked', quiz).forEach((inp) => {
        const w = data.weights[inp.value];
        if (w) Object.keys(w).forEach((p) => (scores[p] += w[p]));
      });
      let best = null, bestScore = -999;
      Object.keys(scores).forEach((p) => { if (scores[p] > bestScore) { bestScore = scores[p]; best = p; } });
      const p = data.perfumes[best];
      quiz.dataset.p = p.slug;
      $('#r-name').textContent = p.name;
      $('#r-desc').textContent = p.desc;
      $('#r-page').href = p.slug + '.html';
      $('#r-buy').href = p.url;
      const max = Math.max(...Object.values(scores), 1);
      $('#r-scores').innerHTML = Object.keys(scores)
        .sort((a, b) => scores[b] - scores[a])
        .map((k) => `<li><span>${data.perfumes[k].name}</span><i style="transform:scaleX(${(scores[k] / max).toFixed(3)})"></i></li>`)
        .join('');
      show(qs.length);
      bar.style.width = '100%';
      $('#r-name').focus({ preventScroll: true });
    };

    const advance = () => (i === qs.length - 1 ? finish() : show(i + 1));

    $('#q-start').addEventListener('click', () => show(0));
    back.addEventListener('click', () => i > 0 && show(i - 1));
    next.addEventListener('click', advance);
    qs.forEach((q) => {
      q.addEventListener('change', () => (next.disabled = false));
      // Fareyle/dokunarak seçince kendiliğinden ilerle; klavyede "Devam" ile ilerlenir.
      q.addEventListener('click', (e) => {
        if (e.target.matches('input') && e.detail > 0) setTimeout(advance, 320);
      });
    });
    $('#r-again').addEventListener('click', () => {
      $$('input:checked', quiz).forEach((x) => (x.checked = false));
      delete quiz.dataset.p;
      show(0);
    });
  }
})();
