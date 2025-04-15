# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Department(models.Model):
    
    _name = 'stage_sec_production.department'
    _description = 'Department'
    
    department_name = fields.Char(string = "Department name", required=True)
    department_location = fields.Char(string = "Location", required=True)
    department_description = fields.Char(string ="Department description", required=True)
    number_employees = fields.Char(string = "Number of employees", required=True)
    department_phone = fields.Integer(string = "Phone of department", required=True)
    department_email = fields.Char(string = "Department email", required=True)