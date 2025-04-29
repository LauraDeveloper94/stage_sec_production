# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Section(models.Model):

    _name = 'stage_sec_production.section'
    _description = 'Section'

    name = fields.Char(string = "Name", required=True, size=100)
    location = fields.Char(string = "Location", required=True, size=100)

    employee_ids = fields.One2many('stage_sec_production.employee', 'section_id')
    department_id = fields.Many2one('stage_sec_production.department')
