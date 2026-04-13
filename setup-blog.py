#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DataFlujo Blog Setup Script
Crea la carpeta blog/ y los 6 articulos de blog completos.
Ejecutar desde el directorio del site: python setup-blog.py
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOG_DIR = os.path.join(BASE_DIR, "blog")
os.makedirs(BLOG_DIR, exist_ok=True)
print(f"[OK] Directorio creado: {BLOG_DIR}")

# ─────────────────────────────────────────────
# CSS COMPARTIDO
# ─────────────────────────────────────────────
CSS = """
:root{--bg:#ffffff;--bg2:#f8f8f6;--bg3:#f0f0ec;--t:#0a0a0a;--t2:#4a4a4a;--t3:#9a9a9a;--ac:#0f1f40;--ac2:#1a3a6b;--bd:rgba(0,0,0,.09);--bd2:rgba(0,0,0,.16);--r:4px;--s:0 2px 12px rgba(0,0,0,.06);--s2:0 8px 32px rgba(0,0,0,.11);--fb:'Inter','Segoe UI',system-ui,sans-serif;--fe:'Playfair Display',Georgia,serif;--fd:'Syne','Arial Black',sans-serif}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
body{font-family:var(--fb);background:var(--bg);color:var(--t);overflow-x:hidden;line-height:1.65}
img{max-width:100%;display:block}a{text-decoration:none;color:inherit}ul{list-style:none}
.cnt{max-width:1200px;margin:0 auto;padding:0 2rem}
.hdr{position:fixed;top:0;left:0;right:0;z-index:200;height:64px;background:#fff;border-bottom:1px solid var(--bd);transition:box-shadow .3s}
.hdr.scrolled{box-shadow:var(--s2)}
.hdr-inner{max-width:1200px;margin:0 auto;padding:0 2rem;height:100%;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:.65rem;line-height:1}
.logo-icon{display:flex;align-items:flex-end;color:var(--ac);flex-shrink:0}
.logo-brand{font-family:var(--fe);font-size:1.12rem;font-weight:700;line-height:1;letter-spacing:-.02em}
.logo-data{color:var(--t)}.logo-flujo{background:linear-gradient(90deg,#2563eb,#06b6d4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.logo-sub{font-family:var(--fd);font-size:.5rem;font-weight:600;color:var(--t3);letter-spacing:.1em;text-transform:uppercase;margin-top:3px}
.hnav{display:flex;align-items:center;gap:.25rem}
.hnav a{font-size:.83rem;font-weight:500;color:var(--t2);padding:.4rem .9rem;transition:color .2s;letter-spacing:.01em;font-family:var(--fd)}
.hnav a:hover,.hnav a.active{color:var(--t)}
.nav-cta{background:var(--ac)!important;color:#fff!important;padding:.4rem 1.1rem!important;font-weight:600!important}
.nav-cta:hover{background:var(--ac2)!important}
.mbtn{display:none;background:none;border:1px solid var(--bd);padding:.35rem .7rem;cursor:pointer;font-size:1rem}
.mnav{display:none;position:fixed;top:64px;left:0;right:0;background:#fff;border-bottom:1px solid var(--bd);padding:1rem 2rem;z-index:199;box-shadow:var(--s2)}
.mnav.open{display:flex;flex-direction:column;gap:.25rem}
.mnav a{font-size:.9rem;color:var(--t2);padding:.65rem 0;border-bottom:1px solid var(--bd);font-family:var(--fd)}
@media(max-width:768px){.hnav{display:none}.mbtn{display:block}}
.rv{opacity:0;transform:translateY(24px);transition:opacity .7s cubic-bezier(.22,1,.36,1),transform .7s cubic-bezier(.22,1,.36,1)}.rv.in{opacity:1;transform:none}
.d1{transition-delay:.1s}.d2{transition-delay:.2s}.d3{transition-delay:.3s}
.iz{overflow:hidden}.iz img{width:100%;display:block;transform:scale(1.07);transition:transform 1.4s cubic-bezier(.16,1,.3,1),opacity .8s ease;opacity:.88}
.iz.iz-in img{transform:scale(1);opacity:1}
.art-hero{position:relative;height:460px;margin-top:64px}
.art-hero-bg{position:absolute;inset:0}
.art-hero-bg img{width:100%;height:100%;object-fit:cover}
.art-hero-overlay{position:absolute;inset:0;background:rgba(8,14,28,.78);display:flex;align-items:flex-end;padding-bottom:3.5rem}
.art-hero-inner{max-width:860px;padding:0 2rem}
.art-crumb{display:flex;align-items:center;gap:.5rem;font-family:var(--fd);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.45);margin-bottom:1.25rem}
.art-crumb a{color:rgba(255,255,255,.45);transition:color .2s}.art-crumb a:hover{color:rgba(255,255,255,.8)}
.art-crumb span{color:rgba(255,255,255,.25)}
.art-cat{display:inline-block;font-family:var(--fd);font-size:.62rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#2563eb;margin-bottom:.75rem}
.art-title{font-family:var(--fe);font-size:clamp(1.9rem,4vw,2.8rem);font-weight:800;color:#fff;line-height:1.1;margin-bottom:1.25rem;max-width:760px}
.art-meta{display:flex;align-items:center;gap:1.5rem;font-family:var(--fd);font-size:.72rem;color:rgba(255,255,255,.45)}
.art-meta strong{color:rgba(255,255,255,.7)}
.art-body{max-width:760px;margin:0 auto;padding:72px 2rem 100px}
.art-body h2{font-family:var(--fe);font-size:1.65rem;font-weight:700;color:var(--t);margin:2.75rem 0 1rem;line-height:1.25}
.art-body h3{font-family:var(--fe);font-size:1.2rem;font-weight:700;color:var(--t);margin:2rem 0 .75rem}
.art-body p{font-size:.97rem;color:var(--t2);line-height:1.8;margin-bottom:1.2rem}
.art-body ul,.art-body ol{padding-left:1.5rem;margin-bottom:1.2rem}
.art-body li{font-size:.97rem;color:var(--t2);line-height:1.75;margin-bottom:.4rem}
.art-body ul li{list-style:disc}
.art-body ol li{list-style:decimal}
.art-body strong{color:var(--t);font-weight:600}
.art-body em{font-style:italic}
.art-body a{color:var(--ac);border-bottom:1px solid var(--bd2);transition:border-color .2s}.art-body a:hover{border-color:var(--ac)}
.art-lead{font-size:1.08rem;color:var(--t);line-height:1.85;margin-bottom:2rem;border-left:3px solid var(--ac);padding-left:1.25rem}
.art-quote{background:var(--bg2);border-left:4px solid var(--ac);padding:1.25rem 1.5rem;margin:2rem 0;border-radius:0 var(--r) var(--r) 0}
.art-quote p{margin-bottom:0;font-style:italic;color:var(--t)}
pre,.code-block{background:#0f1f40;color:#e2e8f0;padding:1.5rem;border-radius:var(--r);overflow-x:auto;margin:1.5rem 0;font-size:.82rem;line-height:1.7;font-family:'Consolas','Monaco',monospace}
code{background:#f0f0ec;color:#0f1f40;padding:.15rem .4rem;border-radius:3px;font-size:.84rem;font-family:'Consolas','Monaco',monospace}
pre code{background:none;color:inherit;padding:0;font-size:inherit}
.art-table{width:100%;border-collapse:collapse;margin:1.5rem 0;font-size:.88rem}
.art-table th{background:var(--ac);color:#fff;padding:.65rem 1rem;text-align:left;font-family:var(--fd);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase}
.art-table td{padding:.6rem 1rem;border-bottom:1px solid var(--bd);color:var(--t2);vertical-align:top}
.art-table tr:last-child td{border-bottom:none}
.art-table tr:nth-child(even) td{background:var(--bg2)}
.art-tip{background:#eff6ff;border:1px solid #bfdbfe;border-radius:var(--r);padding:1.1rem 1.25rem;margin:1.5rem 0}
.art-tip strong{display:block;font-family:var(--fd);font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:#2563eb;margin-bottom:.4rem}
.art-tip p{margin-bottom:0;font-size:.88rem;color:#1e3a5f}
.art-warn{background:#fff7ed;border:1px solid #fed7aa;border-radius:var(--r);padding:1.1rem 1.25rem;margin:1.5rem 0}
.art-warn strong{display:block;font-family:var(--fd);font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:#c2410c;margin-bottom:.4rem}
.art-warn p{margin-bottom:0;font-size:.88rem;color:#7c2d12}
.art-divider{border:none;border-top:1px solid var(--bd);margin:2.5rem 0}
.art-cta{background:var(--ac);border-radius:var(--r);padding:2.5rem;margin:3rem 0;text-align:center}
.art-cta h3{font-family:var(--fe);font-size:1.4rem;font-weight:700;color:#fff;margin-bottom:.75rem}
.art-cta p{font-size:.88rem;color:rgba(255,255,255,.65);margin-bottom:1.5rem;line-height:1.7}
.btn-white{display:inline-block;background:#fff;color:var(--ac);padding:.75rem 1.75rem;border-radius:var(--r);font-family:var(--fd);font-size:.82rem;font-weight:700;letter-spacing:.04em;transition:opacity .2s}.btn-white:hover{opacity:.88}
.art-related{border-top:1px solid var(--bd);padding-top:2.5rem;margin-top:1rem}
.art-related h4{font-family:var(--fd);font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--t3);margin-bottom:1.5rem}
.rel-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.25rem}
.rel-card{border:1px solid var(--bd);border-radius:var(--r);padding:1.25rem;transition:border-color .2s,box-shadow .2s}
.rel-card:hover{border-color:var(--bd2);box-shadow:var(--s)}
.rel-cat{font-family:var(--fd);font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ac);margin-bottom:.4rem}
.rel-title{font-family:var(--fe);font-size:.95rem;font-weight:700;color:var(--t);line-height:1.3}
@media(max-width:600px){.rel-grid{grid-template-columns:1fr}}
.footer{background:var(--t);color:#fff;padding:72px 0 32px}
.ft-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}
.ft-brand p{font-size:.83rem;color:rgba(255,255,255,.45);margin-top:1rem;line-height:1.7}
.ft-social{margin-top:1.25rem;display:flex;flex-direction:column;gap:.4rem}
.ft-link{font-size:.8rem;color:rgba(255,255,255,.45);transition:color .2s}.ft-link:hover{color:#fff}
.ft-col h4{font-family:var(--fd);font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.35);margin-bottom:1rem}
.ft-col ul li{margin-bottom:.5rem}
.ft-col ul li a{font-size:.83rem;color:rgba(255,255,255,.5);transition:color .2s}.ft-col ul li a:hover{color:#fff}
.ft-bot{border-top:1px solid rgba(255,255,255,.08);padding-top:1.5rem}
.ft-bot p{font-size:.75rem;color:rgba(255,255,255,.28)}
@media(max-width:768px){.ft-grid{grid-template-columns:1fr 1fr;gap:2rem}.ft-brand{grid-column:1/-1}}
@media(max-width:480px){.ft-grid{grid-column:1fr}}
"""

# ─────────────────────────────────────────────
# HEADER / FOOTER / JS COMPARTIDOS
# ─────────────────────────────────────────────
HEADER = """<header class="hdr" id="hdr">
  <div class="hdr-inner">
    <a href="../index.html" class="logo">
      <div class="logo-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 46" width="38" height="34" aria-hidden="true"><rect x="2" y="25" width="9" height="18" rx="1.5" fill="currentColor" opacity=".7"/><rect x="14" y="12" width="9" height="31" rx="1.5" fill="currentColor" opacity=".7"/><rect x="26" y="29" width="9" height="14" rx="1.5" fill="currentColor" opacity=".7"/><rect x="38" y="3" width="9" height="40" rx="1.5" fill="#2563eb"/><rect x="0" y="44" width="50" height="2" rx="1" fill="currentColor"/></svg></div>
      <div><div class="logo-brand"><span class="logo-data">Data</span><span class="logo-flujo">Flujo</span></div><div class="logo-sub">by antonio-moro.es</div></div>
    </a>
    <nav class="hnav">
      <a href="../index.html">Inicio</a>
      <a href="../productos.html">Productos</a>
      <a href="../blog.html" class="active">Blog</a>
      <a href="../sobre-mi.html">Sobre m&#237;</a>
      <a href="../contacto.html" class="nav-cta">Contacto</a>
    </nav>
    <button class="mbtn" id="mbtn">&#9776;</button>
  </div>
</header>
<nav class="mnav" id="mnav">
  <a href="../index.html">Inicio</a>
  <a href="../productos.html">Productos</a>
  <a href="../blog.html">Blog</a>
  <a href="../sobre-mi.html">Sobre m&#237;</a>
  <a href="../contacto.html">Contacto</a>
</nav>"""

FOOTER = """<footer class="footer">
  <div class="cnt">
    <div class="ft-grid">
      <div class="ft-brand">
        <a href="../index.html" class="logo">
          <div class="logo-icon" style="color:rgba(255,255,255,.6)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 46" width="38" height="34" aria-hidden="true"><rect x="2" y="25" width="9" height="18" rx="1.5" fill="currentColor" opacity=".7"/><rect x="14" y="12" width="9" height="31" rx="1.5" fill="currentColor" opacity=".7"/><rect x="26" y="29" width="9" height="14" rx="1.5" fill="currentColor" opacity=".7"/><rect x="38" y="3" width="9" height="40" rx="1.5" fill="#93c5fd"/><rect x="0" y="44" width="50" height="2" rx="1" fill="currentColor"/></svg></div>
          <div><div class="logo-brand" style="color:#fff"><span class="logo-data" style="color:#fff">Data</span><span class="logo-flujo" style="color:#93c5fd">Flujo</span></div><div class="logo-sub" style="color:rgba(255,255,255,.38)">by antonio-moro.es</div></div>
        </a>
        <p>Recursos digitales de Data Engineering &amp; BI con 20+ a&ntilde;os de experiencia real en producci&oacute;n.</p>
        <div class="ft-social">
          <a href="mailto:hola@antonio-moro.es" class="ft-link">hola@antonio-moro.es</a>
          <a href="https://linkedin.com/in/antonio-moro-diaz-62346213b" target="_blank" class="ft-link">LinkedIn</a>
          <a href="https://github.com/antonio-moro" target="_blank" class="ft-link">GitHub</a>
        </div>
      </div>
      <div class="ft-col">
        <h4>Recursos</h4>
        <ul>
          <li><a href="../productos.html">Power BI Templates</a></li>
          <li><a href="../productos.html">SQL Pack</a></li>
          <li><a href="../productos.html">dbt Starter</a></li>
        </ul>
      </div>
      <div class="ft-col">
        <h4>P&aacute;ginas</h4>
        <ul>
          <li><a href="../blog.html">Blog</a></li>
          <li><a href="../sobre-mi.html">Sobre m&#237;</a></li>
          <li><a href="../contacto.html">Contacto</a></li>
        </ul>
      </div>
      <div class="ft-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="../contacto.html">Aviso legal</a></li>
        </ul>
      </div>
    </div>
    <div class="ft-bot">
      <p>&copy; 2025 DataFlujo &middot; antonio-moro.es &middot; Todos los derechos reservados</p>
    </div>
  </div>
</footer>"""

JS = """<script>
const ro=new IntersectionObserver(e=>e.forEach(v=>{if(v.isIntersecting){v.target.classList.add('in');ro.unobserve(v.target)}}),{threshold:.08,rootMargin:'0px 0px -30px 0px'});
document.querySelectorAll('.rv').forEach(el=>ro.observe(el));
const zo=new IntersectionObserver(e=>e.forEach(v=>{if(v.isIntersecting){v.target.classList.add('iz-in');zo.unobserve(v.target)}}),{threshold:.06});
document.querySelectorAll('.iz').forEach(el=>zo.observe(el));
window.addEventListener('scroll',()=>document.querySelector('.hdr').classList.toggle('scrolled',window.scrollY>20));
document.getElementById('mbtn')?.addEventListener('click',()=>document.getElementById('mnav').classList.toggle('open'));
</script>"""

ICON = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%230f1f40' rx='12'/><rect x='8' y='54' width='18' height='38' rx='3' fill='white' opacity='.7'/><rect x='30' y='28' width='18' height='64' rx='3' fill='white' opacity='.7'/><rect x='52' y='60' width='18' height='32' rx='3' fill='white' opacity='.7'/><rect x='74' y='6' width='18' height='86' rx='3' fill='%232563eb'/><rect x='4' y='94' width='92' height='4' rx='2' fill='white' opacity='.5'/></svg>"
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Syne:wght@600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'

def page(title, desc, body_html):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{desc}">
<title>{title} &mdash; DataFlujo</title>
<link rel="icon" href="{ICON}">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{HEADER}
{body_html}
{FOOTER}
{JS}
</body>
</html>"""

# ════════════════════════════════════════════
# ARTICULO 1: ETL vs ELT
# ════════════════════════════════════════════
art1_body = """
<div class="art-hero">
  <div class="art-hero-bg iz">
    <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1400&auto=format&fit=crop&q=80" alt="Infraestructura de datos cloud">
  </div>
  <div class="art-hero-overlay">
    <div class="art-hero-inner">
      <nav class="art-crumb rv" aria-label="breadcrumb">
        <a href="../index.html">Inicio</a><span>/</span>
        <a href="../blog.html">Blog</a><span>/</span>
        <span>ETL</span>
      </nav>
      <span class="art-cat">ETL</span>
      <h1 class="art-title rv d1">ETL vs ELT en 2025: &iquest;cu&aacute;l domina el mercado cloud?</h1>
      <div class="art-meta rv d2">
        <span>Por <strong>Antonio Moro</strong></span>
        <span>12 Mar 2025</span>
        <span>8 min lectura</span>
      </div>
    </div>
  </div>
</div>

<article class="art-body">
  <p class="art-lead rv">Durante m&aacute;s de dos d&eacute;cadas trabajando en proyectos de datos, he visto c&oacute;mo el paradigma ETL &mdash;que durante a&ntilde;os fue la &uacute;nica opci&oacute;n v&aacute;lida&mdash; ha cedido terreno de forma dr&aacute;stica frente al ELT en entornos cloud. No es una cuesti&oacute;n de moda: es un cambio estructural impulsado por la capacidad de c&oacute;mputo casi ilimitada de plataformas como BigQuery, Snowflake o Redshift.</p>

  <h2 class="rv">Qu&eacute; es ETL y c&oacute;mo funciona</h2>
  <p><strong>ETL</strong> (Extract, Transform, Load) es el proceso cl&aacute;sico de integraci&oacute;n de datos. Los datos se extraen de los sistemas fuente, se transforman en un servidor intermedio y <em>despu&eacute;s</em> se cargan ya procesados en el Data Warehouse. La transformaci&oacute;n ocurre <strong>antes</strong> de llegar al repositorio central.</p>
<pre><code>FUENTES           SERVIDOR ETL             DESTINO
[CRM]    --+
[ERP]    --+-&gt; [EXTRACT] -&gt; [TRANSFORM] -&gt; [LOAD] -&gt; [DWH]
[Web]    --+
[APIs]        (limpieza, joins,           (datos ya
               reglas de negocio)          transformados)</code></pre>
  <p>El servidor ETL act&uacute;a como intermediario. Toda la l&oacute;gica de transformaci&oacute;n &mdash;limpieza, normalizaci&oacute;n, c&aacute;lculos derivados, joins entre tablas de distintas fuentes&mdash; se ejecuta en ese motor. Esto requiere recursos de c&oacute;mputo propios y suele ser el cuello de botella en vol&uacute;menes grandes.</p>

  <h2 class="rv">Qu&eacute; es ELT y por qu&eacute; el cloud lo cambi&oacute; todo</h2>
  <p><strong>ELT</strong> (Extract, Load, Transform) invierte el orden: los datos se cargan <em>en bruto</em> directamente en el Data Warehouse cloud y las transformaciones se ejecutan <strong>dentro</strong> del propio DWH usando la potencia de c&oacute;mputo nativo del cloud.</p>
<pre><code>FUENTES           DESTINO CLOUD                TRANSFORMACION
[CRM]    --+
[ERP]    --+-&gt; [EXTRACT] -&gt; [LOAD RAW] -&gt; [TRANSFORM SQL] -&gt; [MARTS]
[Web]    --+
[APIs]        (datos en bruto,              (SQL sobre BigQuery /
               sin procesar)                Snowflake / Redshift)</code></pre>

  <div class="art-tip">
    <strong>Dato clave</strong>
    <p>BigQuery procesa 1 TB por unos 5 USD. Un servidor ETL dedicado para hacer lo mismo on-premise puede costar cientos de euros/hora en licencias e infraestructura. Esta diferencia de coste es lo que hace que ELT sea el nuevo est&aacute;ndar.</p>
  </div>

  <p>Plataformas como <strong>Google BigQuery</strong>, <strong>Snowflake</strong> o <strong>Amazon Redshift</strong> ejecutan transformaciones SQL complejas sobre terabytes en segundos usando arquitectura MPP (Massively Parallel Processing). El coste marginal de transformar in-situ es tan bajo que ya no tiene sentido pagar por un servidor ETL dedicado.</p>

  <h2 class="rv">Herramientas ETL cl&aacute;sicas</h2>

  <h3>Informatica PowerCenter / IDMC</h3>
  <p>El est&aacute;ndar de facto durante 20 a&ntilde;os en entornos enterprise. Ofrece entorno visual potente, excelente soporte 24/7, conectores para cualquier sistema imaginable y capacidades avanzadas de calidad de dato. Su principal desventaja: el <strong>precio</strong>. Una licencia enterprise puede superar los 200.000 &euro;/a&ntilde;o. Su nueva versi&oacute;n cloud IDMC (Informatica Data Management Cloud) ha modernizado el portfolio pero mantiene el modelo de precios premium.</p>

  <h3>Microsoft SSIS</h3>
  <p>Integrado en el ecosistema Microsoft, es la elecci&oacute;n natural para empresas con SQL Server. La herramienta visual de dise&ntilde;o de paquetes es familiar para equipos de DBA. Sus limitaciones aparecen en escalabilidad horizontal y entornos no-Microsoft. Con Azure Data Factory, Microsoft ha pivotado hacia un modelo m&aacute;s cercano al ELT moderno.</p>

  <h3>Talend</h3>
  <p>Open source con versi&oacute;n enterprise. Buen equilibrio precio/funcionalidad. Genera c&oacute;digo Java ejecutable, lo que puede ser una ventaja (portabilidad) o desventaja (complejidad de depuraci&oacute;n). Adquirido por Qlik en 2023, el roadmap tiene cierta incertidumbre.</p>

  <h2 class="rv">Herramientas ELT modernas</h2>

  <h3>dbt (data build tool)</h3>
  <p>Se ha convertido en el est&aacute;ndar de transformaci&oacute;n ELT. dbt no mueve datos: ejecuta SQL <em>dentro</em> del DWH y a&ntilde;ade gesti&oacute;n de dependencias, tests autom&aacute;ticos, documentaci&oacute;n y linaje de datos. Compatible con BigQuery, Snowflake, Redshift, Databricks y m&aacute;s. Su enfoque SQL-first lo hace accesible a cualquier analista.</p>

  <h3>Fivetran</h3>
  <p>Conector gestionado para la fase de ingesta (Extract + Load). M&aacute;s de 300 conectores predefinidos y mantenidos autom&aacute;ticamente. Precio por fila procesada puede ser alto en vol&uacute;menes grandes, pero el ahorro en mantenimiento justifica el coste en la mayor&iacute;a de proyectos medianos.</p>

  <h3>Airbyte</h3>
  <p>Alternativa open source a Fivetran. M&aacute;s de 350 conectores, disponible self-hosted o como Airbyte Cloud. Ideal para equipos que quieren control total sobre la infraestructura. Los conectores personalizados son f&aacute;ciles de construir gracias al SDK en Python.</p>

  <h2 class="rv">Comparativa ETL vs ELT</h2>
  <table class="art-table">
    <thead><tr><th>Criterio</th><th>ETL cl&aacute;sico</th><th>ELT moderno</th></tr></thead>
    <tbody>
      <tr><td><strong>Rendimiento a escala</strong></td><td>Limitado por servidor intermedio</td><td>Escala con el DWH cloud (MPP)</td></tr>
      <tr><td><strong>Coste infraestructura</strong></td><td>Alto (servidor ETL dedicado)</td><td>Bajo (pago por consulta en DWH)</td></tr>
      <tr><td><strong>Latencia</strong></td><td>Alta (transform antes de cargar)</td><td>Baja (carga inmediata, transform on-demand)</td></tr>
      <tr><td><strong>Flexibilidad cambios</strong></td><td>R&iacute;gida (redise&ntilde;ar jobs)</td><td>Alta (cambiar SQL en dbt, deploy en segundos)</td></tr>
      <tr><td><strong>Linaje y documentaci&oacute;n</strong></td><td>Variable seg&uacute;n herramienta</td><td>Excelente (dbt genera DAG y docs autom&aacute;ticos)</td></tr>
      <tr><td><strong>Privacidad PII antes de DWH</strong></td><td>S&iacute; (anonimizar antes de cargar)</td><td>Requiere controles extra en el DWH</td></tr>
      <tr><td><strong>Requiere DWH cloud potente</strong></td><td>No</td><td>S&iacute; (BigQuery, Snowflake, Redshift)</td></tr>
      <tr><td><strong>Curva de aprendizaje</strong></td><td>Alta (herramientas propietarias)</td><td>Media (SQL + Git + dbt)</td></tr>
    </tbody>
  </table>

  <h2 class="rv">Cu&aacute;ndo todav&iacute;a tiene sentido el ETL cl&aacute;sico</h2>
  <p>El ETL cl&aacute;sico no desaparece, pero queda relegado a nichos espec&iacute;ficos:</p>
  <ul>
    <li><strong>Regulaci&oacute;n estricta (GDPR, PCI-DSS, HIPAA):</strong> cuando los datos PII o datos de tarjetas no pueden almacenarse en bruto en ning&uacute;n sistema antes de ser anonimizados. ETL garantiza que el dato sensible nunca toca el DWH sin transformar.</li>
    <li><strong>Sistemas legacy on-premise:</strong> si tu DWH es SQL Server 2012 o un Teradata antiguo, no tienes la capacidad de c&oacute;mputo para ejecutar transformaciones pesadas in-situ.</li>
    <li><strong>Calidad de dato cr&iacute;tica pre-carga:</strong> en banca o seguros puede ser obligatorio rechazar registros inv&aacute;lidos antes de que lleguen al repositorio central.</li>
    <li><strong>Transformaciones no-SQL complejas:</strong> cuando la l&oacute;gica requiere Python, Java o procesamiento imperativo que no se puede expresar limpiamente en SQL.</li>
  </ul>

  <div class="art-warn">
    <strong>Ojo con la inercia</strong>
    <p>Si tu empresa ya est&aacute; en cloud y mantienes ETL cl&aacute;sico por costumbre, est&aacute;s pagando dos veces: el servidor ETL y el DWH cloud. Eval&uacute;a la migraci&oacute;n a ELT antes de renovar licencias.</p>
  </div>

  <h2 class="rv">Casos de uso reales</h2>

  <h3>Caso 1: Retailer con 50M de transacciones diarias</h3>
  <p>Un cliente del sector retail pasaba 4 horas cada noche ejecutando jobs SSIS para transformar logs de ventas antes de cargarlos en SQL Server DWH. Tras migrar a <strong>Airbyte + BigQuery + dbt</strong>, el proceso completo tard&oacute; 18 minutos. El coste mensual de infraestructura baj&oacute; un 60% y el equipo pas&oacute; de mantener 200 paquetes SSIS a 40 modelos dbt versionados en Git.</p>

  <h3>Caso 2: Banco con datos de tarjetas (PCI-DSS)</h3>
  <p>Una entidad bancaria mantiene Informatica PowerCenter para la ingesta de transacciones. Los datos PAN (Primary Account Number) se tokenizan en el servidor Informatica <em>antes</em> de llegar al DWH. Este es un caso donde el ETL sigue siendo la arquitectura correcta: PCI-DSS exige minimizar los datos de tarjetas lo antes posible en el flujo.</p>

  <div class="art-quote">
    <p>&ldquo;El mejor pipeline de datos es aquel que tu equipo puede entender, modificar y mantener. En 2025, ese pipeline suele estar escrito en SQL y versionado en Git.&rdquo;</p>
  </div>

  <h2 class="rv">Conclusi&oacute;n</h2>
  <p>En 2025, si est&aacute;s construyendo un nuevo proyecto de datos sobre cualquier DWH cloud, <strong>ELT es el enfoque por defecto</strong>. La combinaci&oacute;n Fivetran/Airbyte (ingesta) + dbt (transformaci&oacute;n) + BigQuery/Snowflake (compute) es el stack m&aacute;s adoptado por los mejores equipos de datos del mundo. El ETL cl&aacute;sico sobrevive en nichos muy espec&iacute;ficos de cumplimiento regulatorio y sistemas legacy.</p>

  <hr class="art-divider">
  <div class="art-cta rv">
    <h3>Pack de plantillas dbt listas para BigQuery y Snowflake</h3>
    <p>Modelos dbt de staging, marts y core con tests gen&eacute;ricos preconfigurados, documentaci&oacute;n autom&aacute;tica y estructura de carpetas lista para producci&oacute;n. Ahorra semanas de configuraci&oacute;n inicial.</p>
    <a href="../productos.html" class="btn-white">Ver recursos &rarr;</a>
  </div>
  <div class="art-related rv">
    <h4>Tambi&eacute;n te puede interesar</h4>
    <div class="rel-grid">
      <a href="dbt-data-warehouse-2025.html" class="rel-card">
        <div class="rel-cat">Cloud</div>
        <div class="rel-title">dbt en 2025: el est&aacute;ndar del Data Warehouse moderno</div>
      </a>
      <a href="sql-window-functions.html" class="rel-card">
        <div class="rel-cat">SQL</div>
        <div class="rel-title">SQL Window Functions: la gu&iacute;a definitiva con 20 ejemplos</div>
      </a>
    </div>
  </div>
</article>
"""

# ════════════════════════════════════════════
# ARTICULO 2: DAX TOP 10
# ════════════════════════════════════════════
art2_body = """
<div class="art-hero">
  <div class="art-hero-bg iz">
    <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1400&auto=format&fit=crop&q=80" alt="Dashboard de Business Intelligence">
  </div>
  <div class="art-hero-overlay">
    <div class="art-hero-inner">
      <nav class="art-crumb rv" aria-label="breadcrumb">
        <a href="../index.html">Inicio</a><span>/</span>
        <a href="../blog.html">Blog</a><span>/</span>
        <span>BI</span>
      </nav>
      <span class="art-cat">BI</span>
      <h1 class="art-title rv d1">TOP 10 funciones DAX que todo analista BI debe dominar</h1>
      <div class="art-meta rv d2">
        <span>Por <strong>Antonio Moro</strong></span>
        <span>28 Feb 2025</span>
        <span>6 min lectura</span>
      </div>
    </div>
  </div>
</div>

<article class="art-body">
  <p class="art-lead rv">Despu&eacute;s de revisar m&aacute;s de 200 modelos Power BI en proyectos enterprise, siempre encuentro los mismos patrones: quienes dominan estas 10 funciones DAX construyen modelos que funcionan en producci&oacute;n. Quienes no, generan medidas lentas, resultados incorrectos o paneles que nadie entiende. Aqu&iacute; est&aacute;n, con ejemplos reales.</p>

  <h2 class="rv">1. CALCULATE &mdash; el coraz&oacute;n de DAX</h2>
  <p>CALCULATE es, con diferencia, la funci&oacute;n m&aacute;s importante de DAX. Eval&uacute;a una expresi&oacute;n modificando el contexto de filtro. Sin ella, no puedes hacer casi ninguna medida avanzada.</p>
<pre><code>-- Sintaxis
CALCULATE(&lt;expresion&gt;, [&lt;filtro1&gt;], [&lt;filtro2&gt;], ...)

-- Ejemplo: ventas solo de la categoria "Electronica"
Ventas Electronica =
CALCULATE(
    SUM(Ventas[Importe]),
    Productos[Categoria] = "Electronica"
)

-- Ejemplo: ventas acumuladas del anyo
Ventas YTD =
CALCULATE(
    SUM(Ventas[Importe]),
    DATESYTD(Calendario[Fecha])
)</code></pre>
  <p><strong>Cu&aacute;ndo usarla:</strong> siempre que necesites modificar el contexto de filtro de una expresi&oacute;n. Es la base de casi todas las medidas de inteligencia temporal, comparativas y ratios.</p>

  <h2 class="rv">2. FILTER &mdash; filtrado din&aacute;mico de tablas</h2>
  <p>FILTER devuelve una tabla filtrada. Se usa habitualmente como argumento dentro de CALCULATE cuando el filtro es m&aacute;s complejo que una simple igualdad.</p>
<pre><code>-- Sintaxis
FILTER(&lt;tabla&gt;, &lt;condicion&gt;)

-- Ejemplo: clientes con mas de 10 pedidos
Clientes Alto Volumen =
CALCULATE(
    COUNTROWS(Pedidos),
    FILTER(
        Clientes,
        [Total Pedidos Cliente] &gt; 10
    )
)

-- Ejemplo: productos con precio superior a la media
Ventas Premium =
CALCULATE(
    SUM(Ventas[Importe]),
    FILTER(Productos, Productos[Precio] &gt; AVERAGE(Productos[Precio]))
)</code></pre>

  <h2 class="rv">3. ALL / ALLEXCEPT &mdash; eliminar filtros</h2>
  <p>ALL elimina todos los filtros de una tabla o columna. ALLEXCEPT elimina todos los filtros <em>excepto</em> los de las columnas especificadas. Son esenciales para calcular porcentajes sobre el total.</p>
<pre><code>-- % sobre total general
% del Total =
DIVIDE(
    SUM(Ventas[Importe]),
    CALCULATE(SUM(Ventas[Importe]), ALL(Ventas))
)

-- % sobre total de la categoria (pero respetando el filtro de fecha)
% Categoria =
DIVIDE(
    SUM(Ventas[Importe]),
    CALCULATE(
        SUM(Ventas[Importe]),
        ALLEXCEPT(Productos, Productos[Categoria])
    )
)</code></pre>

  <h2 class="rv">4. SUMX / AVERAGEX &mdash; iteradores fila a fila</h2>
  <p>Las funciones X iteran sobre cada fila de una tabla y eval&uacute;an una expresi&oacute;n. Son imprescindibles cuando necesitas calcular algo por fila antes de agregar.</p>
<pre><code>-- Margen total: precio * (1 - descuento) * cantidad
Margen Total =
SUMX(
    Ventas,
    Ventas[Cantidad] * (Ventas[PrecioUnitario] - Ventas[Coste])
)

-- Precio medio ponderado por volumen
Precio Medio Ponderado =
DIVIDE(
    SUMX(Ventas, Ventas[Cantidad] * Ventas[PrecioUnitario]),
    SUM(Ventas[Cantidad])
)</code></pre>

  <h2 class="rv">5. RANKX &mdash; ranking din&aacute;mico</h2>
  <p>RANKX asigna un rango a cada elemento de una tabla seg&uacute;n una expresi&oacute;n. Ideal para TOP N din&aacute;micos en tablas y visualizaciones.</p>
<pre><code>-- Ranking de productos por ventas
Ranking Producto =
RANKX(
    ALL(Productos[Nombre]),
    [Ventas Totales],
    ,
    DESC,
    DENSE
)</code></pre>
  <div class="art-tip">
    <strong>Tip</strong>
    <p>Usa DENSE para evitar saltos en el ranking (1,2,2,3 en lugar de 1,2,2,4). Especialmente importante en dashboards de ejecutivos donde los saltos generan confusi&oacute;n.</p>
  </div>

  <h2 class="rv">6. DIVIDE &mdash; divisi&oacute;n segura</h2>
  <p>DIVIDE maneja autom&aacute;ticamente la divisi&oacute;n por cero devolviendo un valor alternativo (por defecto BLANK). Nunca uses el operador / directamente en medidas de ratio.</p>
<pre><code>-- Nunca hagas esto:
Margen % MALO = [Beneficio] / [Ventas]   -- error si Ventas = 0

-- Siempre usa DIVIDE:
Margen % =
DIVIDE(
    [Beneficio],
    [Ventas],
    0   -- valor alternativo si denominador = 0
)

-- Tasa de conversion
Tasa Conversion =
DIVIDE([Pedidos Completados], [Visitas], BLANK())</code></pre>

  <h2 class="rv">7. DATEADD / SAMEPERIODLASTYEAR &mdash; inteligencia temporal</h2>
  <p>Estas funciones son la base de cualquier comparativa temporal. SAMEPERIODLASTYEAR es un atajo de DATEADD con -1 a&ntilde;o.</p>
<pre><code>-- Ventas mismo periodo anyo anterior
Ventas AA =
CALCULATE(
    SUM(Ventas[Importe]),
    SAMEPERIODLASTYEAR(Calendario[Fecha])
)

-- Variacion YoY en %
YoY % =
DIVIDE([Ventas Totales] - [Ventas AA], [Ventas AA])

-- Ventas hace 3 meses
Ventas 3M Antes =
CALCULATE(
    SUM(Ventas[Importe]),
    DATEADD(Calendario[Fecha], -3, MONTH)
)</code></pre>

  <h2 class="rv">8. RELATED &mdash; navegar relaciones</h2>
  <p>RELATED trae un valor de una tabla relacionada (del lado "uno" de una relaci&oacute;n 1-N). Se usa en columnas calculadas, no en medidas.</p>
<pre><code>-- En tabla Ventas, traer la categoria del producto
Categoria Venta = RELATED(Productos[Categoria])

-- Margen por linea usando coste de la tabla Productos
Margen Linea =
Ventas[Importe] - (Ventas[Cantidad] * RELATED(Productos[CosteUnitario]))</code></pre>

  <h2 class="rv">9. SWITCH &mdash; l&oacute;gica condicional limpia</h2>
  <p>SWITCH reemplaza cadenas de IF anidados con una sintaxis mucho m&aacute;s legible. Especialmente &uacute;til para segmentaciones y etiquetas.</p>
<pre><code>-- Segmentacion de clientes por volumen
Segmento Cliente =
SWITCH(
    TRUE(),
    [Ventas Cliente] &gt;= 100000, "Platinum",
    [Ventas Cliente] &gt;= 50000,  "Gold",
    [Ventas Cliente] &gt;= 10000,  "Silver",
    "Standard"
)

-- Etiqueta de semaforo
Estado KPI =
SWITCH(
    TRUE(),
    [Margen %] &gt;= 0.20, "Verde",
    [Margen %] &gt;= 0.10, "Amarillo",
    "Rojo"
)</code></pre>

  <h2 class="rv">10. VAR &mdash; variables para medidas limpias y eficientes</h2>
  <p>VAR permite declarar variables dentro de una medida, mejorando la legibilidad y el rendimiento (la expresi&oacute;n se eval&uacute;a una sola vez). Es una buena pr&aacute;ctica usar VAR en cualquier medida moderadamente compleja.</p>
<pre><code>-- Sin VAR: repetimos el calculo de ventas tres veces
Ratio Complicado =
DIVIDE(SUM(Ventas[Importe]) - SUM(Ventas[Coste]), SUM(Ventas[Importe]))

-- Con VAR: limpio, eficiente y facil de depurar
Margen % Limpio =
VAR TotalVentas = SUM(Ventas[Importe])
VAR TotalCoste  = SUM(Ventas[Coste])
VAR Beneficio   = TotalVentas - TotalCoste
RETURN
DIVIDE(Beneficio, TotalVentas, 0)

-- VAR para evitar recalculos en medidas temporales
Crecimiento YoY =
VAR VentasActual = SUM(Ventas[Importe])
VAR VentasAA =
    CALCULATE(
        SUM(Ventas[Importe]),
        SAMEPERIODLASTYEAR(Calendario[Fecha])
    )
RETURN
DIVIDE(VentasActual - VentasAA, VentasAA, BLANK())</code></pre>

  <div class="art-tip">
    <strong>Regla de oro</strong>
    <p>Si una medida tiene m&aacute;s de 3 l&iacute;neas, usa VAR. Si tiene m&aacute;s de 5, es obligatorio. El depurador de DAX Studio te lo agradece.</p>
  </div>

  <hr class="art-divider">
  <div class="art-cta rv">
    <h3>Dashboard Kit con m&aacute;s de 50 medidas DAX listas para usar</h3>
    <p>Plantillas Power BI con medidas DAX de producci&oacute;n para ventas, finanzas, RRHH y log&iacute;stica. Documentadas, optimizadas y listas para adaptar a tu modelo de datos.</p>
    <a href="../productos.html" class="btn-white">Ver recursos &rarr;</a>
  </div>
  <div class="art-related rv">
    <h4>Tambi&eacute;n te puede interesar</h4>
    <div class="rel-grid">
      <a href="kimball-vs-data-vault.html" class="rel-card">
        <div class="rel-cat">Cloud</div>
        <div class="rel-title">Kimball vs Data Vault 2.0: &iquest;qu&eacute; modelo DWH elegir?</div>
      </a>
      <a href="informatica-vs-talend-2025.html" class="rel-card">
        <div class="rel-cat">Tools</div>
        <div class="rel-title">Informatica vs Talend: comparativa honesta 2025</div>
      </a>
    </div>
  </div>
</article>
"""

# ════════════════════════════════════════════
# ARTICULO 3: SQL Window Functions
# ════════════════════════════════════════════
art3_body = """
<div class="art-hero">
  <div class="art-hero-bg iz">
    <img src="https://images.unsplash.com/photo-1489875347316-0d6a16e79b7d?w=1400&auto=format&fit=crop&q=80" alt="C&oacute;digo SQL en pantalla">
  </div>
  <div class="art-hero-overlay">
    <div class="art-hero-inner">
      <nav class="art-crumb rv" aria-label="breadcrumb">
        <a href="../index.html">Inicio</a><span>/</span>
        <a href="../blog.html">Blog</a><span>/</span>
        <span>SQL</span>
      </nav>
      <span class="art-cat">SQL</span>
      <h1 class="art-title rv d1">SQL Window Functions: la gu&iacute;a definitiva con 20 ejemplos</h1>
      <div class="art-meta rv d2">
        <span>Por <strong>Antonio Moro</strong></span>
        <span>15 Feb 2025</span>
        <span>10 min lectura</span>
      </div>
    </div>
  </div>
</div>

<article class="art-body">
  <p class="art-lead rv">Las window functions son, probablemente, la caracter&iacute;stica SQL m&aacute;s infravalorada por analistas y Data Engineers junior. Permiten hacer c&aacute;lculos sobre un conjunto de filas relacionadas sin colapsar el resultado en un GROUP BY. Cuando las dominas, eliminas decenas de subconsultas y CTEs innecesarias de tu c&oacute;digo.</p>

  <h2 class="rv">Qu&eacute; es la cl&aacute;usula OVER</h2>
  <p>La cl&aacute;usula <code>OVER()</code> es lo que convierte una funci&oacute;n normal en una window function. Define la "ventana" de filas sobre la que opera la funci&oacute;n para cada fila del resultado.</p>
<pre><code>SELECT
    columna1,
    columna2,
    funcion() OVER (
        PARTITION BY columna_particion
        ORDER BY columna_orden
        ROWS BETWEEN inicio AND fin
    ) AS resultado
FROM tabla;</code></pre>
  <ul>
    <li><strong>PARTITION BY:</strong> divide las filas en grupos (como un GROUP BY, pero sin colapsar filas)</li>
    <li><strong>ORDER BY:</strong> define el orden dentro de cada partici&oacute;n</li>
    <li><strong>ROWS/RANGE BETWEEN:</strong> define el marco de filas para funciones de agregaci&oacute;n</li>
  </ul>

  <h2 class="rv">Funciones de Ranking</h2>

  <h3>ROW_NUMBER &mdash; n&uacute;mero &uacute;nico por fila</h3>
<pre><code>-- Ejemplo 1: numerar pedidos por cliente segun fecha
SELECT
    cliente_id,
    pedido_id,
    fecha_pedido,
    ROW_NUMBER() OVER (
        PARTITION BY cliente_id
        ORDER BY fecha_pedido
    ) AS num_pedido
FROM pedidos;

-- Ejemplo 2: obtener solo el primer pedido de cada cliente
WITH pedidos_numerados AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY fecha_pedido) AS rn
    FROM pedidos
)
SELECT * FROM pedidos_numerados WHERE rn = 1;</code></pre>

  <h3>RANK y DENSE_RANK &mdash; ranking con empates</h3>
<pre><code>-- Ejemplo 3: ranking de ventas por region
-- RANK salta numeros en empates (1,2,2,4), DENSE_RANK no (1,2,2,3)
SELECT
    region,
    vendedor,
    total_ventas,
    RANK()       OVER (PARTITION BY region ORDER BY total_ventas DESC) AS rank_con_salto,
    DENSE_RANK() OVER (PARTITION BY region ORDER BY total_ventas DESC) AS rank_denso
FROM resumen_ventas;

-- Ejemplo 4: top 3 productos por categoria
WITH ranking AS (
    SELECT
        categoria,
        producto,
        ventas,
        DENSE_RANK() OVER (PARTITION BY categoria ORDER BY ventas DESC) AS dr
    FROM ventas_producto
)
SELECT * FROM ranking WHERE dr &lt;= 3;</code></pre>

  <h3>NTILE &mdash; dividir en cuartiles o percentiles</h3>
<pre><code>-- Ejemplo 5: segmentar clientes en cuartiles de gasto
SELECT
    cliente_id,
    gasto_anual,
    NTILE(4) OVER (ORDER BY gasto_anual DESC) AS cuartil
    -- cuartil 1 = top 25% de gasto
FROM clientes;

-- Ejemplo 6: deciles de precio de productos
SELECT
    producto_id,
    precio,
    NTILE(10) OVER (ORDER BY precio) AS decil_precio
FROM productos;</code></pre>

  <h2 class="rv">Funciones de Desplazamiento</h2>

  <h3>LAG y LEAD &mdash; acceder a filas anteriores o siguientes</h3>
<pre><code>-- Ejemplo 7: variacion de ventas mes a mes
SELECT
    mes,
    ventas,
    LAG(ventas, 1, 0) OVER (ORDER BY mes) AS ventas_mes_anterior,
    ventas - LAG(ventas, 1, 0) OVER (ORDER BY mes) AS variacion_absoluta,
    ROUND(100.0 * (ventas - LAG(ventas,1) OVER (ORDER BY mes))
          / NULLIF(LAG(ventas,1) OVER (ORDER BY mes), 0), 2) AS variacion_pct
FROM ventas_mensuales;

-- Ejemplo 8: tiempo entre compras de un cliente
SELECT
    cliente_id,
    fecha_compra,
    LAG(fecha_compra) OVER (PARTITION BY cliente_id ORDER BY fecha_compra) AS compra_anterior,
    DATE_DIFF(fecha_compra,
              LAG(fecha_compra) OVER (PARTITION BY cliente_id ORDER BY fecha_compra),
              DAY) AS dias_entre_compras
FROM pedidos;</code></pre>

<pre><code>-- Ejemplo 9: ver el siguiente evento de un usuario (BigQuery)
SELECT
    usuario_id,
    evento,
    timestamp,
    LEAD(evento, 1) OVER (PARTITION BY usuario_id ORDER BY timestamp) AS siguiente_evento,
    LEAD(timestamp, 1) OVER (PARTITION BY usuario_id ORDER BY timestamp) AS ts_siguiente
FROM eventos_sesion;</code></pre>

  <h3>FIRST_VALUE y LAST_VALUE</h3>
<pre><code>-- Ejemplo 10: precio de la primera compra de cada cliente
SELECT
    cliente_id,
    fecha_compra,
    importe,
    FIRST_VALUE(importe) OVER (
        PARTITION BY cliente_id
        ORDER BY fecha_compra
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS importe_primera_compra

-- Ejemplo 11: maximo de los ultimos 3 meses (LAST_VALUE con marco)
SELECT
    fecha,
    ventas,
    LAST_VALUE(ventas) OVER (
        ORDER BY fecha
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS ventas_ultimo_en_ventana
FROM ventas_diarias;</code></pre>

  <h2 class="rv">Funciones de Agregaci&oacute;n como Ventana</h2>
<pre><code>-- Ejemplo 12: total acumulado de ventas (running total)
SELECT
    fecha,
    ventas_dia,
    SUM(ventas_dia) OVER (ORDER BY fecha ROWS UNBOUNDED PRECEDING) AS ventas_acumuladas
FROM ventas_diarias;

-- Ejemplo 13: porcentaje sobre el total de la particion
SELECT
    region,
    vendedor,
    ventas,
    SUM(ventas) OVER (PARTITION BY region) AS total_region,
    ROUND(100.0 * ventas / SUM(ventas) OVER (PARTITION BY region), 2) AS pct_region
FROM ventas;

-- Ejemplo 14: media movil de 7 dias
SELECT
    fecha,
    ventas,
    AVG(ventas) OVER (
        ORDER BY fecha
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS media_movil_7d
FROM ventas_diarias;

-- Ejemplo 15: count acumulado de nuevos clientes por mes
SELECT
    mes_alta,
    nuevos_clientes,
    COUNT(*) OVER (ORDER BY mes_alta ROWS UNBOUNDED PRECEDING) AS total_acumulado
FROM resumen_clientes;</code></pre>

  <h2 class="rv">ROWS BETWEEN y RANGE BETWEEN</h2>
  <p>Estas cl&aacute;usulas definen el marco de filas para funciones de agregaci&oacute;n. La diferencia entre ROWS y RANGE es sutil pero importante:</p>
  <ul>
    <li><strong>ROWS:</strong> basado en posici&oacute;n f&iacute;sica de filas (m&aacute;s predecible)</li>
    <li><strong>RANGE:</strong> basado en valor l&oacute;gico (puede incluir empates)</li>
  </ul>
<pre><code>-- Ejemplo 16: suma de los ultimos 3 dias (incluyendo hoy)
SUM(ventas) OVER (ORDER BY fecha ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)

-- Ejemplo 17: total desde el inicio del periodo hasta el final
SUM(ventas) OVER (ORDER BY fecha ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)

-- Ejemplo 18: maximo en ventana de 5 filas centrada en la fila actual
MAX(precio) OVER (ORDER BY fecha ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING)

-- Ejemplo 19: suma de todos los valores iguales o menores (RANGE)
SUM(importe) OVER (ORDER BY importe RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)

-- Ejemplo 20: diferencia respecto al inicio del anyo (YTD vs total)
SELECT
    fecha,
    ventas,
    SUM(ventas) OVER (PARTITION BY EXTRACT(YEAR FROM fecha)
                      ORDER BY fecha
                      ROWS UNBOUNDED PRECEDING) AS ventas_ytd,
    SUM(ventas) OVER (PARTITION BY EXTRACT(YEAR FROM fecha)) AS ventas_anyo_completo
FROM ventas_diarias;</code></pre>

  <h2 class="rv">Compatibilidad entre plataformas</h2>
  <table class="art-table">
    <thead>
      <tr><th>Funci&oacute;n</th><th>BigQuery</th><th>Snowflake</th><th>PostgreSQL</th><th>SQL Server</th></tr>
    </thead>
    <tbody>
      <tr><td>ROW_NUMBER</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
      <tr><td>RANK / DENSE_RANK</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
      <tr><td>NTILE</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
      <tr><td>LAG / LEAD</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
      <tr><td>FIRST_VALUE / LAST_VALUE</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
      <tr><td>SUM/AVG/COUNT OVER</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
      <tr><td>ROWS BETWEEN</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
      <tr><td>RANGE BETWEEN</td><td>&#10003;</td><td>Parcial</td><td>&#10003;</td><td>&#10003;</td></tr>
    </tbody>
  </table>

  <div class="art-tip">
    <strong>Tip de rendimiento</strong>
    <p>En BigQuery y Snowflake, las window functions sobre tablas grandes pueden ser costosas. Aseg&uacute;rate de filtrar antes con un CTE o subconsulta. Evita m&uacute;ltiples window functions con el mismo OVER() en columnas separadas: BigQuery puede optimizarlas si las escribes en la misma subquery.</p>
  </div>

  <hr class="art-divider">
  <div class="art-cta rv">
    <h3>SQL Cheatsheet con todas las window functions y funciones anal&iacute;ticas</h3>
    <p>Referencia r&aacute;pida en PDF con sintaxis, ejemplos y compatibilidad de m&aacute;s de 40 funciones SQL para BigQuery, Snowflake y PostgreSQL. Ideal para tener siempre a mano.</p>
    <a href="../productos.html" class="btn-white">Ver recursos &rarr;</a>
  </div>
  <div class="art-related rv">
    <h4>Tambi&eacute;n te puede interesar</h4>
    <div class="rel-grid">
      <a href="etl-vs-elt-2025.html" class="rel-card">
        <div class="rel-cat">ETL</div>
        <div class="rel-title">ETL vs ELT en 2025: &iquest;cu&aacute;l domina el mercado cloud?</div>
      </a>
      <a href="dbt-data-warehouse-2025.html" class="rel-card">
        <div class="rel-cat">Cloud</div>
        <div class="rel-title">dbt en 2025: el est&aacute;ndar del Data Warehouse moderno</div>
      </a>
    </div>
  </div>
</article>
"""

# ════════════════════════════════════════════
# ARTICULO 4: dbt en 2025
# ════════════════════════════════════════════
art4_body = """
<div class="art-hero">
  <div class="art-hero-bg iz">
    <img src="https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=1400&auto=format&fit=crop&q=80" alt="Arquitectura de datos cloud">
  </div>
  <div class="art-hero-overlay">
    <div class="art-hero-inner">
      <nav class="art-crumb rv" aria-label="breadcrumb">
        <a href="../index.html">Inicio</a><span>/</span>
        <a href="../blog.html">Blog</a><span>/</span>
        <span>Cloud</span>
      </nav>
      <span class="art-cat">Cloud</span>
      <h1 class="art-title rv d1">dbt en 2025: el est&aacute;ndar del Data Warehouse moderno</h1>
      <div class="art-meta rv d2">
        <span>Por <strong>Antonio Moro</strong></span>
        <span>1 Feb 2025</span>
        <span>9 min lectura</span>
      </div>
    </div>
  </div>
</div>

<article class="art-body">
  <p class="art-lead rv">En 2025, si construyes un Data Warehouse sin dbt, est&aacute;s eligiendo el camino dif&iacute;cil. dbt (data build tool) ha ganado el mercado de transformaciones ELT de forma aplastante. No porque sea perfecto, sino porque resuelve un problema real que cualquier equipo de datos ha sufrido: c&oacute;mo gestionar transformaciones SQL de forma profesional, versionada y probada.</p>

  <h2 class="rv">Por qu&eacute; dbt ha ganado el mercado</h2>
  <p>Antes de dbt, el flujo t&iacute;pico era: un analista escrib&iacute;a SQL en un editor, lo pegaba en el DWH, y nadie sab&iacute;a de d&oacute;nde ven&iacute;an los datos ni qui&eacute;n los hab&iacute;a transformado. dbt cambi&oacute; esto introduciendo:</p>
  <ul>
    <li><strong>Modelos SQL versionados en Git:</strong> cada transformaci&oacute;n es un fichero .sql bajo control de versiones</li>
    <li><strong>Gesti&oacute;n autom&aacute;tica de dependencias:</strong> dbt calcula el orden correcto de ejecuci&oacute;n usando un DAG</li>
    <li><strong>Tests integrados:</strong> validaci&oacute;n de datos como parte del pipeline</li>
    <li><strong>Documentaci&oacute;n autom&aacute;tica:</strong> genera un portal web con el linaje de todos los modelos</li>
    <li><strong>Jinja templating:</strong> l&oacute;gica din&aacute;mica dentro del SQL sin cambiar de lenguaje</li>
  </ul>

  <div class="art-quote">
    <p>&ldquo;dbt les da a los ingenieros de datos las mejores pr&aacute;cticas de ingenier&iacute;a de software: tests, documentaci&oacute;n, modularidad y control de versiones. Todo aplicado a SQL.&rdquo;</p>
  </div>

  <h2 class="rv">dbt Core vs dbt Cloud</h2>
  <table class="art-table">
    <thead><tr><th>Caracter&iacute;stica</th><th>dbt Core</th><th>dbt Cloud</th></tr></thead>
    <tbody>
      <tr><td>Precio</td><td>Gratuito (open source)</td><td>Desde 50 USD/usuario/mes</td></tr>
      <tr><td>Interfaz</td><td>CLI &uacute;nicamente</td><td>IDE web + CLI</td></tr>
      <tr><td>Orquestaci&oacute;n</td><td>Manual / Airflow</td><td>Jobs gestionados</td></tr>
      <tr><td>Alertas y monitoreo</td><td>No incluido</td><td>Incluido</td></tr>
      <tr><td>CI/CD integrado</td><td>Requiere configuraci&oacute;n</td><td>Nativo (GitHub/GitLab)</td></tr>
      <tr><td>Mejor para</td><td>Equipos peque&ntilde;os, experimentaci&oacute;n</td><td>Equipos medianos/grandes</td></tr>
    </tbody>
  </table>

  <h2 class="rv">Arquitectura de un proyecto dbt</h2>
<pre><code>mi_proyecto_dbt/
|-- dbt_project.yml        # configuracion del proyecto
|-- profiles.yml           # conexion al DWH (fuera del repo)
|-- models/
|   |-- staging/           # fuentes en bruto, 1:1 con tablas origen
|   |   |-- stg_ventas.sql
|   |   |-- stg_clientes.sql
|   |   |-- _sources.yml   # definicion de fuentes
|   |-- intermediate/      # calculos intermedios, no expuestos
|   |   |-- int_ventas_enriquecidas.sql
|   |-- marts/             # tablas finales para BI
|   |   |-- ventas/
|   |   |   |-- fct_ventas.sql
|   |   |   |-- dim_cliente.sql
|   |   |   |-- _schema.yml  # tests y documentacion
|-- seeds/                 # CSVs estaticos (tablas de referencia)
|-- macros/                # funciones SQL reutilizables
|-- tests/                 # tests singulares (SQL custom)
|-- snapshots/             # SCD tipo 2 (historial de cambios)</code></pre>

  <h3>Ejemplo de modelo con Jinja</h3>
<pre><code>-- models/staging/stg_ventas.sql
{{ config(materialized='view') }}

WITH source AS (
    SELECT * FROM {{ source('raw', 'ventas') }}
),

renamed AS (
    SELECT
        CAST(id_venta AS STRING)       AS venta_id,
        CAST(id_cliente AS STRING)     AS cliente_id,
        CAST(id_producto AS STRING)    AS producto_id,
        DATE(fecha_venta)              AS fecha_venta,
        CAST(cantidad AS INT64)        AS cantidad,
        CAST(precio_unitario AS FLOAT64) AS precio_unitario,
        CAST(descuento AS FLOAT64)     AS descuento,
        cantidad * precio_unitario * (1 - descuento) AS importe_neto,
        _PARTITIONDATE                 AS fecha_carga
    FROM source
    WHERE fecha_venta IS NOT NULL
      AND cantidad &gt; 0
)

SELECT * FROM renamed</code></pre>

  <h3>Tests gen&eacute;ricos en schema.yml</h3>
<pre><code># models/marts/ventas/_schema.yml
version: 2

models:
  - name: fct_ventas
    description: "Tabla de hechos de ventas. Una fila por linea de pedido."
    columns:
      - name: venta_id
        description: "Identificador unico de la venta"
        tests:
          - unique
          - not_null
      - name: cliente_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_cliente')
              field: cliente_id
      - name: importe_neto
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0</code></pre>

  <h2 class="rv">Despliegue en GCP BigQuery (paso a paso)</h2>
<pre><code># 1. Instalar dbt con el adaptador de BigQuery
pip install dbt-bigquery

# 2. Configurar profiles.yml
# Ubicacion: ~/.dbt/profiles.yml
my_project:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: oauth
      project: mi-proyecto-gcp
      dataset: dbt_dev
      threads: 4
      timeout_seconds: 300
    prod:
      type: bigquery
      method: service-account
      project: mi-proyecto-gcp
      dataset: dbt_prod
      keyfile: /path/to/service-account.json
      threads: 8

# 3. Verificar conexion
dbt debug

# 4. Ejecutar todos los modelos
dbt run

# 5. Ejecutar tests
dbt test

# 6. Generar documentacion
dbt docs generate
dbt docs serve</code></pre>

  <h2 class="rv">Despliegue en Azure Synapse / Azure SQL</h2>
<pre><code># 1. Instalar adaptador de Synapse
pip install dbt-synapse

# 2. Configurar profiles.yml para Synapse
my_project:
  target: dev
  outputs:
    dev:
      type: synapse
      driver: 'ODBC Driver 18 for SQL Server'
      server: mi-workspace.sql.azuresynapse.net
      port: 1433
      database: mi_dedicated_pool
      schema: dbt_dev
      authentication: ServicePrincipal
      tenant_id: "xxxx-xxxx-xxxx"
      client_id: "xxxx-xxxx-xxxx"
      client_secret: "{{ env_var('DBT_AZURE_CLIENT_SECRET') }}"
      threads: 4

# 3. Variables de entorno para secretos
export DBT_AZURE_CLIENT_SECRET="tu_secreto_aqui"

# 4. Ejecutar solo modelos de staging
dbt run --select staging

# 5. Ejecutar con full-refresh (reconstruir desde cero)
dbt run --full-refresh</code></pre>

  <h2 class="rv">Integraci&oacute;n con Apache Airflow</h2>
<pre><code># DAG de Airflow para ejecutar dbt
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='dbt_daily_run',
    schedule_interval='0 6 * * *',
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['dbt', 'datawarehouse']
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/dbt/mi_proyecto && dbt run --target prod',
        env={'DBT_PROFILES_DIR': '/opt/dbt/profiles'}
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/dbt/mi_proyecto && dbt test --target prod'
    )

    dbt_run &gt;&gt; dbt_test</code></pre>

  <div class="art-tip">
    <strong>Buena pr&aacute;ctica</strong>
    <p>Usa el proveedor oficial <code>apache-airflow-providers-dbt-cloud</code> si usas dbt Cloud. Para dbt Core, el BashOperator es la opci&oacute;n m&aacute;s portable. El paquete <code>astronomer-cosmos</code> convierte cada modelo dbt en una tarea Airflow individual para mayor observabilidad.</p>
  </div>

  <hr class="art-divider">
  <div class="art-cta rv">
    <h3>dbt Starter Kit para BigQuery y Snowflake</h3>
    <p>Proyecto dbt completo con estructura de carpetas, modelos de staging y marts, tests gen&eacute;ricos preconfigurados, macros de utilidad y documentaci&oacute;n. Listo para arrancar en horas, no semanas.</p>
    <a href="../productos.html" class="btn-white">Ver recursos &rarr;</a>
  </div>
  <div class="art-related rv">
    <h4>Tambi&eacute;n te puede interesar</h4>
    <div class="rel-grid">
      <a href="etl-vs-elt-2025.html" class="rel-card">
        <div class="rel-cat">ETL</div>
        <div class="rel-title">ETL vs ELT en 2025: &iquest;cu&aacute;l domina el mercado cloud?</div>
      </a>
      <a href="kimball-vs-data-vault.html" class="rel-card">
        <div class="rel-cat">Cloud</div>
        <div class="rel-title">Kimball vs Data Vault 2.0: &iquest;qu&eacute; modelo DWH elegir?</div>
      </a>
    </div>
  </div>
</article>
"""

# ════════════════════════════════════════════
# ARTICULO 5: Kimball vs Data Vault
# ════════════════════════════════════════════
art5_body = """
<div class="art-hero">
  <div class="art-hero-bg iz">
    <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1400&auto=format&fit=crop&q=80" alt="Arquitectura de datos y Data Warehouse">
  </div>
  <div class="art-hero-overlay">
    <div class="art-hero-inner">
      <nav class="art-crumb rv" aria-label="breadcrumb">
        <a href="../index.html">Inicio</a><span>/</span>
        <a href="../blog.html">Blog</a><span>/</span>
        <span>Cloud</span>
      </nav>
      <span class="art-cat">Cloud</span>
      <h1 class="art-title rv d1">Kimball vs Data Vault 2.0: &iquest;qu&eacute; modelo DWH elegir?</h1>
      <div class="art-meta rv d2">
        <span>Por <strong>Antonio Moro</strong></span>
        <span>15 Ene 2025</span>
        <span>9 min lectura</span>
      </div>
    </div>
  </div>
</div>

<article class="art-body">
  <p class="art-lead rv">He implementado ambas metodolog&iacute;as en proyectos reales: Kimball en retailers y empresas de consumo, Data Vault en banca y telecomunicaciones. La pregunta no es cu&aacute;l es mejor en abstracto, sino cu&aacute;l es mejor <em>para tu contexto</em>. Esta gu&iacute;a te da los criterios para tomar esa decisi&oacute;n.</p>

  <h2 class="rv">Historia y filosof&iacute;a</h2>

  <h3>Kimball: dimensional modeling desde los 90</h3>
  <p>Ralph Kimball public&oacute; su metodolog&iacute;a en 1996 con el libro <em>The Data Warehouse Toolkit</em>. Su idea central es simple y poderosa: organizar los datos en torno a c&oacute;mo los usuarios de negocio los piensan. Las tablas de <strong>hechos</strong> contienen m&eacute;tricas num&eacute;ricas (ventas, transacciones, eventos) y las <strong>dimensiones</strong> contienen el contexto descriptivo (qui&eacute;n, qu&eacute;, cu&aacute;ndo, d&oacute;nde).</p>
<pre><code>-- Esquema estrella tipico de Kimball
            dim_fecha
               |
dim_cliente -- fct_ventas -- dim_producto
               |
            dim_vendedor

-- fct_ventas (tabla de hechos)
venta_id, fecha_id, cliente_id, producto_id, vendedor_id,
cantidad, precio_unitario, descuento, importe_neto

-- dim_cliente (dimension)
cliente_id, nombre, ciudad, segmento, canal_adquisicion,
fecha_alta, edad, genero</code></pre>

  <h3>Data Vault 2.0: auditabilidad enterprise</h3>
  <p>Dan Linstedt desarroll&oacute; Data Vault en los a&ntilde;os 90 para la Marina de EE.UU. La versi&oacute;n 2.0 (2013) lo adapt&oacute; al cloud y al Big Data. Su premisa: los datos de negocio son hist&oacute;ricamente correctos, auditables y nunca se borran. La arquitectura se basa en tres tipos de tabla:</p>
  <ul>
    <li><strong>Hubs:</strong> identifican entidades de negocio &uacute;nicas (CLIENTE, PRODUCTO, ORDEN). Solo contienen la clave de negocio y metadatos de carga.</li>
    <li><strong>Links:</strong> representan relaciones entre Hubs (CLIENTE compra PRODUCTO).</li>
    <li><strong>Satellites:</strong> almacenan los atributos descriptivos y sus cambios hist&oacute;ricos con timestamps.</li>
  </ul>
<pre><code>-- Hub de Cliente (Data Vault)
hub_cliente_id (PK), cliente_bk (business key), load_date, record_source

-- Satellite de Cliente (atributos + historial)
hub_cliente_id (FK), load_date, load_end_date, hash_diff,
nombre, ciudad, segmento, canal_adquisicion, record_source

-- Link entre Cliente y Producto
link_venta_id (PK), hub_cliente_id (FK), hub_producto_id (FK),
load_date, record_source</code></pre>

  <h2 class="rv">Comparativa detallada</h2>
  <table class="art-table">
    <thead><tr><th>Criterio</th><th>Kimball</th><th>Data Vault 2.0</th></tr></thead>
    <tbody>
      <tr><td><strong>Complejidad de implementaci&oacute;n</strong></td><td>Media &mdash; intuitivo para equipos peque&ntilde;os</td><td>Alta &mdash; requiere disciplina y automatizaci&oacute;n</td></tr>
      <tr><td><strong>Rendimiento para BI/reporting</strong></td><td>Excelente &mdash; star schema optimizado para queries anal&iacute;ticas</td><td>Requiere capa de presentaci&oacute;n (Business Vault o Information Mart)</td></tr>
      <tr><td><strong>Flexibilidad ante cambios</strong></td><td>Limitada &mdash; a&ntilde;adir una nueva fuente puede romper el modelo</td><td>Alta &mdash; nuevas fuentes se integran sin romper lo existente</td></tr>
      <tr><td><strong>Auditabilidad hist&oacute;rica</strong></td><td>Parcial &mdash; requiere SCD tipo 2 en dimensiones</td><td>Total &mdash; toda la historia queda en Satellites por dise&ntilde;o</td></tr>
      <tr><td><strong>Curva de aprendizaje</strong></td><td>Baja &mdash; cualquier analista SQL entiende star schema</td><td>Alta &mdash; requiere formaci&oacute;n espec&iacute;fica</td></tr>
      <tr><td><strong>Tiempo de implementaci&oacute;n inicial</strong></td><td>R&aacute;pido (semanas)</td><td>Lento (meses para proyectos grandes)</td></tr>
      <tr><td><strong>Escalabilidad</strong></td><td>Buena, pero el dise&ntilde;o puede engordar con m&uacute;ltiples fuentes</td><td>Excelente &mdash; dise&ntilde;ado para escalar con m&uacute;ltiples sistemas fuente</td></tr>
      <tr><td><strong>Coste de mantenimiento</strong></td><td>Bajo si el negocio no cambia mucho</td><td>Bajo a largo plazo gracias a la modularidad</td></tr>
    </tbody>
  </table>

  <h2 class="rv">Cu&aacute;ndo usar Kimball</h2>
  <p>Kimball es la elecci&oacute;n correcta cuando:</p>
  <ul>
    <li>El equipo es peque&ntilde;o o mediano (2-8 personas de datos)</li>
    <li>Los usuarios de negocio necesitan acceso directo al modelo (self-service BI)</li>
    <li>Las fuentes de datos son estables y no cambian frecuentemente</li>
    <li>El tiempo de entrega es cr&iacute;tico (hay que tener resultados en semanas)</li>
    <li>El DWH sirve principalmente para reporting y dashboards</li>
    <li>No hay requisitos regulatorios fuertes de auditabilidad</li>
  </ul>

  <div class="art-tip">
    <strong>Caso de uso ideal para Kimball</strong>
    <p>Un retailer de tama&ntilde;o mediano que quiere analizar ventas, clientes y producto. Los datos vienen de un solo ERP y un sistema de e-commerce. El equipo tiene 3 personas de datos y el CEO quiere dashboards en Power BI en 6 semanas.</p>
  </div>

  <h2 class="rv">Cu&aacute;ndo usar Data Vault 2.0</h2>
  <p>Data Vault 2.0 brilla en escenarios enterprise:</p>
  <ul>
    <li>M&uacute;ltiples sistemas fuente que comparten entidades de negocio (10+ fuentes)</li>
    <li>Industrias reguladas: banca, seguros, telecomunicaciones, sanidad</li>
    <li>Requisitos de auditor&iacute;a: necesidad de saber exactamente qu&eacute; dato lleg&oacute; cu&aacute;ndo y de d&oacute;nde</li>
    <li>Equipos grandes con varios subequipos trabajando en paralelo</li>
    <li>Los requisitos de negocio cambian frecuentemente (nuevas fuentes, nuevos atributos)</li>
    <li>El DWH es la "fuente &uacute;nica de la verdad" para toda la organizaci&oacute;n</li>
  </ul>

  <h2 class="rv">El enfoque h&iacute;brido: Business Vault</h2>
  <p>En proyectos enterprise modernos, la arquitectura m&aacute;s adoptada combina lo mejor de ambos mundos:</p>
  <ul>
    <li><strong>Raw Vault:</strong> ingesta fiel de los datos fuente en estructura Data Vault (Hubs, Links, Satellites). Sin transformaciones de negocio. M&aacute;xima auditabilidad.</li>
    <li><strong>Business Vault:</strong> capa intermedia sobre el Raw Vault donde se aplican reglas de negocio, c&aacute;lculos derivados y se resuelven conflictos entre fuentes.</li>
    <li><strong>Information Mart:</strong> capa de presentaci&oacute;n en star schema Kimball, optimizada para las herramientas de BI (Power BI, Tableau, Looker).</li>
  </ul>

  <div class="art-quote">
    <p>&ldquo;Data Vault sin una capa de presentaci&oacute;n en star schema es como tener el mejor almac&eacute;n del mundo al que nadie puede entrar. El Business Vault es la llave.&rdquo;</p>
  </div>

  <h2 class="rv">Experiencias reales</h2>
  <p>En un proyecto de banca para una entidad con 8 sistemas fuente (core bancario, tarjetas, hipotecas, seguros, inversiones, banca online, TPV y datos de mercado), impl&eacute;ment&eacute; Data Vault 2.0. La decisi&oacute;n fue correcta: 18 meses despu&eacute;s, se a&ntilde;adieron 3 nuevas fuentes sin tocar ninguna tabla existente. El auditor interno pod&iacute;a rastrear cualquier dato hasta su origen con fecha y hora exactas.</p>
  <p>En contraste, para una cadena de restaurantes con datos de un solo POS y un sistema de fidelizaci&oacute;n, usamos Kimball puro. El equipo de 4 personas ten&iacute;a dashboards funcionando en 3 semanas. Data Vault habr&iacute;a sido un exceso brutal de ingenier&iacute;a para ese contexto.</p>

  <hr class="art-divider">
  <div class="art-cta rv">
    <h3>Plantilla de arquitectura DWH lista para empezar</h3>
    <p>Documentaci&oacute;n de arquitectura, diagramas de modelo de datos, y scripts SQL de creaci&oacute;n de tablas para proyectos Kimball y Data Vault en BigQuery y Snowflake.</p>
    <a href="../productos.html" class="btn-white">Ver recursos &rarr;</a>
  </div>
  <div class="art-related rv">
    <h4>Tambi&eacute;n te puede interesar</h4>
    <div class="rel-grid">
      <a href="dbt-data-warehouse-2025.html" class="rel-card">
        <div class="rel-cat">Cloud</div>
        <div class="rel-title">dbt en 2025: el est&aacute;ndar del Data Warehouse moderno</div>
      </a>
      <a href="etl-vs-elt-2025.html" class="rel-card">
        <div class="rel-cat">ETL</div>
        <div class="rel-title">ETL vs ELT en 2025: &iquest;cu&aacute;l domina el mercado cloud?</div>
      </a>
    </div>
  </div>
</article>
"""

# ════════════════════════════════════════════
# ARTICULO 6: Informatica vs Talend
# ════════════════════════════════════════════
art6_body = """
<div class="art-hero">
  <div class="art-hero-bg iz">
    <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1400&auto=format&fit=crop&q=80" alt="Herramientas de desarrollo de datos">
  </div>
  <div class="art-hero-overlay">
    <div class="art-hero-inner">
      <nav class="art-crumb rv" aria-label="breadcrumb">
        <a href="../index.html">Inicio</a><span>/</span>
        <a href="../blog.html">Blog</a><span>/</span>
        <span>Tools</span>
      </nav>
      <span class="art-cat">Tools</span>
      <h1 class="art-title rv d1">Informatica vs Talend: comparativa honesta 2025</h1>
      <div class="art-meta rv d2">
        <span>Por <strong>Antonio Moro</strong></span>
        <span>5 Ene 2025</span>
        <span>7 min lectura</span>
      </div>
    </div>
  </div>
</div>

<article class="art-body">
  <p class="art-lead rv">He trabajado con Informatica PowerCenter desde la versi&oacute;n 8.x y con Talend desde su versi&oacute;n 5 Open Studio. He implementado ambas herramientas en proyectos enterprise reales: banca, seguros, telecomunicaciones, retail. Esta comparativa no es te&oacute;rica &mdash;es la experiencia acumulada de cientos de pipelines en producci&oacute;n.</p>

  <h2 class="rv">Informatica PowerCenter / IDMC</h2>
  <p>Informatica lleva m&aacute;s de 30 a&ntilde;os en el mercado y es la herramienta ETL m&aacute;s usada en entornos enterprise de alta exigencia. Su producto principal era <strong>PowerCenter</strong> (on-premise), y su apuesta actual es <strong>IDMC</strong> (Informatica Data Management Cloud), una plataforma cloud unificada que incluye integraci&oacute;n de datos, calidad, gobierno y API management.</p>

  <h3>Puntos fuertes de Informatica</h3>
  <ul>
    <li><strong>Madurez y estabilidad:</strong> PowerCenter est&aacute; en producci&oacute;n en los bancos m&aacute;s grandes del mundo. Ha procesado billones de registros. Su fiabilidad es fuera de serie.</li>
    <li><strong>Soporte enterprise 24/7:</strong> cuando tienes un problema en producci&oacute;n a las 3 de la ma&ntilde;ana, Informatica tiene ingenieros esperando. Esto vale mucho en sectores cr&iacute;ticos.</li>
    <li><strong>Calidad de dato integrada:</strong> Informatica Data Quality (IDQ) es uno de los mejores motores de calidad del mercado. Reglas de validaci&oacute;n, estandarizaci&oacute;n, deduplicaci&oacute;n y enriquecimiento en el mismo ecosistema.</li>
    <li><strong>Conectores certificados:</strong> m&aacute;s de 500 conectores certificados para SAP, Salesforce, Oracle, mainframes, sistemas financieros legados. Si existe el sistema, probablemente hay conector.</li>
    <li><strong>CLAIRE AI:</strong> la capa de inteligencia artificial de IDMC que sugiere mapeos, detecta anomal&iacute;as y automatiza tareas de gobierno.</li>
  </ul>

  <h3>Puntos d&eacute;biles</h3>
  <ul>
    <li><strong>Precio prohibitivo:</strong> una instalaci&oacute;n enterprise de PowerCenter puede costar entre 150.000 y 500.000 EUR/a&ntilde;o entre licencias, soporte y mantenimiento. IDMC usa modelo de consumo pero sigue siendo caro.</li>
    <li><strong>Rigidez del entorno:</strong> el desarrollo en PowerCenter tiene una curva de aprendizaje alta y el entorno de desarrollo no ha evolucionado tanto como deber&iacute;a.</li>
    <li><strong>Migraci&oacute;n a IDMC costosa:</strong> pasar de PowerCenter a IDMC no es trivial. Los workflows, sesiones y mappings requieren redise&ntilde;o.</li>
  </ul>

  <h2 class="rv">Talend Data Integration / Talend Cloud</h2>
  <p>Talend naci&oacute; en 2006 como alternativa open source a Informatica. Su modelo: una edici&oacute;n gratuita (Open Studio) y versiones enterprise con m&aacute;s funcionalidades y soporte. En 2023 fue adquirido por Qlik (a su vez parte de Thoma Bravo), lo que ha generado incertidumbre sobre su roadmap independiente.</p>

  <h3>Puntos fuertes de Talend</h3>
  <ul>
    <li><strong>Precio/valor:</strong> Talend Enterprise cuesta entre 3 y 10 veces menos que Informatica. Para empresas medianas o proyectos con presupuesto limitado, es una diferencia determinante.</li>
    <li><strong>Open Studio gratuito:</strong> permite aprender la herramienta, hacer proyectos piloto o incluso proyectos peque&ntilde;os en producci&oacute;n sin coste de licencia.</li>
    <li><strong>Generaci&oacute;n de c&oacute;digo Java:</strong> los jobs de Talend compilan a c&oacute;digo Java ejecutable. Esto permite depurar el c&oacute;digo generado, integrarlo en pipelines de CI/CD y ejecutarlo sin la interfaz de Talend.</li>
    <li><strong>Buena integraci&oacute;n con Big Data:</strong> Talend tiene componentes nativos para Spark, Hadoop, Kafka y servicios cloud. Para proyectos de Big Data, su ecosistema es s&oacute;lido.</li>
    <li><strong>Calidad de dato:</strong> Talend Data Quality (integrado en la suite enterprise) ofrece perfilado, validaci&oacute;n y limpieza de datos con una interfaz visual accesible.</li>
  </ul>

  <h3>Puntos d&eacute;biles</h3>
  <ul>
    <li><strong>Incertidumbre post-Qlik:</strong> la integraci&oacute;n con Qlik Analytics y el futuro del roadmap de Talend como producto independiente genera dudas en proyectos de larga duraci&oacute;n.</li>
    <li><strong>Complejidad del c&oacute;digo generado:</strong> depurar un job grande de Talend que ha generado 10.000 l&iacute;neas de Java puede ser una pesadilla.</li>
    <li><strong>Soporte menos r&aacute;pido:</strong> en comparaci&oacute;n con Informatica, el soporte enterprise de Talend es menos &aacute;gil en incidentes cr&iacute;ticos.</li>
  </ul>

  <h2 class="rv">Comparativa directa</h2>
  <table class="art-table">
    <thead><tr><th>Criterio</th><th>Informatica IDMC</th><th>Talend Cloud</th></tr></thead>
    <tbody>
      <tr><td><strong>Rendimiento en vol&uacute;menes altos</strong></td><td>Excelente (optimizado para terabytes)</td><td>Bueno (mejora con Spark)</td></tr>
      <tr><td><strong>Precio anual (referencia)</strong></td><td>100.000&ndash;500.000 EUR</td><td>20.000&ndash;80.000 EUR</td></tr>
      <tr><td><strong>Soporte enterprise</strong></td><td>24/7, SLA garantizado</td><td>Horario comercial (enterprise)</td></tr>
      <tr><td><strong>N&uacute;mero de conectores</strong></td><td>500+ certificados</td><td>900+ (muchos open source)</td></tr>
      <tr><td><strong>Curva de aprendizaje</strong></td><td>Alta (6-12 meses para producir)</td><td>Media (3-6 meses)</td></tr>
      <tr><td><strong>Cloud native</strong></td><td>S&iacute; (IDMC)</td><td>S&iacute; (Talend Cloud / Stitch)</td></tr>
      <tr><td><strong>Comunidad</strong></td><td>Grande y especializada</td><td>Grande (open source activo)</td></tr>
      <tr><td><strong>Calidad de dato integrada</strong></td><td>IDQ &mdash; top del mercado</td><td>TDQ &mdash; competente</td></tr>
    </tbody>
  </table>

  <h2 class="rv">Alternativas modernas que no puedes ignorar</h2>
  <p>En 2025 no podemos hablar de ETL sin mencionar las alternativas cloud-native que est&aacute;n ganando terreno:</p>
  <ul>
    <li><strong>Fivetran:</strong> para la fase de ingesta (Extract + Load), Fivetran es el l&iacute;der indiscutible. Conectores mantenidos autom&aacute;ticamente, sin infraestructura que gestionar. Caro a gran escala pero imbatible en time-to-value.</li>
    <li><strong>Airbyte:</strong> la alternativa open source a Fivetran. Self-hosted o en cloud. Ideal para equipos que quieren control y no quieren vendor lock-in en la ingesta.</li>
    <li><strong>Azure Data Factory:</strong> si tu stack es Azure, ADF es la elecci&oacute;n natural. Visual, integrado con Synapse, Logic Apps y el ecosistema Microsoft. No alcanza la potencia de Informatica, pero para proyectos Azure-first es suficiente.</li>
    <li><strong>AWS Glue:</strong> similar a ADF pero en el ecosistema AWS. Basado en Apache Spark, buen precio/valor para proyectos en AWS.</li>
  </ul>

  <div class="art-warn">
    <strong>Cuidado con el lock-in</strong>
    <p>Tanto Informatica como Talend generan dependencia en sus formatos propietarios de mappings/jobs. Antes de comprometerte con cualquiera de las dos, evalu&uacute;a el coste de migraci&oacute;n futura. En proyectos nuevos, considera seriamente una arquitectura ELT con dbt que es mucho m&aacute;s portable.</p>
  </div>

  <h2 class="rv">Mi recomendaci&oacute;n seg&uacute;n perfil</h2>
  <ul>
    <li><strong>Banco o aseguradora grande con PowerCenter existente:</strong> mantener y migrar progresivamente a IDMC. No cambiar de vendor hasta tener una estrategia clara de salida.</li>
    <li><strong>Empresa mediana en cloud Azure:</strong> Azure Data Factory + dbt. Sin licencias, escalable, y el equipo lo aprende en semanas.</li>
    <li><strong>Empresa mediana en GCP o AWS:</strong> Airbyte (ingesta) + dbt (transformaci&oacute;n). Stack moderno, open source, sin vendor lock-in.</li>
    <li><strong>Empresa que busca alternativa a Informatica sin subirse al cloud:</strong> Talend Enterprise on-premise sigue siendo una opci&oacute;n v&aacute;lida y significativamente m&aacute;s barata.</li>
    <li><strong>Proyecto nuevo con equipo moderno:</strong> evita Informatica y Talend salvo que haya una raz&oacute;n muy espec&iacute;fica. El stack ELT moderno es m&aacute;s &aacute;gil, m&aacute;s barato y m&aacute;s f&aacute;cil de contratar.</li>
  </ul>

  <div class="art-quote">
    <p>&ldquo;Informatica es el mejor coche de gama alta del mercado. Si tu empresa puede permitirse el precio y el equipo, es imbatible. Si no, hay coches muy buenos por mucho menos dinero.&rdquo;</p>
  </div>

  <hr class="art-divider">
  <div class="art-cta rv">
    <h3>Plantillas de pipelines ETL documentadas para producci&oacute;n</h3>
    <p>Coleci&oacute;n de pipelines ETL documentados, patrones de dise&ntilde;o para integraci&oacute;n de datos y gu&iacute;as de migraci&oacute;n de herramientas legacy a stacks modernos. Basado en proyectos reales.</p>
    <a href="../productos.html" class="btn-white">Ver recursos &rarr;</a>
  </div>
  <div class="art-related rv">
    <h4>Tambi&eacute;n te puede interesar</h4>
    <div class="rel-grid">
      <a href="etl-vs-elt-2025.html" class="rel-card">
        <div class="rel-cat">ETL</div>
        <div class="rel-title">ETL vs ELT en 2025: &iquest;cu&aacute;l domina el mercado cloud?</div>
      </a>
      <a href="dbt-data-warehouse-2025.html" class="rel-card">
        <div class="rel-cat">Cloud</div>
        <div class="rel-title">dbt en 2025: el est&aacute;ndar del Data Warehouse moderno</div>
      </a>
    </div>
  </div>
</article>
"""

# ─────────────────────────────────────────────
# ESCRIBIR ARCHIVOS
# ─────────────────────────────────────────────
articles = [
    ("etl-vs-elt-2025.html",
     "ETL vs ELT en 2025: &iquest;cu&aacute;l domina el mercado cloud?",
     "ETL vs ELT en 2025: analisis tecnico completo. Por que el cloud ha cambiado el paradigma, comparativa de herramientas y cuando usar cada enfoque.",
     art1_body),
    ("dax-funciones-top10.html",
     "TOP 10 funciones DAX que todo analista BI debe dominar",
     "Las 10 funciones DAX imprescindibles en Power BI con ejemplos reales de produccion. CALCULATE, FILTER, ALL, SUMX, RANKX, DIVIDE, DATEADD y mas.",
     art2_body),
    ("sql-window-functions.html",
     "SQL Window Functions: la gu&iacute;a definitiva con 20 ejemplos",
     "Guia completa de SQL window functions compatible con BigQuery, Snowflake y PostgreSQL. ROW_NUMBER, RANK, LAG, LEAD, SUM OVER y 20 ejemplos reales.",
     art3_body),
    ("dbt-data-warehouse-2025.html",
     "dbt en 2025: el est&aacute;ndar del Data Warehouse moderno",
     "Por que dbt ha ganado el mercado ELT. Guia completa: dbt Core vs Cloud, arquitectura, modelos con Jinja, despliegue en BigQuery y Azure, integracion con Airflow.",
     art4_body),
    ("kimball-vs-data-vault.html",
     "Kimball vs Data Vault 2.0: &iquest;qu&eacute; modelo DWH elegir?",
     "Comparativa detallada Kimball vs Data Vault 2.0 con 8 criterios. Experiencias reales de proyectos enterprise. Cuando usar cada metodologia y el enfoque hibrido.",
     art5_body),
    ("informatica-vs-talend-2025.html",
     "Informatica vs Talend: comparativa honesta 2025",
     "Comparativa de Informatica PowerCenter/IDMC vs Talend tras 20 anyos usando ambas en proyectos enterprise. Precio, rendimiento, soporte y cuando migrar.",
     art6_body),
]

for filename, title, desc, body in articles:
    filepath = os.path.join(BLOG_DIR, filename)
    html = page(title, desc, body)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] {filename}")

# ─────────────────────────────────────────────
# ACTUALIZAR blog.html
# ─────────────────────────────────────────────
blog_html_path = os.path.join(BASE_DIR, "blog.html")
with open(blog_html_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

blog_links = [
    ('ETL', 'blog/etl-vs-elt-2025.html'),
    ('DAX', 'blog/dax-funciones-top10.html'),
    ('SQL', 'blog/sql-window-functions.html'),
    ('Cloud', 'blog/dbt-data-warehouse-2025.html'),
    ('Cloud', 'blog/kimball-vs-data-vault.html'),
    ('Tools', 'blog/informatica-vs-talend-2025.html'),
]

# Replace href="#" in blog cards one by one in order
import re
count = 0
def replace_nth_href(content, n, new_href):
    pattern = r'(<a\s+href="#"\s+class="bc-read">)'
    occurrences = [m.start() for m in re.finditer(pattern, content)]
    if n < len(occurrences):
        pos = occurrences[n]
        match = re.search(pattern, content[pos:])
        old = match.group(0)
        new = old.replace('href="#"', f'href="{new_href}"')
        return content[:pos] + new + content[pos+len(old):]
    return content

for i, (cat, href) in enumerate(blog_links):
    blog_content = replace_nth_href(blog_content, 0, href)

with open(blog_html_path, "w", encoding="utf-8") as f:
    f.write(blog_content)
print("[OK] blog.html actualizado")

# ─────────────────────────────────────────────
# ACTUALIZAR index.html (3 articulos del home)
# ─────────────────────────────────────────────
index_html_path = os.path.join(BASE_DIR, "index.html")
with open(index_html_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace the 3 home blog card links (href="blog.html" on .bc elements)
index_replacements = [
    ('ETL / ELT', 'blog/etl-vs-elt-2025.html'),
    ('Power BI', 'blog/dax-funciones-top10.html'),
    ('SQL', 'blog/sql-window-functions.html'),
]

# Find and replace the .bc anchor tags that wrap each article card
bc_pattern = r'(<a href="blog\.html" class="bc[^"]*")'
bc_matches = list(re.finditer(bc_pattern, index_content))
# Replace only the first 3 .bc links (the article cards, not "Ver todos")
offset = 0
for i, (cat, href) in enumerate(index_replacements):
    m = bc_matches[i]
    old = m.group(0)
    new = old.replace('href="blog.html"', f'href="{href}"')
    start = m.start() + offset
    end = m.end() + offset
    index_content = index_content[:start] + new + index_content[end:]
    offset += len(new) - len(old)

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(index_content)
print("[OK] index.html actualizado")

print()
print("=" * 50)
print("COMPLETADO: 6 articulos de blog creados y")
print("blog.html + index.html actualizados.")
print("=" * 50)
