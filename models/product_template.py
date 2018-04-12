# -*- coding: utf-8 -*-
# © 2018 Ravi Krishnan (ravi73164@gmail.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class ProductTemplate(models.Model):
    """Inherit product template ."""

    _inherit = 'product.template'

    moq = fields.Float('Minimum Order Quantity')
    mpq = fields.Float('Minimum Packing Quantity')

