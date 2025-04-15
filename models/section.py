# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Section(models.Model):

    _name = 'stage_sec_production.section'
    _description = 'Section'

    section_name = fields.Char(string = "Section name", required=True)
    section_location = fields.Char(string = "Section location", required=True)