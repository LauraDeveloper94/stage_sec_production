# -*- coding: utf -8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Supplier(models.Model):
    
    _name = 'stage_sec_production.supplier'
    _description = 'Supplier'
    
    name = fields.Char(string="Name", required=True, size=20)
    email = fields.Char(string="Email", required=True, size=100)
    surname1 = fields.Char(string ="First surname", required=True, size=20)
    surname2 = fields.Char(string = "Second surname", size=20)
    phone_number = fields.Char(string = "Phone number", size=15)
    type = fields.Selection(
        [('raw_material', 'Raw material'), ('finished_goods', 'Finished goods')],
        string="Type", required=True
    )
    address = fields.Char(string = "Address", required=True, size=100)

    _sql_constraints = [
    ('email_unique', 'unique(email)', 'The email must be unique.'),
    ]

    @api.constrains('email')
    def _check_email_format(self):
        email_validation = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for i in self:
            if i.email and not re.match(email_validation, i.email):
                raise ValidationError("The email format is invalid. Please enter a valid email address")

    @api.constrains('phone_number')
    def _check_phone_number_format(self):
        phone_validation = r'^\+?[0-9\s\-]+$'
        for i in self:
            if i.phone_number and not re.match(phone_validation, i.phone_number):
                raise ValidationError("The phone number format is invalid. Please enter a valid phone number")

    @api.constrains('name', 'surname1', 'surname2')
    def _check_just_letters_or_spaces(self):
        for i in self:
            for field in [i.name, i.surname1, i.surname2]:
                if field and not field.replace(" ", "").isalpha():
                    raise ValidationError("Names and surnames must only contain letters and spaces")

    @api.constrains('name', 'surname1', 'surname2', 'email')
    def check_duplicate_supplier(self):
        for i in self:
            check_criteria = [
                ('name', '=', i.name),
                ('surname1', '=', i.surname1),
                ('surname2', '=', i.surname2),
                ('email', '=', i.email),
                ('id', '!=', i.id),
            ]
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
    type = fields.Selection(
        [('wholesaler', 'Wholesaler'), ('retailer', 'Retailer')],
        string="Type", required=True
    )
    address = fields.Char(string="Address", required=True, size=100)

    _sql_constraints = [
    ('email_unique', 'unique(email)', 'The email must be unique.'),
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

    @api.constrains('name', 'surname1', 'surname2')
    def _check_just_letters_or_spaces(self):
        for i in self:
            for field in [i.name, i.surname1, i.surname2]:
                if field and not field.replace(" ", "").isalpha():
                    raise ValidationError("Names and surnames must only contain letters and spaces")

    @api.constrains('name', 'surname1', 'surname2', 'email')
    def check_duplicate_supplier(self):
        for i in self:
            check_criteria = [
                ('name', '=', i.name),
                ('surname1', '=', i.surname1),
                ('surname2', '=', i.surname2),
                ('email', '=', i.email),
                ('id', '!=', i.id),
            ]
            if self.env['stage_sec_production.supplier'].search(check_criteria):
                raise ValidationError("This supplier already exists")