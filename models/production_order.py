# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError 
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class Production_order(models.Model):
    _name = 'stage_sec_production.production_order'
    _description = 'Production order'
    
    start_date = fields.Datetime(string="Start date")
    status = fields.Selection([
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished')
    ], string="Status", compute="_compute_status", store=True, default='not_started', required=True)
    end_date = fields.Datetime(string="End date")
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
        self.start_date = fields.Datetime.now() 
        self.status = 'in_progress'
        self.assign_resources()

    def action_advance_phase(self):
        self.ensure_one()
        self.advance_phase()

    def assign_resources(self):       
        phase_config = {
            'cutting': {'employee': ('cutter', 2), 'machinery': ('cut', 1)},
            'assembling': {'employee': ('assembler', 2), 'machinery': ('assembly', 1)},
            'welding': {'employee': ('welder', 1), 'machinery': ('welding', 1)},
            'painting': {'employee': ('painter', 1), 'machinery': ('paint', 1)},
        }

        manufacturing = self.env['stage_sec_production.manufacturing'].search([
        ('phase', '=', 'not_assigned'),
        ('production_order_id', '=', False)
        ], limit=1)

        if not manufacturing:
            raise UserError("No manufacturing orders with phase 'not assigned' available")

        manufacturing.production_order_id = self.id
        manufacturing.phase = 'cutting'
        self.manufacturing_ids |= manufacturing

        config = phase_config['cutting']
        emp_type, emp_count = config['employee']
        mach_type, mach_count = config['machinery']

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

        self.employee_ids |= employees
        employees.write({'is_available': False})

        self.machinery_ids |= machines
        machines.write({'is_available': False})

        self.status = 'in_progress'

    def advance_phase(self):
        phase_sequence = ['cutting', 'assembling', 'welding', 'painting']
        phase_config = {
            'cutting': {'employee': ('cutter', 2), 'machinery': ('cut', 1)},
            'assembling': {'employee': ('assembler', 2), 'machinery': ('assembly', 1)},
            'welding': {'employee': ('welder', 1), 'machinery': ('welding', 1)},
            'painting': {'employee': ('painter', 1), 'machinery': ('paint', 1)},
        }

        for manufacturing in self.manufacturing_ids:
            if manufacturing.phase == 'not_assigned':
                continue  

            current_phase = manufacturing.phase
            try:
                current_index = phase_sequence.index(current_phase)
            except ValueError:
                continue 

            emp_type, _ = phase_config[current_phase]['employee']
            mach_type, _ = phase_config[current_phase]['machinery']

            for employee in self.employee_ids.filtered(lambda e: e.type == emp_type):
                employee.is_available = True
                self.employee_ids -= employee

            for machine in self.machinery_ids.filtered(lambda m: m.type == mach_type):
                machine.is_available = True
                self.machinery_ids -= machine

            if current_index + 1 < len(phase_sequence):
                next_phase = phase_sequence[current_index + 1]
                manufacturing.phase = next_phase
                manufacturing.start_date = fields.Datetime.today()
                manufacturing.status = 'in_progress'

                emp_type, emp_count = phase_config[next_phase]['employee']
                mach_type, mach_count = phase_config[next_phase]['machinery']

                employees = self.env['stage_sec_production.employee'].search([
                    ('type', '=', emp_type),
                    ('is_available', '=', True)
                ], limit=emp_count)

                machines = self.env['stage_sec_production.machinery'].search([
                    ('type', '=', mach_type),
                    ('is_available', '=', True)
                ], limit=mach_count)

                if len(employees) < emp_count or len(machines) < mach_count:
                    raise UserError(f"No hay suficientes recursos disponibles para la fase '{next_phase}'.")

                employees.write({'is_available': False})
                machines.write({'is_available': False})
                self.employee_ids |= employees
                self.machinery_ids |= machines
            else:               
                manufacturing.status = 'finished'

            if all(m.status == 'finished' for m in self.manufacturing_ids):
                self.status = 'finished'
                self.end_date = fields.Datetime.now()
    
    #Libero los empleados y maquinaria y vuelvo el manufacturado a su estado inicial cuando borro una orden de producción
    def unlink(self):
        for production_order in self:
            if production_order.employee_ids:
                production_order.employee_ids.write({'is_available': True})
            if production_order.machinery_ids:
                production_order.machinery_ids.write({'is_available': True})
            if production_order.manufacturing_ids:
                production_order.manufacturing_ids.write({
                'phase': 'not_assigned',
                'production_order_id': False,
                'status': 'pending',
                'start_date': False,
                'end_date': False
            })
    
        return super(Production_order, self).unlink()
    