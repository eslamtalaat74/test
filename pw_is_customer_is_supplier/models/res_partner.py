# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer = fields.Boolean(compute='_compute_is_a_customer', inverse='_inverse_is_a_customer',
        store=True, string='Is a Customer',
        help="Check this box if this contact is a customer. It can be selected in sales orders.")
    supplier = fields.Boolean(compute='_compute_is_a_supplier', inverse='_inverse_is_a_supplier',
        store=True, string='Is a Vendor',
        help="Check this box if this contact is a vendor. It can be selected in purchase orders.")


    @api.depends('customer_rank')
    def _compute_is_a_customer(self):
        for partner in self:
            partner.customer = True if partner.customer_rank > 0 else False

    def _inverse_is_a_customer(self):
        for partner in self:
            partner.customer_rank = 1 if partner.customer else 0

    @api.depends('supplier_rank')
    def _compute_is_a_supplier(self):
        for partner in self:
            partner.supplier = True if partner.supplier_rank > 0 else False

    def _inverse_is_a_supplier(self):
        for partner in self:
            partner.supplier_rank = 1 if partner.supplier else 0
