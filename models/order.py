# -*- coding: utf -8 -*-
from odoo import models, fields, api


class Order(models.Model):
    
    _name = 'stage_sec_production.order'
    _description = 'Order'
    
    order_date = fields.Date(string="Order date", required=True)
    total_price = fields.Float(string = "Total price of the order", required=True)
    order_status = fields.Char(string = "Order status", required=True)
    delivery_address = fields.Char(string = "Delivery address", required=True)
    payment_method = fields.Char(string = "Payment method", required=True)
    payment_status = fields.Char(string = "Payment status", required=True)
    client_id = fields.Many2one(
        'stage_sec.cliente', 
        string="Cliente", 
        required=True
    )