# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Supplier(models.Model):
    
    _name = 'stage_sec_production.supplier'
    _description = 'Supplier'
    
    supplier_name = fields.Char(string="Supplier name", required=True)
    email = fields.Char(string="Email", required=True)
    surname1 = fields.Char(string ="First surname", required=True)
    surname2 = fields.Char(string = "Second surname")
    phone_number = fields.Char(string = "Phone number")
    supplier_type = fields.Selection(
        [('raw_material', 'Raw_material'), ('finished_goods', 'Finished_goods')],
        string="Type of supplier", required=True
    )
    supplier_address = fields.Char(string = "Supplier address", required=True)