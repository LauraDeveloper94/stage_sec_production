# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Client(models.Model):
    _name = 'stage_sec_production.client'
    _inherit = 'stage_sec_production.business_entities' 
    _description = 'Client'
    
    type = fields.Selection(
        [('wholesaler', 'Wholesaler'), ('retailer', 'Retailer')],
        string="Type", required=True
    )

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'The email must be unique.')
    ]

order_ids = fields.One2many('stage_sec_production.order', 'client_id') 