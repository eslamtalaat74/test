# -*- coding: utf-8 -*-
{
    "name": "Is Customer, Is a Vendor",
    "version": "14.0",
    'summary': """
        This module is allow you to set partner Is a customer or Is a vendor | Is a Supplier""",
    'description': """
Is a Customer, Is a Vendor, Is a supplier
        """,    
    "category": "Extra Tools",
    'author': "Preway IT Solutions",
    "sequence": 2,
    "depends" : ['sale', 'purchase'],
    "data" : [
        'views/res_partner_view.xml',
    ],
    'post_init_hook': 'update_existing_partners',
    'price': 5.0,
    'currency': 'EUR',
    "installable": True,
    "auto_install": False,
    "images":["static/description/Banner.png"],
}
