# -*- coding: utf-8 -*-
# © 2018 Ravi Krishnan (ravi73164@gmail.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from datetime import datetime, time

class PurchasOrder(models.Model):
    """Inherit purchase order ."""

    _inherit = 'purchase.order'

    partner_ref_date = fields.Date(string="Supplier Reference Date")
    rfq_valid_from = fields.Date(string="Valid From")
    rfq_valid_upto = fields.Date(string="Valid Uptil")


