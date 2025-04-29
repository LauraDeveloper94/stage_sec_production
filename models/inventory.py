# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Inventory(models.Model):
    
    _name = 'stage_sec_production.inventory'
    _description = 'Inventory'

    stock_min = fields.Integer(string = "Minimum stock", required=True)
    stock_max = fields.Integer(string = "Maximum stock", required=True)
    stock_quantity = fields.Integer(string = "Quantity", required=True)
    location = fields.Char(string = "Location", required=True, size=100)
    entry_date = fields.Date(string = "Entry date", required=True)
    exit_date = fields.Date(string = "Exit date", required=True)
    last_update = fields.Date(string = "Last update", required=True)
    stock_alert = fields.Boolean(string="Stock alert", compute="_compute_stock_alert", store = True)

    manufacturing_ids = fields.One2many('stage_sec_production.manufacturing', 'inventory_id')

    @api.depends('stock_quantity', 'stock_min')

    def _compute_stock_alert(self):
        for i in self:
            i.stock_alert = i.stock_quantity < i.stock_min  

