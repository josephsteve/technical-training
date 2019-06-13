# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    x_category_id = fields.Many2one("product.category", string="Category")
