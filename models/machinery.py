# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Machinery(models.Model):
    
    _name = 'stage_sec.machinery'
    _description = 'Machinery'
    
	machinery_name = fields.Char(string= "Machinery name", required=True)
    machinery_location = fields.Char(string = "Machinery location", required=True)
    machinery_type = fields.Char(string= "Machinery type", required=True)
    machinery_status = fields.Char(string = "Machinery status", required=True) 
    installation_date = fields.Date(string = "Installation date", required=True)
    maintenance_date = fields.Date(string = "Maintenance date", required=True)
    operational_hours = fields.Float(string = "Operational hours", required=True)
    maintenance_interval = fields.Float(string = "Maintenance interval", required=True)
    last_maintenance_date = fields.Date(string = "Last maintenance date", required=True)