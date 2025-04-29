# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Manufacturing_process(models.Model):
        
    _name = 'stage_sec_production.manufacturing_process'
    _description = 'Manufacturing process'
        
    start_date = fields.Date(string = "Start date", required=True)
    end_date = fields.Date(string = "End date", required=True)
    notes = fields.Char(string = "Manufacturing process notes")

    manufacturing_id = fields.Many2one('stage_sec_production.manufacturing')
    machinery_id = fields.Many2one('stage_sec_production.machinery')
    employee_id = fields.Many2one('stage_sec_production.employee')
    