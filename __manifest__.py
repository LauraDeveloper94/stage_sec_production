# -*- coding: utf-8 -*-
{
    'name': "StageSec Production Module",

    'summary': "Module to manage and automate StageSec's production",

    'description': """
        This module helps StageSec manage production orders, schedule manufacturing tasks, and control inventory, machinery, and employees.
    """,

    'author': "Laura Nácher",
    'website': "http://www.stagesec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/client.xml',
        'data/department.xml',
        'data/inventory.xml',
        'data/manufacturing.xml',
        'data/material.xml',
        'data/production_order.xml',
        'data/product.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
