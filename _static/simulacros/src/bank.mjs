/* ==========================================================================
   bank.js — carga del banco JSON y persistencia del progreso.
   ========================================================================== */

/* Carga el banco con reintentos: el CDN de GitHub Pages puede devolver
   transitoriamente un error de red/404 mientras propaga un archivo nuevo,
   y algunos navegadores cachean esa respuesta fallida. */
export function loadBank(url, attempt) {
  attempt = attempt || 0;
  return fetch(url, { cache: attempt ? 'reload' : 'default' })
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .catch(function (err) {
      if (attempt >= 3) throw err;
      return new Promise(function (resolve) {
        setTimeout(resolve, 500 * (attempt + 1));
      }).then(function () { return loadBank(url, attempt + 1); });
    });
}

/* Almacén de progreso en localStorage, aislado por año. */
export function makeStore(prefix, year) {
  var key = prefix + (year || 'x');
  return {
    key: key,
    save: function (state) {
      try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) { /* privado */ }
    },
    restore: function () {
      try { return JSON.parse(localStorage.getItem(key)); } catch (e) { return null; }
    },
    wipe: function () {
      try { localStorage.removeItem(key); } catch (e) { /* noop */ }
    }
  };
}
