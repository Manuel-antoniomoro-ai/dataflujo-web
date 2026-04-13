// ─────────────────────────────────────────────────────────────────────────────
// DataFlujo — Backend de Email
// Gestiona los envíos de los formularios de contacto y del modal de productos
// hacia a.morodia@hotmail.com via SMTP de Outlook/Hotmail
// ─────────────────────────────────────────────────────────────────────────────

require('dotenv').config();
const express    = require('express');
const cors       = require('cors');
const nodemailer = require('nodemailer');
const fs         = require('fs');
const path       = require('path');

// Asegurarse de que el directorio data/ y waitlist.json existen al arrancar
const DATA_DIR      = path.join(__dirname, 'data');
const WAITLIST_FILE = path.join(DATA_DIR, 'waitlist.json');
if (!fs.existsSync(DATA_DIR))      fs.mkdirSync(DATA_DIR, { recursive: true });
if (!fs.existsSync(WAITLIST_FILE)) fs.writeFileSync(WAITLIST_FILE, '[]', 'utf8');

const app  = express();
const PORT = process.env.PORT || 3001;

// ── Middleware ────────────────────────────────────────────────────────────────
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Permite peticiones desde ficheros HTML abiertos localmente (file://)
// y desde cualquier origen local. En producción, restringe aquí tu dominio.
app.use(cors({
  origin: [
    'null',            // peticiones file:// en Chrome/Edge
    'http://localhost',
    'http://localhost:3000',
    'http://127.0.0.1',
    /http:\/\/localhost:\d+/
  ],
  methods: ['POST', 'GET', 'OPTIONS'],
  allowedHeaders: ['Content-Type']
}));

// ── Transporte SMTP ───────────────────────────────────────────────────────────
const transporter = nodemailer.createTransport({
  host:   process.env.SMTP_HOST || 'smtp.gmail.com',
  port:   parseInt(process.env.SMTP_PORT) || 587,
  secure: false,          // STARTTLS en el puerto 587
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  }
});

// Verifica la conexión al arrancar
transporter.verify((err) => {
  if (err) {
    console.error('❌  Error SMTP:', err.message);
    console.error('   Revisa tus credenciales en el fichero .env');
  } else {
    console.log('✅  SMTP conectado — listo para enviar emails');
  }
});

// ── Helper: enviar email ──────────────────────────────────────────────────────
async function sendMail({ subject, html, replyTo }) {
  return transporter.sendMail({
    from: `"DataFlujo Web" <${process.env.SMTP_USER}>`,
    to:   process.env.TO_EMAIL || 'a.morodia@hotmail.com',
    replyTo: replyTo || undefined,
    subject,
    html
  });
}

// ── Helper: sanitizar strings ─────────────────────────────────────────────────
function esc(str = '') {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Helper: plantilla HTML del email ─────────────────────────────────────────
function emailTemplate({ title, rows, note }) {
  const rowsHtml = rows
    .filter(([, v]) => v)
    .map(([label, value]) => `
      <tr>
        <td style="padding:10px 16px;font-family:Arial,sans-serif;font-size:13px;
                   color:#6b7280;font-weight:600;text-transform:uppercase;
                   letter-spacing:.06em;white-space:nowrap;width:160px;
                   border-bottom:1px solid #f3f4f6">${esc(label)}</td>
        <td style="padding:10px 16px;font-family:Arial,sans-serif;font-size:14px;
                   color:#111827;border-bottom:1px solid #f3f4f6">${esc(value)}</td>
      </tr>`)
    .join('');

  return `<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f9fafb;font-family:Arial,sans-serif">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f9fafb;padding:40px 0">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08)">

        <!-- Cabecera -->
        <tr>
          <td style="background:#0f1f40;padding:28px 32px">
            <p style="margin:0;font-family:Arial,sans-serif;font-size:11px;
                      font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                      color:rgba(255,255,255,.5)">DataFlujo</p>
            <h1 style="margin:8px 0 0;font-size:20px;font-weight:700;
                       color:#ffffff;line-height:1.3">${esc(title)}</h1>
          </td>
        </tr>

        <!-- Datos -->
        <tr>
          <td style="padding:8px 0">
            <table width="100%" cellpadding="0" cellspacing="0">
              ${rowsHtml}
            </table>
          </td>
        </tr>

        ${note ? `
        <!-- Mensaje largo -->
        <tr>
          <td style="padding:8px 32px 24px">
            <p style="margin:0 0 6px;font-family:Arial,sans-serif;font-size:11px;
                      font-weight:700;letter-spacing:.08em;text-transform:uppercase;
                      color:#6b7280">Mensaje</p>
            <div style="background:#f9fafb;border-radius:6px;padding:16px;
                        font-family:Arial,sans-serif;font-size:14px;color:#374151;
                        line-height:1.7;white-space:pre-wrap">${esc(note)}</div>
          </td>
        </tr>` : ''}

        <!-- Pie -->
        <tr>
          <td style="padding:20px 32px;border-top:1px solid #f3f4f6">
            <p style="margin:0;font-family:Arial,sans-serif;font-size:12px;
                      color:#9ca3af">Enviado desde el formulario web de dataflujo.com
              · ${new Date().toLocaleString('es-ES', { timeZone: 'Europe/Madrid' })}</p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>`;
}

// ─────────────────────────────────────────────────────────────────────────────
// POST /api/contact  — Formulario de contacto.html
// ─────────────────────────────────────────────────────────────────────────────
app.post('/api/contact', async (req, res) => {
  const { name, company, email, phone, tipo, message } = req.body;

  // Validación básica
  if (!name || !email || !message) {
    return res.status(400).json({ ok: false, error: 'Faltan campos obligatorios: name, email, message' });
  }

  const tipoLabel = {
    producto:    'Pregunta sobre un recurso',
    consultoria: 'Consultoría puntual',
    formacion:   'Formación o mentoring',
    otro:        'Otro'
  }[tipo] || tipo || '—';

  try {
    await sendMail({
      subject:  `[Contacto Web] ${name}${company ? ` · ${company}` : ''}`,
      replyTo:  email,
      html: emailTemplate({
        title: '📩 Nuevo mensaje de contacto',
        rows: [
          ['Nombre',  name],
          ['Empresa', company],
          ['Email',   email],
          ['Teléfono', phone],
          ['Motivo',  tipoLabel]
        ],
        note: message
      })
    });

    console.log(`[${new Date().toISOString()}] Contacto de ${name} <${email}>`);
    res.json({ ok: true });

  } catch (err) {
    console.error('Error enviando email de contacto:', err.message);
    res.status(500).json({ ok: false, error: 'Error al enviar el email. Inténtalo de nuevo.' });
  }
});

// ─────────────────────────────────────────────────────────────────────────────
// POST /api/modal  — Modal de productos.html (solicitar información)
// ─────────────────────────────────────────────────────────────────────────────
app.post('/api/modal', async (req, res) => {
  const { name, email, whatsapp, product } = req.body;

  // Validación básica
  if (!name || !email || !whatsapp) {
    return res.status(400).json({ ok: false, error: 'Faltan campos obligatorios: name, email, whatsapp' });
  }

  try {
    await sendMail({
      subject:  `[Interés producto] ${product || 'sin especificar'} — ${name}`,
      replyTo:  email,
      html: emailTemplate({
        title: `🛒 Solicitud de información`,
        rows: [
          ['Producto',  product || '—'],
          ['Nombre',    name],
          ['Email',     email],
          ['WhatsApp',  whatsapp]
        ],
        note: null
      })
    });

    console.log(`[${new Date().toISOString()}] Modal: ${name} <${email}> → ${product}`);
    res.json({ ok: true });

  } catch (err) {
    console.error('Error enviando email de modal:', err.message);
    res.status(500).json({ ok: false, error: 'Error al enviar el email. Inténtalo de nuevo.' });
  }
});

// ─────────────────────────────────────────────────────────────────────────────
// POST /api/waitlist  — Registro en la lista de espera de productos
// Guarda la entrada en data/waitlist.json y envía notificación por email.
// ─────────────────────────────────────────────────────────────────────────────
app.post('/api/waitlist', async (req, res) => {
  const { nombre, email, producto } = req.body;

  // Validación básica de campos obligatorios
  if (!nombre || !email) {
    return res.status(400).json({ ok: false, error: 'Faltan campos obligatorios: nombre, email' });
  }

  const entrada = {
    nombre,
    email,
    producto: producto || '—',
    fecha:    new Date().toISOString()
  };

  // Persistir en waitlist.json (lectura → append → escritura)
  try {
    const contenido = fs.readFileSync(WAITLIST_FILE, 'utf8');
    const lista     = JSON.parse(contenido);
    lista.push(entrada);
    fs.writeFileSync(WAITLIST_FILE, JSON.stringify(lista, null, 2), 'utf8');
  } catch (errArchivo) {
    console.error('Error al guardar en waitlist.json:', errArchivo.message);
    // Continúa — intenta enviar el email aunque falle el fichero
  }

  // Enviar notificación por email al administrador
  try {
    await sendMail({
      subject: `[Waitlist] ${producto || 'recurso'} — ${nombre}`,
      replyTo: email,
      html: emailTemplate({
        title: '🔔 Nueva entrada en la waitlist',
        rows: [
          ['Nombre',   nombre],
          ['Email',    email],
          ['Producto', producto || '—']
        ],
        note: null
      })
    });

    console.log(`[${new Date().toISOString()}] Waitlist: ${nombre} <${email}> → ${producto}`);
    res.json({ ok: true });

  } catch (err) {
    console.error('Error enviando email de waitlist:', err.message);
    // El registro ya fue guardado; devolvemos ok aunque el email falle
    res.json({ ok: true, warning: 'Registro guardado pero el email de notificación falló.' });
  }
});

// ── Health check ──────────────────────────────────────────────────────────────
app.get('/api/health', (_, res) => {
  res.json({ ok: true, time: new Date().toISOString() });
});

// ── Arrancar servidor ─────────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`\n🚀 DataFlujo email backend corriendo en http://localhost:${PORT}`);
  console.log(`   Endpoints:`);
  console.log(`   POST http://localhost:${PORT}/api/contact`);
  console.log(`   POST http://localhost:${PORT}/api/modal`);
  console.log(`   GET  http://localhost:${PORT}/api/health\n`);
});
