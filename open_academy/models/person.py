# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Person(models.Model):
    _name = 'open_academy.person'
    _description = """
        Sessions Information
        """

    name = fields.Char(compute='_compute_name')

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for record in self:
            record.name = record.first_name + " " + record.last_name