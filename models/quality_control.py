# -*- coding: utf -8 -*-
from odoo import models, fields, api

class Quality_control(models.Model):
        
    _name = 'stage_sec_production.quality_control'
    _description = 'Quality control'
        
    control_date = fields.Date(string = "Control date", required=True)
    status = fields.Char(string = "Status", required=True)   
    qc_report = fields.Char(string = "Report")
    retest_required = fields.Boolean(string = "Retest required", required=True)
    approved_quantity = fields.Integer(string = "Approved quantity", required=True)
    rejected_quantity = fields.Integer(string = "Rejected quantity", required=True)