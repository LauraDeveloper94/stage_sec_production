# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Product(models.Model):
    
    _name = 'stage_sec_production.product'
    _description = 'Product'
    
    name = fields.Char(string="Product name", required=True)
    description = fields.Char(string="Product description", required=True)
    price = fields.Float(string = "Price of the product", required=True)
    dimensions = fields.Float(string = "Dimensions of the product", required=True)
    weight = fields.Float(string = "Weight of the product", required=True)
    stock_min = fields.Integer(string = "Minimum stock", required=True)
    stock_max = fields.Integer(string = "Maximum stock", required=True)