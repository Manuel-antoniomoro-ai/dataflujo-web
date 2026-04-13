const AM = {
  // ── IDENTIDAD ──────────────────────────────────────────────────────
  nombre:    "Antonio Moro",
  titulo:    "Senior Data Engineer & BI Architect",
  subtitulo: "20+ años construyendo soluciones de datos en producción",
  email:     "a.morodiaz@hotmail.com",
  linkedin:  "https://linkedin.com/in/antonio-moro-diaz-62346213b",
  github:    "https://github.com/antonio-moro",
  ubicacion: "Madrid, España · Remote OK",
  respuesta: "Menos de 48h",

  // ── STATS ──────────────────────────────────────────────────────────
  años:        "20+",
  proyectos:   "200+",
  recursos:    27,
  tecnologias: "12+",

  // ── GUMROAD ────────────────────────────────────────────────────────
  gumroadBase: "https://gumroad.com/",

  // ── PRECIOS DE RECURSOS DIGITALES ──────────────────────────────────
  // ▸ Cambia aquí los precios sin tocar ningún HTML.
  // ▸ precio: null  →  muestra "Consultar precio"
  // ▸ precio: 0     →  muestra "Gratis"
  // ▸ mostrarPrecios: false  →  oculta TODOS los precios del catálogo
  mostrarPrecios: true,
  precios: {
    // — Power BI —
    "Dashboard Kit — Finanzas":              { precio: 29,  orig: 89 },
    "Dashboard Kit — Operaciones":           { precio: 19  },
    "Dashboard — Contabilidad":              { precio: 19  },
    "Power BI Starter Guide":                { precio: 9  },
    // — Tableau —
    "Starter Pack — Ventas":                 { precio: 19  },
    "Public Portfolio Template":             { precio: 19  },
    // — SQL —
    "Templates Pack — 50+ Queries BI":       { precio: 19  },
    "Pack — Entrevistas Data Engineer":      { precio: 9  },
    "SQL Cheatsheet — Window Functions":     { precio: 0   },
    // — dbt —
    "Project Starter":                       { precio: 19  },
    "Macro Library — 30+ macros Jinja":      { precio: 9  },
    // — Excel —
    "Automation con Macros VBA":             { precio: 19  },
    "Power Query Templates":                 { precio: 9  },
    "Excel → Python Migrator Kit":           { precio: 19  },
    // — Python —
    "Task Automation Kit":                   { precio: 19  },
    "Data Pipeline con Python + Airflow":    { precio: 19  },
    "Pack de Alertas — Email / Slack":       { precio: 9  },
    // — Shell / Scripting —
    "Automation Pack — Windows Admin":       { precio: 19  },
    "Bash Scripts Pack — Unix/Linux":        { precio: 19  },
    "CI/CD para Data Projects":              { precio: 9  },
    // — ETL —
    "ETL Patterns con Python (sin Airflow)": { precio: 19  },
    "Mapping Templates":                     { precio: 19  },
    // — Cloud —
    "GCP / BigQuery Setup Guide":            { precio: 19  },
    "Azure Data Factory Pipelines Starter":  { precio: 29  },
    // — Arquitectura —
    "Data Warehouse Architecture Guide":     { precio: 19  },
    // — Cursos —
    "dbt + BigQuery desde cero":             { precio: 57, orig: 197 },
    "SQL Avanzado para Data Engineers":      { precio: 29,  orig: 149 }
  },

  // ── EMPRESAS ───────────────────────────────────────────────────────
  empresas: [
    { nombre: "Accenture",     rol: "Data Architecture",   periodo: "2010-2014" },
    { nombre: "IBM",           rol: "Data Engineering",    periodo: "2014-2017" },
    { nombre: "Soprasteria",   rol: "Senior BI Architect", periodo: "2017-2020" },
    { nombre: "Línea Directa", rol: "BI Lead",             periodo: "2020-2022" },
    { nombre: "Bankinter",     rol: "Data Engineer",       periodo: "2022-2023" },
    { nombre: "Orange",        rol: "Analytics Engineer",  periodo: "2023-2024" }
  ],

  // ── TECNOLOGÍAS ────────────────────────────────────────────────────
  tech: ["Power BI","SQL","dbt","BigQuery","Snowflake","Python","Airflow","Informatica","Talend","Azure DF","Databricks","Redshift"],

  // ── SERVICIOS ──────────────────────────────────────────────────────
  servicios: [
    {
      titulo: "Consultoría BI & Power BI",
      precio: "Desde 800 €/día",
      desc:   "Soluciones Power BI end-to-end: modelo de datos, DAX avanzado y dashboards ejecutivos listos para producción.",
      items:  ["Modelado dimensional (Kimball)", "DAX avanzado y optimización", "Row Level Security corporativo", "Conexión a ERP/CRM vía DirectQuery"]
    },
    {
      titulo: "Data Engineering & ETL/ELT",
      precio: "Desde 900 €/día",
      desc:   "Pipelines de datos escalables en cloud con las herramientas más demandadas del mercado.",
      items:  ["Pipelines con dbt + Airflow", "Migración a cloud GCP / Azure / AWS", "Arquitectura medallion (Bronze/Silver/Gold)", "CDC e integración incremental"]
    },
    {
      titulo: "Formación & Mentoring",
      precio: "Desde 400 €/sesión",
      desc:   "Formación técnica en SQL, Power BI y Data Engineering para equipos y profesionales.",
      items:  ["Workshops intensivos 1-3 días", "Mentoring 1:1 semanal", "Material personalizado incluido", "Seguimiento post-formación"]
    },
    {
      titulo: "Auditoría de Datos",
      precio: "Desde 1.500 €",
      desc:   "Revisión completa de tu stack de datos: arquitectura, calidad de datos, gobierno y plan de mejora.",
      items:  ["Audit de calidad de datos", "Revisión modelos Power BI / DAX", "Informe ejecutivo + sesión de presentación", "Roadmap de mejoras priorizado"]
    }
  ],

  // ── PRODUCTOS DESTACADOS ───────────────────────────────────────────
  productosDestacados: [
    { titulo: "Dashboard Kit Finanzas — Power BI", categoria: "Power BI", precio: 29, precioOrig: 89, desc: "P&L, Cashflow, Balance y KPIs ejecutivos. Conecta a cualquier ERP vía DirectQuery." },
    { titulo: "SQL Templates Pack — 50+ Queries",  categoria: "SQL",      precio: 19, precioOrig: null, desc: "Window functions, cohortes, pivots y métricas de negocio para BigQuery, Snowflake y Postgres." },
    { titulo: "dbt + BigQuery Project Starter",     categoria: "dbt",      precio: 19, precioOrig: null, desc: "Arquitectura medallion completa con tests, macros y seeds. Listo para GCP." }
  ],

  // ── BLOG ARTÍCULOS ─────────────────────────────────────────────────
  articulos: [
    { id:"etl",     titulo:"ETL vs ELT en 2025: ¿cuál domina el mercado cloud?",          categoria:"ETL",   fecha:"12 Mar 2025", min:8,  resumen:"La migración al cloud ha cambiado las reglas del juego. Analizo si ELT ha sustituido realmente al ETL clásico." },
    { id:"dax",     titulo:"TOP 10 funciones DAX que todo analista BI debe dominar",       categoria:"BI",    fecha:"28 Feb 2025", min:6,  resumen:"Después de revisar más de 200 proyectos Power BI, estas son las funciones que marcan la diferencia." },
    { id:"sql",     titulo:"SQL Window Functions: la guía definitiva con 20 ejemplos",     categoria:"SQL",   fecha:"15 Feb 2025", min:10, resumen:"ROW_NUMBER, RANK, LAG, LEAD... Las window functions que muchos data analysts aún no dominan." },
    { id:"dbt",     titulo:"dbt en 2025: el estándar del Data Warehouse moderno",          categoria:"Cloud", fecha:"1 Feb 2025",  min:9,  resumen:"dbt ha revolucionado las transformaciones en el DWH. Explico cómo empezar y por qué es el futuro." },
    { id:"kimball", titulo:"Kimball vs Data Vault 2.0: ¿qué modelo DWH elegir?",           categoria:"Cloud", fecha:"15 Ene 2025", min:9,  resumen:"Comparativa honesta después de implementar ambos en proyectos reales de Fortune 500." },
    { id:"tools",   titulo:"Informatica vs Talend: comparativa honesta 2025",              categoria:"Tools", fecha:"5 Ene 2025",  min:7,  resumen:"Dos décadas usando ambas herramientas. Todo comparado sin filtros." }
  ]
};
