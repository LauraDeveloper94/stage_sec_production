# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Material(models.Model):
    
    _name = 'stage_sec.material'
    _description = 'Material'
    
    material_name = fields.Char(string="Material", required=True)
    material_type = fields.Char(string="Type of material", required=True)
    price = fields.Float(string = "Price of the material", required=True)
    dimensions = fields.Float(string = "Dimensions of the material", required=True)
    weight = fields.Float(string = "Weight of the material", required=True)
    stock_min = fields.Integer(string = "Minimum stock", required=True)
    stock_max = fields.Integer(string = "Maximum stock", required=True)
    availability = fields.Integer(string = "Availability of the material", required=True)