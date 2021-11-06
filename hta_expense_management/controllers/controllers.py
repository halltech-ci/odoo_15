# -*- coding: utf-8 -*-
# from odoo import http


# class HtaExpenseManagement(http.Controller):
#     @http.route('/hta_expense_management/hta_expense_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_expense_management/hta_expense_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_expense_management.listing', {
#             'root': '/hta_expense_management/hta_expense_management',
#             'objects': http.request.env['hta_expense_management.hta_expense_management'].search([]),
#         })

#     @http.route('/hta_expense_management/hta_expense_management/objects/<model("hta_expense_management.hta_expense_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_expense_management.object', {
#             'object': obj
#         })
