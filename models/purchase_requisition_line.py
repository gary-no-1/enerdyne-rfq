# -*- coding: utf-8 -*-
# © 2017 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from datetime import datetime, time

class PurchaseRequisitionLine(models.Model):
    """Inherit purchase requistion line."""

    _inherit = 'purchase.requisition.line'