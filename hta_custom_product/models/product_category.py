# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = "product.category"
    
    """def get_default_related_code(self):
        if self.parent_id:
            code = self.env['product.category'].search([('id', '=', self.parent_id.id)])
        else:
            code = 0
        return code
    """    
    
    category_code = fields.Char()
    related_code = fields.Char(string='Related Code', compute = '_compute_related_code', store=True, recursive=True)
    
    @api.depends('parent_id.related_code', 'category_code')
    def _compute_related_code(self):
        for categ in self:
            if categ.parent_id:
                categ.related_code = str(self.parent_id.related_code) + '-' + str(self.category_code)
            else:
                categ.related_code = str(self.category_code)
    
    @api.onchange('parent_id')
    def onchange_parent_id(self):
        self.related_code = str(self.parent_id.related_code) + '-' + str(self.category_code) 
        
    