# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Department(models.Model):
    
    _name = 'stage_sec_production.department'
    _description = 'Department'
    
    name = fields.Char(string = "Department name", required=True)
    location = fields.Char(string = "Location", required=True)
    description = fields.Char(string ="Department description", required=True)
    number_employees = fields.Char(string = "Number of employees", required=True)
    phone = fields.Integer(string = "Phone of department", required=True)
    email = fields.Char(string = "Department email", required=True)