// =============================================================================
// DataFlujo — Waitlist (acceso anticipado a recursos)
// Conexión con Formspree — sin backend propio.
// Sustituir FORMSPREE_WAITLIST_AQUI por tu endpoint real de formspree.io
// =============================================================================

const FORMSPREE_WAITLIST = 'https://formspree.io/f/xaqayobk';

// Abrir el modal de waitlist con el nombre del recurso
function abrirWaitlist(btn) {
  const recurso = btn.dataset.recurso || 'este recurso';
  document.getElementById('wlRecurso').value             = recurso;
  document.getElementById('wlRecursoNombre').textContent = recurso;
  document.getElementById('msgWaitlist').style.display   = 'none';
  document.getElementById('formWaitlist').reset();
  // Restaurar el valor hidden tras el reset
  document.getElementById('wlRecurso').value             = recurso;
  document.getElementById('modalWaitlist').style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

// Cerrar el modal (clic en fondo o en botón cerrar)
function cerrarWaitlist(e) {
  if (e && e.target !== document.getElementById('modalWaitlist')) return;
  document.getElementById('modalWaitlist').style.display = 'none';
  document.body.style.overflow = '';
}

// Cerrar también con la tecla Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const modal = document.getElementById('modalWaitlist');
    if (modal && modal.style.display !== 'none') cerrarWaitlist();
  }
});

// Enviar la solicitud de acceso a Formspree
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('formWaitlist');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const email   = document.getElementById('wlEmail').value.trim();
    const recurso = document.getElementById('wlRecurso').value;
    const rgpd    = document.getElementById('wlRgpd').checked;
    const msg     = document.getElementById('msgWaitlist');
    const btn     = form.querySelector('button[type="submit"]');

    if (!rgpd) {
      mostrarMensajeWL(msg, 'Acepta la política de privacidad para continuar.', 'ko');
      return;
    }

    btn.disabled    = true;
    btn.textContent = 'Enviando...';

    try {
      const res = await fetch(FORMSPREE_WAITLIST, {
        method:  'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body:    JSON.stringify({
          email,
          recurso,
          tipo:   'waitlist',
          origen: window.location.pathname
        })
      });

      if (res.ok) {
        mostrarMensajeWL(msg, '¡Apuntado! Te aviso en cuanto esté disponible.', 'ok');
        setTimeout(() => cerrarWaitlist(), 2500);
      } else {
        mostrarMensajeWL(msg, 'Algo fue mal. Inténtalo de nuevo.', 'ko');
      }
    } catch {
      mostrarMensajeWL(msg, 'Sin conexión. Inténtalo de nuevo.', 'ko');
    } finally {
      btn.disabled    = false;
      btn.textContent = 'Apuntarme a la lista →';
    }
  });
});

// Mostrar mensaje de estado en el formulario
function mostrarMensajeWL(el, texto, tipo) {
  el.textContent   = texto;
  el.className     = `newsletter-msg ${tipo}`;
  el.style.display = 'block';
}

