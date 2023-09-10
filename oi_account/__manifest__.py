# -*- coding: utf-8 -*-
{
    'name': "Accounting Extension",

    'summary': 'Extension in Accounting, Accounting Extension, Enable Accounting Features, Enable Canceling Entries by Defaults, Add Accounts Company Domain for Contact/Product/Product Category, Multiple Company - Invoice Accounts/Journal Company Validation',
    
    'description' : """
        * enable accounting features
    """,

    "author": "Openinside",
    "license": "OPL-1",
    'website': "https://www.open-inside.com",
    "price" : 0,
    "currency": 'EUR',
    'category': 'Accounting',
    'version': '14.0.1.1.4',
    'images':[
        'static/description/cover.png'
        ], 

    # any module necessary for this one to work correctly
    'depends': ['account','payment'],

    # always loaded
    'data': [
        'security/group.xml',
        'view/account_chart_template.xml',
        'view/account_account_type.xml',
        'view/action.xml',       
        'view/menu.xml',
        'view/res_config_settings_views.xml'
        
    ],    
    'odoo-apps' : True,
    'auto_install': True,
}