# -*- coding: utf-8 -*-
{
    'name': 'EliteSolutions - Fondo del Menú de Aplicaciones',
    'version': '19.0.1.0.0',
    'category': 'Hidden',
    'summary': 'Fondo del menú de aplicaciones de Odoo Enterprise con la marca "Implementado por EliteSolutions", sin necesidad de Odoo Studio',
    'description': """
        Reemplaza el fondo del menú de aplicaciones (home menu) de Odoo Enterprise
        por una imagen discreta con marcas de agua de Odoo y de EliteSolutions
        ("Implementado por").

        En Odoo Enterprise el fondo personalizado solo se puede cambiar con Odoo
        Studio. Este módulo lo hace sin Studio: solo redefine la variable CSS
        --homeMenu-bg-image que ya usa web_enterprise. No agrega modelos, campos ni
        permisos. Para quitarlo basta desinstalar el módulo.
    """,
    'author': 'EliteSolutions Ltda.',
    'maintainer': 'EliteSolutions Ltda. <soporte@elitesolutions.cl>',
    'support': 'soporte@elitesolutions.cl',
    'website': 'https://www.elitesolutions.cl',
    'license': 'OPL-1',
    'depends': ['web_enterprise'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'elitesolutions_home_background/static/src/scss/home_background.scss',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
