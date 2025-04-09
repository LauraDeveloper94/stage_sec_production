# -*- coding: utf -8 -*-

class Employee(models.Model):
    
    _name = 'stage_sec.employee'
    _description = 'Employee'
    
    id_number = fields.Char(string="ID number", required=True)
    employee_name = fields.Char(string="Employee name", required=True)
    email = fields.Char(string="Email", required=True)
    surname1 = fields.Char(string = "First surname", required=True)
    surname2 = fields.Char(string = "Second surname")
    phone_number = fields.Char(string = "Phone number")
    employee_type = fields.Selection(
        [('factory_worker', 'Factory_worker'), ('engineer', 'Engineer')],
        string="Type of employee", required=True
    )
    employee_address = fields.Char(string = "Employee address", required=True)
    position = fields.Char(string = "Employee position", required=True)