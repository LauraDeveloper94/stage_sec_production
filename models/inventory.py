# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Inventory(models.Model):
    
    _name = 'stage_sec_production.inventory'
    _description = 'Inventory'

    stock_min = fields.Integer(string = "Minimum stock", required=True)
    stock_max = fields.Integer(string = "Maximum stock", required=True)
    stock_quantity = fields.Integer(string = "Quantity", required=True)
    location = fields.Char(string = "Location", required=True)
    entry_date = fields.Date(string = "Entry date", required=True)
    exit_date = fields.Date(string = "Exit date", required=True)
    last_update = fields.Date(string = "Last update", required=True)