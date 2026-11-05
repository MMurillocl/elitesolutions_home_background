# EliteSolutions - Fondo del Menú de Aplicaciones

Módulo Odoo 19 (Enterprise) que deja como fondo del menú de aplicaciones una imagen
discreta con marcas de agua de Odoo y "Implementado por EliteSolutions", **sin Odoo Studio**.

- Depende de `web_enterprise`. No agrega modelos, campos ni permisos.
- Redefine la variable CSS `--homeMenu-bg-image` (la misma que usa Odoo para su fondo).
- Desinstalar el módulo devuelve el fondo original.
- Imagen: `static/img/fondo_home.png` (2560x1440). Se genera con
  `elitesolutions/meta/fondo-home/generar_fondo_home.py`.

## Instalación

Agregar como submódulo en la rama de la versión y actualizar la lista de Apps:

    git submodule add -b 19.0 https://github.com/MMurillocl/elitesolutions_home_background.git MMurillocl/elitesolutions_home_background

## Autoría

EliteSolutions Ltda. - soporte@elitesolutions.cl - https://www.elitesolutions.cl - Licencia OPL-1.
