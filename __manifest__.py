# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# Copyright 2018 Ravi Krishnan (<http://ravi73164.tumblr.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Project Task Week Month',
    'summary': 'Adds field week , month to project task',
    'author': 'Ravi Krishnan',
    'website': 'http://ravi73164.tumblr.com',
    'category': 'Purchase',
    'license': 'AGPL-3',
    'version': '10.0.1.0.0',
    'depends': [
        'purchase',
    ],
    'data': [
        'views/menus.xml',
        'views/purchase_requistion_line_view.xml',
    ],
    'installable': True,
}
