# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course Information'

    _rec_name = 'title'
    title = fields.Char(string='Title')
    # name = fields.Char(string='Title', required=True)
    level = fields.Selection([
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    ], string='Difficulty')