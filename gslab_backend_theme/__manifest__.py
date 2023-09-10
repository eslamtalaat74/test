{
    "name": "GSLab Backend Theme",
    "summary": "YABT based on responsive web client and inspired by Openworx",
    "version": "14.0.1.2.4",
    "category": "Themes/Backend",
    "website": "https://www.gslab.it",
    "author": "Giovanni - GSLab",
    "live_test_url": "https://odoo.gslab.it",
    "price": "49",
    "currency": "EUR",
    "license": "LGPL-3",
    "support": "giovanni@gslab.it",
    "installable": True,
    "depends": ['base_setup', 'mail'],
    "data": [
        "views/assets.xml", "views/res_users.xml", "views/web.xml",
        "views/res_config_settings_views.xml"
    ],
    "qweb": [
        "static/src/xml/apps.xml",
        "static/src/xml/form_buttons.xml",
        "static/src/xml/menu.xml",
        "static/src/xml/navbar.xml",
        "static/src/xml/attachment_viewer.xml",
        "static/src/xml/discuss.xml",
    ],
    "images": [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook'
}
