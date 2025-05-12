# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests
import logging

_logger = logging.getLogger(__name__)

class Manufacturing(models.Model):
    
    _name = 'stage_sec_production.manufacturing'
    _description = 'Manufacturing'
    
    name = fields.Char(string="Name", required=True)
    reference = fields.Integer(string="Reference", required=True)
    phase = fields.Selection([
        ('not_assigned', 'not assigned'),
        ('cutting', 'cutting'),
        ('assembling', 'assembling'),
        ('welding', 'welding'),
        ('painting', 'painting'),
    ], string="Phase", required=True)
    start_date = fields.Date(string = "Start date")
    end_date = fields.Date(string = "End date")
    status = fields.Selection([
        ('pending', 'pending'),
        ('in_progress', 'in progress'),
        ('finished', 'finished')
    ], default='pending')

    production_order_id = fields.Many2one('stage_sec_production.production_order')
    material_ids = fields.Many2many('stage_sec_production.material', 'manufacturing_material_rel', 'manufacturing_id', 'material_id')
    quality_control_ids = fields.One2many('stage_sec_production.quality_control', 'manufacturing_id')
    inventory_id = fields.Many2one('stage_sec_production.inventory')
    product_id = fields.Many2one('stage_sec_production.product', compute='_compute_product', inverse='_inverse_product') 
    manufacturing_process_ids = fields.One2many('stage_sec_production.manufacturing_process', 'manufacturing_id')

    _sql_constraints = [
        ('unique_reference', 'unique(reference)', 'The reference must be unique.')
    ]
    
    def _compute_product(self):
        for rec in self:
            rec.product_id = self.env['stage_sec_production.product'].search([('manufacturing_ref_id', '=', rec.id)], limit=1)
            
    def _inverse_product(self):
        for rec in self:
            rec.product_id.manufacturing_ref_id = rec

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for i in self:
            if i.start_date and i.end_date:
                if i.start_date > i.end_date:
                    raise ValidationError("The start date cannot be later than the end date.")
    
    @api.constrains('quantity')
    def _check_quantity(self):
        for i in self:
            if i.quantity < 0:
                raise ValidationError("Quantity cannot be negative.")
            
    def cron_get_all_machinery_data(self):
        machinery_types = ["cut", "assembly", "welding", "paint"]
        for m_type in machinery_types:
            try:
                url = f"http://localhost:5000/machineryData/{m_type}"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    _logger.info("Received data for '%s': %s", m_type, data)
                else:
                    _logger.error("Error from obtaining data from '%s': %s", m_type, response.status_code)
            except Exception as e:
                _logger.exception("Error from obtaining data from '%s': %s", m_type, e)
    