# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Machinery(models.Model):
    
    _name = 'stage_sec_production.machinery'
    _description = 'Machinery'
    
    name = fields.Char(string = "Name", required=True, size=50)
    location = fields.Char(string = "Location", required=True, size=100)
    type = fields.Char(string= "Type", required=True)
    status = fields.Char(string = "Status", required=True, size=50) 
    installation_date = fields.Date(string = "Installation date", required=True)
    maintenance_date = fields.Date(string = "Maintenance date", required=True)
    operational_hours = fields.Float(string = "Operational hours", required=True)
    maintenance_interval = fields.Float(string = "Maintenance interval", required=True)
    last_maintenance_date = fields.Date(string = "Last maintenance date", required=True)