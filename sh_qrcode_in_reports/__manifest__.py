# -*- coding: utf-8 -*-
{
    "name": "Print QR Code in sales, purchase, inventory, accounts, and mrp reports | Sale Order QR Code | Purchase Order QR Code | Invoice QR Code | Inventory QR Code | Manufacturing QR Code In Reports",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "license": "OPL-1",
    "version": "14.0.1",
    "category": "Extra Tools",
    "summary": """
qr code in sale order app, qr code in purchase order,
qr code in warehouse, qr code in account,purchase qr,
qr code in mrp report, invoice qr, sales qr module,
qr code in vendor bill, qr code in inventory odoo
""",
    "description": """
QR codes eliminate the possibility of human error.
The occurrence of errors for manually entered data
is significantly higher than that of QR codes.
A QR code scan is fast and reliable and takes
infinitely less time than entering data by hand.
This module uses to show QR code in sale order reports,
purchase order reports, warehouse reports, accounting reports,
and MRP reports. Very useful to make the process faster,
Quickly read sale order, purchase order, invoice, bills,
delivery order, picking operation, MRP order no by QR Code.
qr code in sale order app, qr code in purchase order,
qr code in warehouse reports, qr code in accounting module,
qr code in mrp report, qr code in invoice module,
qr code in vendor bill, qr code in inventory odoo
""",
    "depends": [
        "purchase",
        "sale_management",
        "stock",
        "mrp",
        "account"
    ],
    "data": [
        "reports/sale_order_report.xml",
        "reports/purchase_order_report.xml",
        "reports/account_invoice_report.xml",
        "reports/stock_delivery_slip_report.xml",
        "reports/manufacturing_report.xml",
    ],
    "images": ["static/description/background.png", ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "price": 18,
    "currency": "EUR"
}
