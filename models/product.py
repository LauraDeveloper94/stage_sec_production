# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Product(models.Model):
    
    _name = 'stage_sec_production.product'
    _description = 'Product'
    
    name = fields.Char(string="Name", required=True, size=50)
    quantity = fields.Integer(string="Quantity", required=True)
    description = fields.Char(string="Description", required=True, size=200)
    price = fields.Float(string = "Price", required=True)
    dimensions = fields.Float(string = "Dimensions", required=True)
    weight = fields.Float(string = "Weight", required=True)

    order_id= fields.Many2one('stage_sec_production.order') 
    manufacturing_ref_id = fields.Many2one('stage_sec_production.manufacturing') 

    @api.constrains('price')
    def _check_price(self):
        for i in self:
            if i.price < 0:
                raise ValidationError("The price cannot be negative.")

    @api.constrains('weight')
    def _check_weight(self):
        for i in self:
            if i.weight < 0:
                raise ValidationError("The weight cannot be negative.")