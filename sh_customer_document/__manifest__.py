# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Customer Document Management",

    "author": "Softhealer Technologies",

    "license": "OPL-1",

    "website": "https://www.softhealer.com",

    "support": "support@softhealer.com",

    "version": "14.0.1",

    "category": "Document Management",

    "summary": "Customer Document Management,Customers Document Management,Customer Documents Management,Customers Documents Management, Manage Customer Document,Manage Documents,Customer Document,Employee Document Management Odoo",
    
    "description": """This module is very useful to manage important documents of the customer. It helps to send email notifications to customers for document expiration. You can send notifications before/after the expiry date as well as when the document expires. We provide a multiple email feature that helps to send email notifications to multiple employees at a time. You can see the document without download using the document smart button. This module allows sending the notification using scheduled action or manually. cheers!""",

    "depends": ['contacts'],
    "data": [

        'security/ir.model.access.csv',
        'security/customer_document_security.xml',

        'data/customer_document_email_notification_template.xml',
        'data/customer_document_scheduler.xml',

#         'views/customer_document.xml',
        'views/sh_ir_attachments_views.xml',
        'views/res_partner.xml',
        'views/general_config_settings.xml',
    ],
    "images": ["static/description/background.png", ],

    "installable": True,
    "auto_install": False,
    "application": True,
    "price": "12",
    "currency": "EUR"
}
