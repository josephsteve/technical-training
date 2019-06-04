# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sessions(models.Model):
    _name = 'open_academy.sessions'
    _description = """
    Sessions Information
    """

    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    course = fields.Many2one('open_academy.course', ondelete='set null', required=True)