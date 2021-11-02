# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrContract(models.Model):
    _inherit = "hr.contract"
    
    loan_account = fields.Many2one('account.account', 'Loan Account', company_dependent=True, domain=[('deprecated', '=', False)])
    advance_account = fields.Many2one('account.account', 'Advance Account', company_dependent=True, domain=[('deprecated', '=', False)])