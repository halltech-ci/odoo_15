# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ExpenseRequest(models.Model):
    _name = 'expense.request'
    _description = 'Custom expense request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc'
    
    
    @api.model
    def _default_employee_id(self):
        return self.env.user.employee_id
    
    @api.model
    def _get_default_requested_by(self):
        return self.env['res.users'].browse(self.env.uid)
    
    def _get_default_name(self):
        return self.env["ir.sequence"].next_by_code("expense.request.code")

    name = fields.Char(default=_get_default_name, readonly=True)
    description = fields.Char('Description', required=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('validate', 'Validate'),
        ('to_approve', 'To Approve'),
        ('approve', 'Approved'),
        ('post', 'Paid'),
        ('refuse', 'Refused'),
        ('cancel', 'Cancelled')
    ], string='Status', index=True, readonly=True, tracking=True, copy=False, default='draft', required=True, help='Expense Report State')
  