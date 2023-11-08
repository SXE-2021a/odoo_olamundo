# -*- coding: utf-8 -*-
{
    'name': "odoo_olamundo",

    'summary': """
       Proxecto de benvida""",

    'description': """
       proxecto inicial
    """,

    'author': "Eu mesmo",
    'website': "https://www.edu.xunta.gal/centros/iesteis/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/olamundo.xml',
        'views/menu.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
