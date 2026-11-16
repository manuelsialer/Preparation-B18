/* ==========================================================================
   mathjax.js — carga e invocación de MathJax v3 para las fórmulas LaTeX.

   Las páginas de simulacro no incluyen MathJax (Sphinx solo lo añade donde
   detecta fórmulas), así que el motor lo inyecta y re-tipografía el contenido
   dinámico que genera.
   ========================================================================== */

var CDN = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';

/* Inyecta MathJax v3 una sola vez y habilita los delimitadores $...$. */
export function ensureMathJax() {
  if (window.__simMathJaxLoaded) return;
  window.__simMathJaxLoaded = true;
  if (window.MathJax) return;
  window.MathJax = {
    tex: {
      /* Solo \(...\) y \[...\]: los bancos usan "$" como símbolo monetario
         (soles), así que no puede ser delimitador de matemáticas. */
      inlineMath: [['\\(', '\\)']],
      displayMath: [['\\[', '\\]']]
    },
    options: { processHtmlClass: 'tex2jax_process|mathjax_process|math|output_area' }
  };
  var s = document.createElement('script');
  s.async = true;
  s.src = CDN;
  document.head.appendChild(s);
}

/* Re-tipografia un elemento ya montado (tras inyectar contenido dinámico). */
export function typeset(el) {
  if (!el || !window.MathJax) return;
  var MJ = window.MathJax;
  var run = function () {
    try {
      if (MJ.typesetPromise) { MJ.typesetPromise([el]).catch(function () {}); }
      else if (MJ.typeset) { MJ.typeset([el]); }
    } catch (e) { /* noop */ }
  };
  if (MJ.startup && MJ.startup.promise) {
    MJ.startup.promise.then(run).catch(function () {});
  } else {
    run();
  }
}

/* Habilita la sección del simulacro para MathJax: Sphinx la marca como
   ignorada, así que le quitamos esas clases y añadimos las de proceso. */
export function enableMathJaxOn(root) {
  try {
    Array.prototype.forEach.call(
      document.querySelectorAll('.tex2jax_ignore, .mathjax_ignore'),
      function (n) {
        n.classList.remove('tex2jax_ignore');
        n.classList.remove('mathjax_ignore');
      });
    root.classList.add('tex2jax_process');
    root.classList.add('mathjax_process');
  } catch (e) { /* noop */ }
}
