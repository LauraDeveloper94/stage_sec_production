# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Client(models.Model):
    _name = 'stage_sec_production.client'
    _description = 'Client'
    
    name = fields.Char(string="Name", required=True, size=20)
    email = fields.Char(string="Email", required=True, size=100)
    surname1 = fields.Char(string="First surname", required=True, size=20)
    surname2 = fields.Char(string="Second surname", size=20)
    phone_number = fields.Char(string="Phone number", size=15)
    address = fields.Char(string="Address", required=True, size=100)
    type = fields.Selection(
        [('wholesaler', 'Wholesaler'), ('retailer', 'Retailer')],
        string="Type", required=True
    ) 

    order_ids = fields.One2many('stage_sec_production.order', 'client_id')  

    _sql_constraints = [
    ('email_unique', 'UNIQUE(email)', 'The email must be unique.'),
    ]


    @api.constrains('email')
    def _check_email_format(self):
        email_validation = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for i in self:
            if i.email and not re.match(email_validation, i.email):
                raise ValidationError("The email format is invalid. Please enter a valid email address")

    @api.constrains('phone_number')
    def _check_phone_number_format(self):
        phone_validation = r'^\+?[0-9\s\-\(\)]{7,15}$'
        for i in self:
            if i.phone_number and not re.match(phone_validation, i.phone_number):
                raise ValidationError("The phone number format is invalid. Please enter a valid phone number")
    