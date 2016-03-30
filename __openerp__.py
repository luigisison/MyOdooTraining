# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': "Open Academy Course Management",

    'description': """
Open Academy Course Management
================================================
- Courses
- Sessions
- Attendees
""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base", "mail"],

    # always loaded
    'data': [
        "security/openacademy_security.xml",
        "security/ir.model.access.csv",
        "wizards/wizard_invite_partner_views.xml",
        "views/openacademy_views.xml",
        "views/openacademy_workflow.xml",
        "reports/report_sessions.xml",
        "views/openacademy_reports.xml",
    ],
    # only loaded in demonstration mode
    #'demo': [
    #  'demo/demo.xml',
    #],
}
