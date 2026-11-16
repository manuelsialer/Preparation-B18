/* ==========================================================================
   Simulacro interactivo — Examen Nacional de Preselección Beca 18
   Punto de entrada (script clásico). La lógica vive en ./src/ como módulos ES:

     util.mjs     — helpers de presentación (DOM, escape, texto enriquecido)
     mathjax.mjs  — carga de MathJax v3 y tipografiado de fórmulas LaTeX
     bank.mjs     — carga del banco JSON con reintentos + persistencia
     engine.mjs   — máquina de estados (intro → corrida → resultados)

   Por qué la entrada es un script clásico y los módulos usan .mjs:
     Jupyter Book auto-incluye globalmente TODO archivo .js bajo _static/
     (jupyter_book/config.py → html_js_files). Si los módulos fueran .js con
     import/export, se cargarían como scripts clásicos en cada página y
     lanzarían SyntaxError. La extensión .mjs evita esa auto-inclusión: los
     archivos se copian pero no se inyectan; esta entrada los importa de forma
     dinámica solo cuando la página contiene un simulacro. GitHub Pages sirve
     .mjs con Content-Type de JavaScript, por lo que el import funciona.

   Uso en la página:
     <div class="simulacro" data-bank=".../banks/2023.json"
                          data-img=".../img/2023"></div>
     <script src=".../simulacro.js"></script>
   ========================================================================== */
(function () {
  'use strict';
  if (window.__simBooted) return;   // la etiqueta <script> puede aparecer 2 veces
  window.__simBooted = true;

  /* Directorio del propio simulacro.js (Sphinx reescribe su src segun la
     profundidad de la pagina). Sirve de base para resolver los modulos y las
     rutas data-bank / data-img. */
  var BASE = (function () {
    try {
      var s = document.currentScript;
      if (!s) {
        var all = document.getElementsByTagName('script');
        for (var i = all.length - 1; i >= 0; i--) {
          if (all[i].src && all[i].src.indexOf('simulacro.js') !== -1) { s = all[i]; break; }
        }
      }
      if (s && s.src) return s.src.substring(0, s.src.lastIndexOf('/') + 1);
    } catch (e) { /* noop */ }
    return null;
  })();

  /* Importa el motor solo si la pagina trae un simulacro (evita cargar los
     módulos y MathJax en el resto del libro, donde simulacro.js también se
     inyecta globalmente). */
  function boot() {
    if (!BASE) return;
    if (!document.querySelector('div.simulacro[data-bank]')) return;
    import(new URL('src/engine.mjs', BASE).href)
      .then(function (engine) { engine.start(BASE); })
      .catch(function (e) {
        if (window.console && console.error) {
          console.error('simulacro: no se pudo cargar el motor', e);
        }
      });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
