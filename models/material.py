# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Material(models.Model):
    
    _name = 'stage_sec_production.material'
    _description = 'Material'
    
    name = fields.Char(string="Material", required=True)
    type = fields.Char(string="Type", required=True)
    price = fields.Float(string = "Price", required=True)
    dimensions = fields.Float(string = "Dimensions", required=True)
    weight = fields.Float(string = "Weight", required=True)
    stock_min = fields.Integer(string = "Minimum stock", required=True)
    stock_max = fields.Integer(string = "Maximum stock", required=True)
    availability = fields.Integer(string = "Availability", required=True)