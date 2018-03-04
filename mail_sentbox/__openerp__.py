# -*- coding: utf-8 -*-

{
    'name': 'Sent Messages',
    'version': '8.0.1.0.0',
    'license':'LGPL-3',
    'category': 'Social Network',
    'summary': 'Filter Sent Messages in Messaging menu.',
    'description': '''
        Filter Sent Messages in Messaging menu.
    ''',
    'author': 'Aleksandra Shumkoska',
    'support': 'a_shumkoska@yahoo.com',
    'depends': [
        'mail'
    ],
    'data': [
        'views/mail_thread_view.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'css': ['static/src/css/description.css'],
    'installable': True,
    'auto_install': False,
}