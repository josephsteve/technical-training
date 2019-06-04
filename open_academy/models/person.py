# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Person(models.Model):
    _name = 'open_academy.person'
    _description = 'Person Information'

    # name = fields.Char(compute='_compute_name')

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)

    # @api.depends('first_name', 'last_name')
    # def _compute_name(self):
    #     for record in self:
    #         record.name = f'{record.first_name} {record.last_name}'

    @api.multi
    def name_get(self):
        return [(record.id, f'{record.first_name} {record.last_name}') for record in self]
