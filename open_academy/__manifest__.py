# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        My very first module created for Odoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Joseph Serrano",
    'website': "http://www.caldoor.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Demo',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
#         'demo/demo.xml',
    ],
}