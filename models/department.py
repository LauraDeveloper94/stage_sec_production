# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Department(models.Model):
    
    _name = 'stage_sec_production.department'
    _description = 'Department'
    
    name = fields.Char(string = "Name", required=True, size=30)
    location = fields.Char(string = "Location", required=True, size=50)
    description = fields.Char(string ="Description", required=True, size=200)
    number_employees = fields.Integer(string = "Number of employees", required=True)
    phone = fields.Char(string = "Phone", required=True, size=15)
    email = fields.Char(string = "Email", required=True, size=100)