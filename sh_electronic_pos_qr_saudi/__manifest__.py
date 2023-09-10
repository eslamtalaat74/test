# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
{
    "name": "Electronic invoice KSA - Point of sale | Saudi Invoice QR Code  | Invoice based on TLV Base64 string QR Code | Saudi Electronic Invoice with Base64 TLV QRCode",
    'author': 'Softhealer Technologies',
    'website': 'https://www.softhealer.com',
    "support": "support@softhealer.com",
    'version': '14.0.14',
    'category': "Point of Sale",
    'summary': "Electronic invoice KSA - POS Saudi Electronic Invoice for POS Receipt Saudi VAT E-Invoice for POS Electronic Pos QR Saudi Saudi VAT E-Invoice for POS Electronic Invoice with QR code arabic translations Customer Invoice Arabic headers arabic name Odoo",
    'description': """This module allows you to print a Saudi electronic invoice with a QR code in a POS receipt. You can customize the size (height and width) and position of QRCode on POS receipts (top & bottom). You can print POS receipts in regional and global languages, such as Arabic and English so you can print product names and company address in both languages in POS receipt. You can print receipt QRCode elements that include VAT, tax information, and other elements as needed. We provide a POS order line notes option and POS users can print the order line notes in the receipt. As per Saudi Arabia Zakat's regulations to apply specific terms to the electronic invoice by 4th of Dec 2021.""",
    "depends": ["point_of_sale", 'pos_restaurant'], #'l10n_sa_pos'
    "data": [
        'data/data.xml',
        'views/pos_config.xml',
        'views/assets.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/pos.xml', ],
    'images': ['static/description/background.png', ],
    "license": "OPL-1",
    "installable": True,
    "application": True,
    "autoinstall": False,
    "price": 65,
    "currency": "EUR"
}
