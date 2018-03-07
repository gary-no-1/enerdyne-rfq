# -*- coding: utf-8 -*-
# © 2017 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from datetime import datetime, time

class PurchasOrderLine(models.Model):
    """Inherit purchase order line."""

    _inherit = 'purchase.order.line'

    tender = fields.Char(related='order_id.origin')
    order_no = fields.Char(related='order_id.name')
    order_date = field.Date(related='order_id.date_order',default=lambda s: fields.Date.context_today(s))

