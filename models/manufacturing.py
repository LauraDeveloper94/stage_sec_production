# -*- coding: utf -8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Manufacturing(models.Model):
    
    _name = 'stage_sec_production.manufacturing'
    _description = 'Manufacturing'
    
    quantity = fields.Integer(string="Quantity", required=True)
    phase = fields.Char(string="Phase", required=True)
    start_date = fields.Date(string = "Start date", required=True)
    end_date = fields.Date(string = "End date", required=True)

    production_order_ids = fields.Many2many('stage_sec_production.production_order', 'production_manufacturing_rel', 'manufacturing_id', 'production_order_id')
    material_ids = fields.Many2many('stage_sec_production.material', 'manufacturing_material_rel', 'manufacturing_id', 'material_id')
    quality_control_ids = fields.One2many('stage_sec_production.quality_control', 'manufacturing_id')
    inventory_id = fields.Many2one('stage_sec_production.inventory')
    product_id = fields.Many2one('stage_sec_production.product', compute='_compute_product', inverse='_inverse_product') #1:1 con producto
    manufacturing_process_ids = fields.One2many('stage_sec_production.manufacturing_process', 'manufacturing_id')
    
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