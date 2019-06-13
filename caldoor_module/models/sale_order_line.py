# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrderLineInherit(models.Model):
    _inherit = "sale.order.line"

    width = fields.Char(string="Width")
    depth = fields.Char(string="Depth")
    height = fields.Char(string="Height")
    sqft = fields.Float(string="SqFt/Box")
    sqft_price = fields.Float(string="SqFt Price")
