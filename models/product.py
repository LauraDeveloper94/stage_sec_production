# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Product(models.Model):
    
    _name = 'stage_sec_production.product'
    _description = 'Product'
    
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description", required=True)
    price = fields.Float(string = "Price", required=True)
    dimensions = fields.Float(string = "Dimensions", required=True)
    weight = fields.Float(string = "Weight", required=True)
    stock_min = fields.Integer(string = "Minimum stock", required=True)
    stock_max = fields.Integer(string = "Maximum stock", required=True)