# -*- coding: utf-8 -*-
{
    'name' : 'POS Category Company Restrict',
    'version' : '14.0',
    'category' : 'Sales/Point of Sale',
    "author": "Ahmed Elmahdi",
    'summary': 'POS Category Company Restrict',
    "price": 5,
    "currency": "EUR",
    "license": "LGPL-3",
    "description": """
POS Category company restrict
show POS categories for each company
    """,
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_category_view.xml',
        'security/pos_category_restrict_security.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "images":['static/description/pos_categroy.png'],
}
