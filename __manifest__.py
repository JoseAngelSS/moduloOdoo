# -*- coding: utf-8 -*-
{
    'name': "Gestion y asignacion de proyectos",

    'summary': """
        En este modulo podemos asignar diferentes empleados""",

    'description': """
        En proceso
    """,

    'author': "Jose Angel Guisseppe Informatics",
    'website': "http://infsalinas.sytes.net:10250",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True ,
}
