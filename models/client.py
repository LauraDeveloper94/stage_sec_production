# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Client(models.Model):
    _name = 'stage_sec.client'
    _description = 'Client'
    
    client_name = fields.Char(string="Client name", required=True)
    email = fields.Char(string="Email", required=True)
    surname1 = fields.Char(string="First surname", required=True)
    surname2 = fields.Char(string="Second surname")
    phone_number = fields.Integer(string="Phone number")
    client_type = fields.Selection(
        [('wholesaler', 'Wholesaler'), ('retailer', 'Retailer')],
        string="Type of client", required=True
    )
    client_address = fields.Char(string="Client address", required=True)
