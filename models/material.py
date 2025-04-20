# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Material(models.Model):
    
    _name = 'stage_sec_production.material'
    _description = 'Material'
    
    name = fields.Char(string="Material", required=True, size=50)
    type = fields.Char(string="Type", required=True)
    price = fields.Float(string = "Price", required=True)
    dimensions = fields.Float(string = "Dimensions", required=True)
    weight = fields.Float(string = "Weight", required=True)
    stock_min = fields.Integer(string = "Minimum stock", required=True)
    stock_max = fields.Integer(string = "Maximum stock", required=True)
    stock_quantity = fields.Integer(string="quantity", compute="_compute_stock_alert", store=True)
    availability = fields.Integer(string = "Availability", required=True)

    @api.depends('stock_quantity', 'stock_min')

    def _compute_stock_alert(self):
        for i in self:
            i.stock_alert = i.stock_quantity < i.stock_min 