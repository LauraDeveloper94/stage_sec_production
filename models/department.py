# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Department(models.Model):
    
    _name = 'stage_sec_production.department'
    _description = 'Department'
    
    name = fields.Char(string = "Name", required=True, size=30)
    location = fields.Char(string = "Location", required=True, size=50)
    description = fields.Char(string ="Description", required=True, size=200)
    number_employees = fields.Integer(string = "Number of employees", required=True)
    phone = fields.Char(string = "Phone", required=True, size=15)
    email = fields.Char(string = "Email", required=True, size=100)

    section_ids = fields.One2many('stage_sec_production.section', 'department_id')

    _sql_constraints = [
    ('email_unique', 'unique(email)', 'The email must be unique.'),
    ]

    @api.constrains('email')
    def _check_email_format(self):
        email_validation = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for i in self:
            if i.email and not re.match(email_validation, i.email):
                raise ValidationError("The email format is invalid. Please enter a valid email address")

    @api.constrains('phone')
    def _check_phone_number_format(self):
        phone_validation = r'^\+?[0-9\s\-\(\)]{7,15}$'
        for i in self:
            if i.phone and not re.match(phone_validation, i.phone):
                raise ValidationError("The phone number format is invalid. Please enter a valid phone number")
    

