# -*- coding: utf -8 -*-

from odoo import models, fields, api

class Employee(models.Model):
    
    _name = 'stage_sec_production.employee'
    _description = 'Employee'
    
    id_number = fields.Char(string="Identification number", required=True)
    name = fields.Char(string="Name", required=True, size=20)
    email = fields.Char(string="Email", required=True, size=100)
    surname1 = fields.Char(string = "First surname", required=True, size=20)
    surname2 = fields.Char(string = "Second surname", size=20)
    phone_number = fields.Char(string = "Phone number", size=15)
    type = fields.Selection(
        [('engineer', 'Engineer'), ('cutter', 'Cutter'), ('welder', 'Welder')],
        string="Type", required=True
    )
    address = fields.Char(string = "Address", required=True, size=100)
    position = fields.Char(string = "Employee position", required=True)

    section_id = fields.Many2one('stage_sec_production.section')
    production_order_ids = fields.Many2many('stage_sec_production.production_order', 'production_employee_rel', 'employee_id', 'production_order_id')
    manufacturing_process_ids = fields.One2many('stage_sec_production.manufacturing_process', 'employee_id')

