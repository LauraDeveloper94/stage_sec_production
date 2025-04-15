# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Department(models.Model):
    
    _name = 'stage_sec_production.department'
    _description = 'Department'
    
    name = fields.Char(string = "Name", required=True)
    location = fields.Char(string = "Location", required=True)
    description = fields.Char(string ="Description", required=True)
    number_employees = fields.Char(string = "Number of employees", required=True)
    phone = fields.Integer(string = "Phone", required=True)
    email = fields.Char(string = "Email", required=True)