# -*- coding: utf-8 -*-
{
    'name': "hta_custom_product",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #views
        'views/views.xml',
        'views/templates.xml',
        'views/product_category_views.xml',
        'views/product_views.xml',
        #data
        'data/product_category_code_seq.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    
    "installable": True,
    "pre_init_hook": "pre_init_product_category_code",
    #"post_init_hook": "post_init_product_category_code",
}
