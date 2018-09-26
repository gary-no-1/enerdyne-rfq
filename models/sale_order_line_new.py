# -*- coding: utf-8 -*-
# © 2018 Ravi Krishnan (ravi73164@gmail.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
import datetime

class SaleOrderLine(models.Model):
    """Inherit sale order  line."""

    _inherit = 'sale.order.line'

    moq = fields.Float('M.O.Q',related='product_id.moq',store=True)
    mpq = fields.Float('M.P.Q',related='product_id.mpq',store=True)
    sale_delay = fields.Float('Lead Time',related='product_id.sale_delay',store=True)

    dlvy_date = fields.Date('Dlvy Date')
    dlvy_week = fields.Char('Dlvy Week', readonly=True, compute='_compute_week_no')

    @api.change(dlvy_date)
    def _dlvy_date_onchange(self):
         if self.dlvy_date:
             date = datetime.strptime(self.dlvy_date, "%Y-%m-%d") 
             year = date.year
             month = date.month
             day = date.day
             dt = datetime.date(year,month,day)
             yr = dt.isocalendar()[0]
             wk = dt.isocalendar()[1]
             self.dlvy_week = str(yr) + '/' + str(wk).zfill(2)
         return true

