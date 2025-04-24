# -*- coding: utf -8 -*-
from odoo import models, fields, api


class Order(models.Model):
    
    _name = 'stage_sec_production.order'
    _description = 'Order'
    
    date = fields.Date(string="Date", required=True)
    total_price = fields.Float(string = "Total price", required=True)
    status = fields.Char(string = "Status", required=True, size=50)
    delivery_address = fields.Char(string = "Delivery address", required=True, size=100)
    payment_method = fields.Char(string = "Payment method", required=True)
    payment_status = fields.Char(string = "Payment status", required=True)

    client_id = fields.Many2one('stage_sec_production.client') 