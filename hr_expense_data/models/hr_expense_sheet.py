# Copyright 2014 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"
    _rec_name = "number"

    number = fields.Char(string="رقم فاتورة المورد")
    vendor = fields.Many2one('res.partner',string="المورد")
    adress = fields.Char(string="العنوان")
    tax_id = fields.Char(string="المعرف الضريبي")

