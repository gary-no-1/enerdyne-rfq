# -*- coding: utf-8 -*-
# © 2018 Ravi Krishnan (ravi73164@gmail.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from datetime import datetime, time

class PurchasRequisition(models.Model):
    """Inherit purchase requisition ."""

    _inherit = 'purchase.requisition'

    opportunity_id = fields.Many2one(
        'crm.lead',
        'Opportinity Number'
    )

    sale_order_id = fields.Many2one(
        'sale.order',
        'Sale Order'
    )

    partner_ref_date = fields.Date(string="Supplier Reference Date")

