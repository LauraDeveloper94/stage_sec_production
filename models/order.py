# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Order(models.Model):
    
    _name = 'stage_sec_production.order'
    _description = 'Order'
    
    order_number = fields.Char(string="Order number", required=True)
    date = fields.Date(string="Date", required=True)
    total_price = fields.Float(string = "Total price", required=True)
    status = fields.Char(string = "Status", required=True, size=50)
    delivery_address = fields.Char(string = "Delivery address", required=True, size=100)
    payment_method = fields.Char(string = "Payment method", required=True)
    payment_status = fields.Char(string = "Payment status", required=True)

    client_id = fields.Many2one('stage_sec_production.client') 
    product_ids = fields.Many2many('stage_sec_production.product', 'order_product_rel', 'order_id', 'product_id') 

    _sql_constraints = [
    ('unique_order_number', 'unique(order_number)', 'The order number must be unique.')
    ]

    @api.constrains('total_price')
    def _check_total_price(self):
        for i in self:
            if i.total_price < 0:
                raise ValidationError("The total price cannot be negative.")