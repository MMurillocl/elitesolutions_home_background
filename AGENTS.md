# AGENTS.md - elitesolutions_home_background

Módulo Odoo 19 (Enterprise) de EliteSolutions: fondo del menú de aplicaciones con la marca
"Implementado por EliteSolutions", sin Odoo Studio.

## Por qué existe
En Odoo Enterprise el fondo personalizado (`res.company.background_image`) lo define
`web_studio`. Clientes Odoo.sh sin Studio (HDS, Santa Cristina, H2S) no tienen ese campo.
Mario descartó instalar Studio: este módulo logra lo mismo con CSS.

## Cómo funciona
`web_enterprise/.../home_menu_background.scss` pinta el fondo con
`var(--homeMenu-bg-image, url(background-light.svg))` sobre `.o_home_menu_background`.
`static/src/scss/home_background.scss` redefine esa variable (bundle `web.assets_backend`).
Sin modelos, campos ni permisos. Desinstalar = vuelve el fondo original.

## Imagen
`static/img/fondo_home.png` (2560x1440), generada con
`C:\repos\elitesolutions\meta\fondo-home\generar_fondo_home.py` (marcas Odoo + Elite al 76% de alto,
translúcidas). Para cambiarla: regenerar y reemplazar el archivo (subir versión del manifest).

## Reglas
- NO instalar en bases que ya tengan Studio y un fondo propio (el de Studio se aplica por estilo en línea y gana).
- Repo público a propósito (así Odoo.sh lo clona sin deploy key); no meter datos de clientes.

## Changelog AGENTS.md

| Fecha | IA | Sección modificada | Por qué |
|-------|----|--------------------|---------|
| 2026-11-05 | Claude | Todo | Creación: Mario pidió un módulo chico, no privado, para clientes SH sin Studio (HDS, Santa Cristina, H2S) |
