# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Production_order(models.Model):
    _name = 'stage_sec_production.production_order'
    _description = 'Production order'
    
    start_date = fields.Date(string="Start date", required=True)
    status = fields.Char(string="Status", required=True)
    end_date = fields.Date(string="End date", required=True)
    priority_level = fields.Char(string="Priority level", required=True)
