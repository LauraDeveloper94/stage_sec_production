# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Client(models.Model):
    _name = 'stage_sec_production.client'
    _description = 'Client'
    
    name = fields.Char(string="Name", required=True, size=20)
    email = fields.Char(string="Email", required=True, size=100)
    surname1 = fields.Char(string="First surname", required=True, size=20)
    surname2 = fields.Char(string="Second surname", size=20)
    phone_number = fields.Char(string="Phone number", size=15)
    type = fields.Selection(
        [('wholesaler', 'Wholesaler'), ('retailer', 'Retailer')],
        string="Type", required=True
    )
    address = fields.Char(string="Address", required=True, size=100)
