/* ==========================================================================
   engine.js — máquina de estados del simulacro interactivo.

   Flujo: intro → corrida (temporizador + marcado) → resultados + análisis.
   Depende de util.js (presentación), mathjax.js (fórmulas) y bank.js
   (carga del banco y persistencia).
   ========================================================================== */
import { makeResolver, LETTERS, h, esc, rich, passageBody, fmtClock } from './util.mjs';
import { ensureMathJax, typeset, enableMathJaxOn } from './mathjax.mjs';
import { loadBank, makeStore } from './bank.mjs';

var STORE_PREFIX = 'simB18::';

/* Arranque completo: prepara MathJax y monta el motor en cada simulacro.
   Lo invoca la entrada clásica (simulacro.js) tras importar este módulo. */
export function start(scriptBase) {
  ensureMathJax();
  bootAll(makeResolver(scriptBase));
}

/* Monta el motor en cada <div class="simulacro" data-bank=...>. */
export function bootAll(resolveUrl) {
  function start() {
    Array.prototype.forEach.call(
      document.querySelectorAll('div.simulacro[data-bank]'),
      function (root) { init(root, resolveUrl); });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
}

function init(root, resolveUrl) {
  var bankUrl = resolveUrl(root.getAttribute('data-bank'));
  var imgBase = resolveUrl(root.getAttribute('data-img')).replace(/\/+$/, '');
  var bank = null;
  var state = null;          // {i, answers, timeLeft, finished, started}
  var timerId = null;
  var store = null;

  enableMathJaxOn(root);

  /* ------------------------------------------------ persistencia ---- */
  function save() { if (store) store.save(state); }
  function restore() { return store ? store.restore() : null; }
  function wipe() { if (store) store.wipe(); }

  /* ------------------------------------------------ helpers --------- */
  function sectionOf(q) {
    for (var i = 0; i < bank.sections.length; i++) {
      var s = bank.sections[i];
      if (q.id >= s.from && q.id <= s.to) return s;
    }
    return bank.sections[0];
  }

  function stats() {
    var total = { ok: 0, bad: 0, blank: 0 };
    var bySec = {};
    bank.sections.forEach(function (s) {
      bySec[s.id] = { label: s.label, ok: 0, bad: 0, blank: 0 };
    });
    bank.questions.forEach(function (q) {
      var a = state.answers[q.id];
      var b = bySec[sectionOf(q).id];
      var k = !a ? 'blank' : (a === q.answer ? 'ok' : 'bad');
      b[k]++;
      total[k]++;
    });
    return { total: total, bySec: bySec };
  }

  function mount(el) {
    root.innerHTML = '';
    root.appendChild(el);
    typeset(root);
  }

  /* ------------------------------------------------ intro ----------- */
  function viewIntro() {
    var secs = bank.sections.map(function (s) {
      return s.label + ' (' + s.from + '–' + s.to + ')';
    }).join(' · ');
    var v = h('div', 'sim-view');
    v.innerHTML =
      '<div class="sim-card sim-card-center">' +
      '<h3 class="sim-title">' + esc(bank.title) + '</h3>' +
      '<p class="sim-muted">' + bank.questions.length +
      ' preguntas · ' + esc(secs) + ' · ' + bank.duration_min + ' minutos</p>' +
      '<ul class="sim-instructions">' +
      '<li>El temporizador de <b>' + bank.duration_min + ' minutos</b> arranca al pulsar «Iniciar» y el examen se entrega automáticamente al llegar a 00:00.</li>' +
      '<li>Puedes marcar y cambiar tus respuestas libremente antes de finalizar.</li>' +
      '<li>Al finalizar verás tu puntaje, el desglose por sección y el <b>análisis detallado de cada falla</b> (tu respuesta frente a la clave oficial).</li>' +
      '<li>Tu progreso queda guardado en este navegador: si cierras la página puedes continuar donde quedaste.</li>' +
      '</ul>' +
      '<button type="button" class="sim-btn sim-btn-primary sim-btn-lg sim-start">Iniciar simulacro</button>' +
      '</div>';
    v.querySelector('.sim-start').addEventListener('click', function () {
      state = {
        started: true,
        finished: false,
        i: 0,
        answers: {},
        timeLeft: bank.duration_min * 60
      };
      save();
      startTimer();
      viewRun();
    });
    mount(v);
  }

  function viewIntroError(msg) {
    var v = h('div', 'sim-view');
    v.innerHTML =
      '<div class="sim-card sim-card-center"><p class="sim-error">' +
      esc(msg) + '</p></div>';
    mount(v);
  }

  /* ------------------------------------------------ corrida --------- */
  function viewRun() {
    var v = h('div', 'sim-view sim-run');

    var top = h('div', 'sim-topbar');
    top.innerHTML =
      '<button type="button" class="sim-btn sim-btn-ghost sim-prev">‹ Anterior</button>' +
      '<span class="sim-timer" role="timer">' + fmtClock(state.timeLeft) + '</span>' +
      '<span class="sim-progress"></span>' +
      '<button type="button" class="sim-btn sim-btn-danger sim-finish">Finalizar</button>';
    v.appendChild(top);

    var body = h('div', 'sim-body');
    var main = h('div', 'sim-main');
    var side = h('aside', 'sim-side');
    body.appendChild(main);
    body.appendChild(side);
    v.appendChild(body);

    v.querySelector('.sim-prev').addEventListener('click', function () {
      go(state.i - 1);
    });
    v.querySelector('.sim-finish').addEventListener('click', function () {
      if (window.confirm('¿Finalizar el simulacro? Tiempo empleado: ' +
        fmtClock(bank.duration_min * 60 - state.timeLeft) +
        ' · respondidas: ' + answeredCount() + '/' + bank.questions.length)) {
        finish(false);
      }
    });

    mount(v);
    renderNavigator(side);
    renderQuestion(main, top);
  }

  function answeredCount() {
    return Object.keys(state.answers).length;
  }

  function startTimer() {
    clearInterval(timerId);
    var ticks = 0;
    timerId = setInterval(function () {
      if (!state || state.finished) { clearInterval(timerId); return; }
      state.timeLeft--;
      ticks++;
      if (ticks % 5 === 0) save();
      var chip = root.querySelector('.sim-timer');
      if (chip) {
        chip.textContent = fmtClock(state.timeLeft);
        chip.classList.toggle('sim-warn', state.timeLeft <= 600);
        chip.classList.toggle('sim-alert', state.timeLeft <= 120);
      }
      if (state.timeLeft <= 0) finish(true);
    }, 1000);
  }

  function go(i) {
    if (i < 0 || i >= bank.questions.length) return;
    state.i = i;
    save();
    var main = root.querySelector('.sim-main');
    var top = root.querySelector('.sim-topbar');
    var side = root.querySelector('.sim-side');
    if (main) {
      renderQuestion(main, top);
      renderNavigator(side);
    }
  }

  function renderNavigator(side) {
    if (!side) return;
    side.innerHTML = '';
    side.appendChild(h('div', 'sim-side-title', 'Tarjeta de respuestas'));
    var grid = h('div', 'sim-nav');
    var prevSec = null;
    bank.questions.forEach(function (q, idx) {
      var sec = sectionOf(q);
      if (prevSec !== null && sec.id !== prevSec) {
        grid.appendChild(h('div', 'sim-nav-break'));
      }
      prevSec = sec.id;
      var cell = h('button', 'sim-nav-cell', String(q.id));
      cell.type = 'button';
      cell.dataset.qid = q.id;
      cell.addEventListener('click', function () { go(idx); });
      grid.appendChild(cell);
    });
    side.appendChild(grid);
    side.appendChild(h('div', 'sim-legend',
      '<span class="sim-dot sim-dot-ok"></span> respondida &nbsp;' +
      '<span class="sim-dot"></span> pendiente'));
    side.appendChild(h('button', 'sim-btn sim-btn-ghost sim-jump-end',
      'Ir al final »')).addEventListener('click', function () {
        go(bank.questions.length - 1);
      });
    paintNavigator();
  }

  function paintNavigator() {
    var grid = root.querySelector('.sim-nav');
    if (!grid) return;
    Array.prototype.forEach.call(grid.querySelectorAll('.sim-nav-cell'), function (cell) {
      var qid = Number(cell.dataset.qid);
      cell.classList.toggle('sim-nav-ok', !!state.answers[qid]);
      cell.classList.toggle('sim-nav-cur', qid === bank.questions[state.i].id);
    });
    var p = root.querySelector('.sim-progress');
    if (p) p.textContent = 'Respondidas ' + answeredCount() + '/' + bank.questions.length;
  }

  function renderQuestion(main, top) {
    var q = bank.questions[state.i];
    var sec = sectionOf(q);
    main.innerHTML = '';

    var card = h('div', 'sim-card sim-question');
    card.appendChild(h('div', 'sim-q-head',
      '<span class="sim-badge">' + esc(sec.label) + '</span>' +
      '<span class="sim-q-num">Pregunta ' + q.id + ' de ' + bank.questions.length + '</span>'));

    appendPassage(card, q);

    card.appendChild(h('div', 'sim-stem', rich(q.stem, imgBase, 'sim-inline-img')));
    appendFigures(card, q);

    var opts = h('div', 'sim-options');
    q.options.forEach(function (opt, k) {
      var letter = LETTERS[k];
      var b = h('button', 'sim-option');
      b.type = 'button';
      b.innerHTML =
        '<span class="sim-letter">' + letter + '</span>' +
        '<span class="sim-opt-text">' + rich(opt, imgBase, 'sim-inline-img') + '</span>';
      b.dataset.letter = letter;
      b.addEventListener('click', function () {
        state.answers[q.id] = letter;
        save();
        paintOptions(card, q);
        paintNavigator();
      });
      opts.appendChild(b);
    });
    card.appendChild(opts);
    main.appendChild(card);

    var nav = h('div', 'sim-q-nav');
    nav.innerHTML =
      '<button type="button" class="sim-btn sim-prev">‹ Anterior</button>' +
      '<button type="button" class="sim-btn sim-btn-primary sim-next">Siguiente ›</button>';
    nav.querySelector('.sim-prev').addEventListener('click', function () { go(state.i - 1); });
    nav.querySelector('.sim-next').addEventListener('click', function () { go(state.i + 1); });
    main.appendChild(nav);

    typeset(main);
    paintOptions(card, q);
    paintNavigator();
    var chip = root.querySelector('.sim-timer');
    if (chip) chip.textContent = fmtClock(state.timeLeft);
    if (top && top.querySelector('.sim-progress')) {
      top.querySelector('.sim-progress').textContent =
        'Respondidas ' + answeredCount() + '/' + bank.questions.length;
    }
    main.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  /* Bloque de lectura opcional asociado a la pregunta. */
  function appendPassage(card, q) {
    if (!q.passage) return;
    var p = bank.passages[q.passage - 1];
    var t = (p && p.title) ? p.title : 'Lectura ' + q.passage;
    var det = h('details', 'sim-passage');
    det.open = true;
    det.innerHTML =
      '<summary>Lectura · ' + esc(t) + '</summary>' +
      '<div class="sim-passage-body">' +
      passageBody(p ? p.html : '', imgBase) + '</div>';
    card.appendChild(det);
  }

  /* Figuras de la pregunta (recortes del examen). */
  function appendFigures(card, q) {
    if (!q.images || !q.images.length) return;
    var figs = h('div', 'sim-figures');
    q.images.forEach(function (f) {
      var wrap = h('div', 'sim-figure');
      wrap.innerHTML = '<img class="sim-fig-img" src="' + imgBase + '/' + esc(f) +
        '" alt="figura del examen" loading="lazy">';
      figs.appendChild(wrap);
    });
    card.appendChild(figs);
  }

  function paintOptions(card, q) {
    var picked = state.answers[q.id];
    Array.prototype.forEach.call(card.querySelectorAll('.sim-option'), function (b) {
      b.classList.toggle('sim-option-sel', b.dataset.letter === picked);
    });
  }

  /* ------------------------------------------------ final ----------- */
  function finish(auto) {
    clearInterval(timerId);
    state.finished = true;
    state.used = bank.duration_min * 60 - Math.max(0, state.timeLeft);
    save();
    viewResults(auto);
  }

  function viewResults(auto) {
    var st = stats();
    var used = (typeof state.used === 'number')
      ? state.used
      : bank.duration_min * 60 - Math.max(0, state.timeLeft);
    var pct = Math.round((100 * st.total.ok) / bank.questions.length);

    var v = h('div', 'sim-view sim-results');

    var summary = h('div', 'sim-card sim-card-center sim-summary');
    summary.innerHTML =
      '<p class="sim-muted">' + (auto ? 'Tiempo agotado — entrega automática' : 'Simulacro finalizado') + '</p>' +
      '<h3 class="sim-title">' + esc(bank.title) + '</h3>' +
      '<div class="sim-score"><span class="sim-score-num">' + st.total.ok + '</span>' +
      '<span class="sim-score-den">/ ' + bank.questions.length + '</span>' +
      '<span class="sim-score-pct">(' + pct + ' %)</span></div>' +
      '<p class="sim-muted">Tiempo empleado: ' + fmtClock(used) + ' de ' + bank.duration_min + ':00 min</p>' +
      '<table class="sim-table"><thead><tr><th>Sección</th><th>Correctas</th>' +
      '<th>Incorrectas</th><th>Sin responder</th></tr></thead><tbody>' +
      bank.sections.map(function (s) {
        var b = st.bySec[s.id];
        return '<tr><td>' + esc(b.label) + '</td><td>' + b.ok + '</td><td>' +
          b.bad + '</td><td>' + b.blank + '</td></tr>';
      }).join('') +
      '<tr class="sim-table-total"><td>Total</td><td>' + st.total.ok + '</td><td>' +
      st.total.bad + '</td><td>' + st.total.blank + '</td></tr>' +
      '</tbody></table>' +
      '<button type="button" class="sim-btn sim-btn-ghost sim-retry">Reintentar simulacro</button>';
    v.appendChild(summary);

    var filters = h('div', 'sim-filters');
    filters.innerHTML =
      '<span class="sim-muted">Análisis de fallas:</span> ' +
      '<button type="button" class="sim-btn sim-btn-primary sim-btn-small sim-fl" data-f="bad">Falladas y sin responder</button>' +
      '<button type="button" class="sim-btn sim-btn-ghost sim-btn-small sim-fl" data-f="all">Todas</button>' +
      '<button type="button" class="sim-btn sim-btn-ghost sim-btn-small sim-fl" data-f="ok">Solo correctas</button>';
    v.appendChild(filters);

    var list = h('div', 'sim-review');
    v.appendChild(list);

    function paintReviews(mode) {
      list.innerHTML = '';
      var shown = 0;
      bank.questions.forEach(function (q) {
        var a = state.answers[q.id];
        var ok = a === q.answer;
        var status = !a ? 'blank' : (ok ? 'ok' : 'bad');
        if (mode === 'bad' && status === 'ok') return;
        if (mode === 'ok' && status !== 'ok') return;
        shown++;
        list.appendChild(reviewCard(q, a, status));
      });
      if (!shown) {
        list.appendChild(h('div', 'sim-card sim-card-center sim-muted',
          mode === 'bad' ? '¡Sin fallas! Respondiste todo correctamente. 🎉' :
            'Nada que mostrar con este filtro.'));
      }
      typeset(list);
    }

    Array.prototype.forEach.call(filters.querySelectorAll('.sim-fl'), function (b) {
      b.addEventListener('click', function () {
        Array.prototype.forEach.call(filters.querySelectorAll('.sim-fl'), function (x) {
          x.className = x.className.replace('sim-btn-primary', 'sim-btn-ghost');
        });
        b.className = b.className.replace('sim-btn-ghost', 'sim-btn-primary');
        paintReviews(b.dataset.f);
      });
    });

    summary.querySelector('.sim-retry').addEventListener('click', function () {
      if (!window.confirm('¿Reiniciar el simulacro? Se borrará tu intento actual.')) return;
      wipe();
      state = null;
      clearInterval(timerId);
      viewIntro();
    });

    mount(v);
    /* filtro inicial: fallas y sin responder (si no hay fallas, todas) */
    var first = (st.total.bad + st.total.blank) > 0 ? 'bad' : 'all';
    Array.prototype.forEach.call(filters.querySelectorAll('.sim-fl'), function (b) {
      if (b.dataset.f === first) b.click();
    });
  }

  function reviewCard(q, a, status) {
    var sec = sectionOf(q);
    var badge = status === 'ok'
      ? '<span class="sim-badge sim-badge-ok">✓ Correcta</span>'
      : status === 'bad'
        ? '<span class="sim-badge sim-badge-bad">✗ Incorrecta</span>'
        : '<span class="sim-badge sim-badge-blank">○ Sin responder</span>';

    var card = h('div', 'sim-card sim-review-card');
    card.innerHTML =
      '<div class="sim-q-head">' +
      '<span class="sim-badge">' + esc(sec.label) + '</span>' +
      '<span class="sim-q-num">Pregunta ' + q.id + '</span>' + badge + '</div>';

    appendPassage(card, q);
    card.appendChild(h('div', 'sim-stem', rich(q.stem, imgBase, 'sim-inline-img')));
    appendFigures(card, q);

    var opts = h('div', 'sim-options sim-options-review');
    q.options.forEach(function (opt, k) {
      var letter = LETTERS[k];
      var cls = 'sim-option sim-option-static';
      var note = '';
      if (letter === q.answer) {
        cls += ' sim-option-correct';
        note = '<span class="sim-note sim-note-ok">Clave oficial</span>';
      }
      if (a === letter && letter !== q.answer) {
        cls += ' sim-option-wrong';
        note = '<span class="sim-note sim-note-bad">Tu respuesta</span>';
      }
      if (a === letter && letter === q.answer) {
        note = '<span class="sim-note sim-note-ok">Clave oficial — tu respuesta</span>';
      }
      var b = h('div', cls);
      b.innerHTML =
        '<span class="sim-letter">' + letter + '</span>' +
        '<span class="sim-opt-text">' + rich(opt, imgBase, 'sim-inline-img') + '</span>' +
        note;
      opts.appendChild(b);
    });
    if (!a) {
      opts.appendChild(h('div', 'sim-muted sim-no-answer',
        'No marcaste ninguna alternativa (correcta: <b>' + q.answer + '</b>).'));
    }
    card.appendChild(opts);

    if (q.explain) {
      card.appendChild(h('div', 'sim-explain',
        '<b>💡 Explicación:</b> ' + rich(q.explain, imgBase, 'sim-inline-img')));
    }
    return card;
  }

  /* ------------------------------------------------ arranque -------- */
  function boot(b) {
    bank = b;
    store = makeStore(STORE_PREFIX, bank.year);
    var saved = restore();
    if (saved && saved.started && !saved.finished && saved.timeLeft > 0) {
      state = saved;
      startTimer();
      viewRun();
    } else if (saved && saved.finished) {
      state = saved;
      state.timeLeft = 0;
      viewResults(false);
    } else {
      wipe();
      viewIntro();
    }
  }

  loadBank(bankUrl)
    .then(boot)
    .catch(function (err) {
      viewIntroError('No se pudo cargar el banco del simulacro (' + err.message +
        '). Revisa tu conexión y vuelve a cargar la página.');
    });
}
