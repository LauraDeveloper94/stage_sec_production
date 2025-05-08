# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError 
from odoo.exceptions import UserError

class Production_order(models.Model):
    _name = 'stage_sec_production.production_order'
    _description = 'Production order'
    
    start_date = fields.Date(string="Start date", required=True)
    status = fields.Selection([
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished')
    ], string="Status", compute="_compute_status", store=True, default='not_started', required=True)
    end_date = fields.Date(string="End date", required=True)
    priority_level = fields.Char(string="Priority level", required=True, size=20)

    employee_ids = fields.Many2many('stage_sec_production.employee', 'production_employee_rel', 'production_order_id', 'employee_id')
    machinery_ids = fields.Many2many('stage_sec_production.machinery', 'production_machinery_rel', 'production_order_id', 'machinery_id')
    manufacturing_ids = fields.One2many('stage_sec_production.manufacturing', 'production_order_id')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for i in self:
            if i.start_date and i.end_date:
                if i.start_date > i.end_date:
                    raise ValidationError("The start date cannot be later than the end date.")
    
    def action_set_in_progress(self):
        print("Iniciación de producción")
        self.ensure_one() 
        self.status = 'in_progress'
        self.assign_resources()

    def assign_resources(self):
        phase_config = {
            'cutting': {'employee': ('cutter', 2), 'machine': ('cut', 1)},
            'assembling': {'employee': ('assembler', 2), 'machine': ('assembly', 1)},
            'welding': {'employee': ('welder', 1), 'machine': ('welding', 1)},
            'painting': {'employee': ('painter', 1), 'machine': ('paint', 1)},
        }

        for order in self:
            for m in order.manufacturing_ids:
                config = phase_config.get(m.phase)

                if config:
                    emp_type, emp_count = config['employee']
                    mach_type, mach_count = config['machine']

                    employee_domain = [('type', '=', emp_type), ('is_available', '=', True)]
                    machine_domain = [('type', '=', mach_type), ('is_available', '=', True)]

                    employees = self.env['stage_sec_production.employee'].search(employee_domain, limit=emp_count)
                    machines = self.env['stage_sec_production.machinery'].search(machine_domain, limit=mach_count)

                if len(employees) < emp_count:
                    raise UserError(
                        f"There are not enough available employees of type '{emp_type}'. "
                        f"Required: {emp_count}, available: {len(employees)}."
                    )

                if len(machines) < mach_count:
                    raise UserError(
                        f"There are not enough available machines of type '{mach_type}'. "
                        f"Required: {mach_count}, available: {len(machines)}."
                    )

                order.employee_ids |= employees
                employees.write({'is_available': False})

                order.machinery_ids |= machines
                machines.write({'is_available': False})

                m.status = 'in_progress'

    def action_finish_phase(self, phase):
        for order in self:
            for m in order.manufacturing_ids.filtered(lambda x: x.phase == phase):
                m.status = 'finished'
                self.release_resources(m)

            if all(m.status == 'finished' for m in order.manufacturing_ids.filtered(lambda x: x.phase == phase)):
                self._update_phase_status(phase)

            if all(m.status == 'finished' for m in order.manufacturing_ids):
                order.status = 'finished'

    def _update_phase_status(self, phase):
        phase_done = self.manufacturing_ids.filtered(lambda m: m.phase == phase)
        if all(m.status == 'finished' for m in phase_done):
            phase_done.write({'status': 'finished'})
        
    def release_resources(self, manufacturing_process):
        phase_config = {
            'cutting': {'employee': 'cutter', 'machine': 'cut'},
            'assembling': {'employee': 'assembler', 'machine': 'assembly'},
            'welding': {'employee': 'welder', 'machine': 'welding'},
            'painting': {'employee': 'painter', 'machine': 'paint'},
        }

        phase = manufacturing_process.phase
        config = phase_config.get(phase)

        if not config:
            return

        for order in self:
            employees = order.employee_ids.filtered(lambda e: e.type == config['employee'])
            machines = order.machinery_ids.filtered(lambda m: m.type == config['machine'])

            employees.write({'is_available': True})
            machines.write({'is_available': True})

            order.employee_ids -= employees
            order.machinery_ids -= machines