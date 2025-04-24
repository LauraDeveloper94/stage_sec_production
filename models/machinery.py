# -*- coding: utf -8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Machinery(models.Model):
    
    _name = 'stage_sec_production.machinery'
    _description = 'Machinery'
    
    name = fields.Char(string = "Name", required=True, size=50)
    location = fields.Char(string = "Location", required=True, size=100)
    type = fields.Char(string= "Type", required=True)
    status = fields.Char(string = "Status", required=True, size=50) 
    installation_date = fields.Date(string = "Installation date", required=True)
    next_maintenance_date = fields.Date(string = "Next maintenance date", required=True)
    operational_hours = fields.Float(string = "Operational hours", required=True)
    maintenance_interval = fields.Float(string = "Maintenance interval", required=True)
    last_maintenance_date = fields.Date(string = "Last maintenance date", required=True)

    production_order_ids = fields.Many2many('stage_sec_production.production_order', 'production_machinery_rel', 'machinery_id', 'production_order_id') 

    @api.constrains('last_maintenance_date', 'next_maintenance_date')

    def _check_maintenance_dates(self):
        for i in self: 
            if i.last_maintenance_date and i.next_maintenance_date:
                if i.last_maintenance_date > i.next_maintenance_date:
                    raise ValidationError("The last maintenance date must be earlier than the next maintenance date.")
                
            if i.installation_date and i.last_maintenance_date:
                if i.installation_date > i.last_maintenance_date:
                    raise ValidationError("The installation date must be earlier than the last maintenance date.")
