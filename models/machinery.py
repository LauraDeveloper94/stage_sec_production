# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests
import logging
_logger = logging.getLogger(__name__)


class Machinery(models.Model):
    
    _name = 'stage_sec_production.machinery'
    _description = 'Machinery'
    
    name = fields.Char(string = "Name", required=True, size=50)
    location = fields.Char(string = "Location", required=True, size=100)
    type = fields.Selection([
        ('cut', 'cut'),
        ('assembly', 'assembly'),
        ('welding', 'welding'),
        ('paint', 'paint')
    ], string="Tipo", required=True)
    product_qty = fields.Integer(string="Cantidad de producto")
    status = fields.Char(string = "Status", required=True, size=50) 
    installation_date = fields.Date(string = "Installation date", required=True)
    next_maintenance_date = fields.Date(string = "Next maintenance date", required=True)
    operational_hours = fields.Float(string = "Operational hours", required=True)
    maintenance_interval = fields.Float(string = "Maintenance interval", required=True)
    last_maintenance_date = fields.Date(string = "Last maintenance date", required=True)
    is_available = fields.Boolean(string="Available", default=True)

    production_order_ids = fields.Many2many('stage_sec_production.production_order', 'production_machinery_rel', 'machinery_id', 'production_order_id')
    manufacturing_process_ids = fields.One2many('stage_sec_production.manufacturing_process', 'machinery_id') 

    @api.constrains('last_maintenance_date', 'next_maintenance_date')
    def _check_maintenance_dates(self):
        for i in self: 
            if i.last_maintenance_date and i.next_maintenance_date:
                if i.last_maintenance_date > i.next_maintenance_date:
                    raise ValidationError("The last maintenance date must be earlier than the next maintenance date.")
                
            if i.installation_date and i.last_maintenance_date:
                if i.installation_date > i.last_maintenance_date:
                    raise ValidationError("The installation date must be earlier than the last maintenance date.")

    def action_get_machine_data(self):
        self.ensure_one()
        self.cron_get_all_machinery_data()
    
    def cron_get_all_machinery_data(self):

        machine_and_key = {
            "Assembly": "assembly",
            "Cutting Saw": "cutting",
            "Painter": "painting",
            "MIG Welder": "welding"
        }

        base_url = 'http://host.docker.internal:5000/machineryData/data'

        for machinery in self:
            machine_key = machine_and_key.get(machinery.name)
            if not machine_key:
                _logger.warning("No API key found for machinery name: %s", machinery.name)
                continue

            url = f'{base_url}/{machine_key}'

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    machinery.write({'product_qty': data['production']})
                else:
                    raise ValidationError(f"Failed to fetch data for {machinery.name}: {response.status_code}")
            except requests.exceptions.RequestException as e:
                raise ValidationError(f"Error connecting to API for {machinery.name}: {e}")
            