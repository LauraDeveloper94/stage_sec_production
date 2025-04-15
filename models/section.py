# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Section(models.Model):

    _name = 'stage_sec_production.section'
    _description = 'Section'

    name = fields.Char(string = "Section name", required=True)
    location = fields.Char(string = "Section location", required=True)