// =============================================================================
// DataFlujo — Newsletter
// Conexión con Formspree — sin backend propio.
// Sustituir FORMSPREE_ENDPOINT_AQUI por tu endpoint real de formspree.io
// =============================================================================

const FORMSPREE_URL = 'FORMSPREE_ENDPOINT_AQUI';

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('formNewsletter');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('emailNewsletter').value.trim();
    const rgpd  = document.getElementById('rgpdNewsletter').checked;
    const msg   = document.getElementById('msgNewsletter');
    const btn   = form.querySelector('.btn-newsletter');

    if (!rgpd) {
      mostrarMensaje(msg, 'Acepta la política de privacidad para continuar.', 'ko');
      return;
    }

    btn.disabled    = true;
    btn.textContent = 'Enviando...';

    try {
      const res = await fetch(FORMSPREE_URL, {
        method:  'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body:    JSON.stringify({
          email,
          tipo:   'newsletter',
          origen: window.location.pathname
        })
      });

      if (res.ok) {
        mostrarMensaje(msg, '¡Apuntado! Te escribo en el próximo envío.', 'ok');
        form.reset();
      } else {
        mostrarMensaje(msg, 'Algo fue mal. Inténtalo de nuevo.', 'ko');
      }
    } catch {
      mostrarMensaje(msg, 'Sin conexión. Inténtalo de nuevo.', 'ko');
    } finally {
      btn.disabled    = false;
      btn.textContent = 'Suscribirme →';
    }
  });
});

// Mostrar mensaje de feedback en el formulario
function mostrarMensaje(el, texto, tipo) {
  el.textContent   = texto;
  el.className     = `newsletter-msg ${tipo}`;
  el.style.display = 'block';
}
