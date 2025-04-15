# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Manufacturing(models.Model):
    
    _name = 'stage_sec_production.manufacturing'
    _description = 'Manufacturing'
    
    quantity = fields.Integer(string="Quantity of manufacturing", required=True)
    phase = fields.Char(string="Phase of manufacturing", required=True)
    start_date = fields.Date(string = "Start date", required=True)
    end_date = fields.Date(string = "End date", required=True)