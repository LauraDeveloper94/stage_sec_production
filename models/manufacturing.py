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