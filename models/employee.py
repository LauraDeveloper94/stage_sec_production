# -*- coding: utf -8 -*-

from odoo import models, fields, api

class Employee(models.Model):
    
    _name = 'stage_sec_production.employee'
    _description = 'Employee'
    
    id_number = fields.Char(string="ID", required=True)
    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    surname1 = fields.Char(string = "First surname", required=True)
    surname2 = fields.Char(string = "Second surname")
    phone_number = fields.Char(string = "Phone number")
    type = fields.Selection(
        [('factory_worker', 'Factory_worker'), ('engineer', 'Engineer')],
        string="Type", required=True
    )
    address = fields.Char(string = "Address", required=True)
    position = fields.Char(string = "Position", required=True)