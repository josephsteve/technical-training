# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class CustomerPartner(models.Model):
    _inherit = "res.partner"

    credit_hold = fields.Char(string="Credit Hold")
    custno = fields.Char(string="CustNo")
    discount = fields.Float(string="Discount %")
    fax = fields.Char(string="Fax")
    h_type = fields.Char(string="H Type")
    shipping_notes = fields.Text(string="Shipping Notes")
    shipvia = fields.Char(string="Ship Via")
    tax_code = fields.Many2one("account.tax", string="Tax Code")
    tax_exempt = fields.Char(string="Tax Exempt #")