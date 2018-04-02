# -*- coding: utf-8 -*-
# © 2018 Ravi Krishnan (ravi73164@gmail.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from datetime import datetime, time

class PurchasOrderLine(models.Model):
    """Inherit purchase order line."""

    _inherit = 'purchase.order.line'

    tender = fields.Char('Purc. Agreement #',related='order_id.origin')
    order_no = fields.Char('P.O.#',related='order_id.name')
    order_date = fields.Datetime(related='order_id.date_order')
    partner_ref = fields.Char('Supplier Ref',related='order_id.partner_ref')
    partner_ref_date = fields.Date('Supplier Ref Date',related='order_id.partner_ref_date')

    landed_price = fields.Float('Landed Price')
