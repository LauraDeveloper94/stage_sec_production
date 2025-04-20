# -*- coding: utf -8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Supplier(models.Model):
    
    _name = 'stage_sec_production.supplier'
    _inherit = 'stage_sec_production.business_entities' 
    _description = 'Supplier'
    
    type = fields.Selection(
        [('raw_material', 'Raw material'), ('finished_goods', 'Finished goods')],
        string="Type", required=True
    )

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'The email must be unique.')
    ]