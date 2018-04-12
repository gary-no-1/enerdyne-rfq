# -*- coding: utf-8 -*-
# Copyright 2018 Ravi Krishnan (<http://ravi73164.tumblr.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Purchase Requisitions Report ',
    'summary': 'Reporting on Item / Vendor for Purchase Requisitions ',
    'author': 'Ravi Krishnan',
    'website': 'http://ravi73164.tumblr.com',
    'category': 'Purchase',
    'license': 'AGPL-3',
    'version': '10.0.1.0.0',
    'depends': [
        'purchase',
        'stock',
        'sale',
    ],
    'data': [
        'views/menus.xml',
        'views/purchase_order_view.xml',
        'views/purchase_order_line_view.xml',
        'views/purchase_requisition_view.xml',
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
}
