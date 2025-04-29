# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Quality_control(models.Model):
        
    _name = 'stage_sec_production.quality_control'
    _description = 'Quality control'
        
    date = fields.Date(string = "Date", required=True)
    status = fields.Char(string = "Status", required=True, size=200)   
    qc_report = fields.Char(string = "Report", size=200)
    retest_required = fields.Boolean(string = "Retest required", required=True)
    approved_quantity = fields.Integer(string = "Approved quantity", required=True)
    rejected_quantity = fields.Integer(string = "Rejected quantity", required=True)

    manufacturing_id = fields.Many2one('stage_sec_production.manufacturing')

    @api.constrains('approved_quantity')
    def _check_approved_quantity(self):
        for i in self:
            if i.approved_quantity < 0:
                raise ValidationError("The approved quantity cannot be negative.")
            
    @api.constrains('rejected_quantity')
    def _check_rejectedd_quantity(self):
        for i in self:
            if i.rejected_quantity < 0:
                raise ValidationError("The rejected quantity cannot be negative.")
            