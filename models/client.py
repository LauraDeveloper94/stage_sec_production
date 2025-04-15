# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Client(models.Model):
    _name = 'stage_sec_production.client'
    _description = 'Client'
    
    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    surname1 = fields.Char(string="First surname", required=True)
    surname2 = fields.Char(string="Second surname")
    phone_number = fields.Integer(string="Phone number")
    type = fields.Selection(
        [('wholesaler', 'Wholesaler'), ('retailer', 'Retailer')],
        string="Type", required=True
    )
    address = fields.Char(string="Address", required=True)
