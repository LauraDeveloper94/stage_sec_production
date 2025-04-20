# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Product(models.Model):
    
    _name = 'stage_sec_production.product'
    _description = 'Product'
    
    name = fields.Char(string="Name", required=True, size=50)
    description = fields.Char(string="Description", required=True, size=200)
    price = fields.Float(string = "Price", required=True)
    dimensions = fields.Float(string = "Dimensions", required=True)
    weight = fields.Float(string = "Weight", required=True)