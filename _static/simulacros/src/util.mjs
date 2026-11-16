/* ==========================================================================
   util.js — utilidades de presentación del simulacro interactivo.
   Sin dependencias: DOM helpers, escape, texto enriquecido y reloj.
   ========================================================================== */

export var TOKEN_RE = /\[\[img:([A-Za-z0-9_.\-]+)\]\]/g;
export var LETTERS = ['A', 'B', 'C', 'D'];

/* Crea un elemento con clase e innerHTML opcionales. */
export function h(tag, cls, html) {
  var e = document.createElement(tag);
  if (cls) e.className = cls;
  if (html !== undefined && html !== null) e.innerHTML = html;
  return e;
}

/* Escapa los caracteres peligrosos para HTML. */
export function esc(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/* Texto enriquecido: escapa HTML, convierte saltos en <br> y los tokens
   [[img:archivo.png]] en <img>. El LaTeX ($...$) queda intacto para MathJax. */
export function rich(text, imgBase, imgClass) {
  var out = esc(text);
  out = out.replace(TOKEN_RE, function (_, file) {
    return '<img class="' + (imgClass || 'sim-inline-img') + '" src="' +
      imgBase + '/' + file + '" alt="recurso del examen" loading="lazy">';
  });
  return out.replace(/\n+/g, '<br>');
}

/* Pasaje: cada bloque separado por lineas en blanco es un parrafo. */
export function passageBody(html, imgBase) {
  var parts = String(html).split(/\n[ \t]*\n+/);
  var out = '';
  for (var i = 0; i < parts.length; i++) {
    var t = parts[i].replace(/\n+/g, ' ').trim();
    if (!t) continue;
    out += '<p class="sim-passage-line">' + rich(t, imgBase, 'sim-inline-img') + '</p>';
  }
  return out;
}

/* Formatea segundos como M:SS. */
export function fmtClock(total) {
  total = Math.max(0, Math.round(total));
  var m = Math.floor(total / 60);
  var s = total % 60;
  return m + ':' + (s < 10 ? '0' : '') + s;
}

/* Resuelve una ruta relativa contra el directorio del propio motor.
   Sphinx reescribe el src de simulacro.js segun la profundidad de la pagina,
   por lo que el directorio del script sirve como base estable. */
export function makeResolver(scriptBase) {
  return function resolveUrl(attr) {
    if (!attr) return attr;
    if (/^(https?:)?\/\//i.test(attr)) return attr;
    if (scriptBase && typeof URL !== 'undefined') {
      try { return new URL(attr, scriptBase).href; } catch (e) { return attr; }
    }
    return attr;
  };
}
