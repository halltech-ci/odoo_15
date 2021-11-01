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
    related_code = fields.Char(string='Related Code', compute = '_compute_related_code', recursive=True,)
    
    @api.depends('parent_id.related_code', 'category_code')
    def _compute_related_code(self):
        for category in self:
            if category.parent_id:
                category.related_code = '%s-%s' % (category.parent_id.related_code, category.category_code)
            else:
                category.related_code = str(category.category_code)
    
    @api.onchange('parent_id')
    def onchange_parent_id(self):
        for category in self:
            category.related_code = '%s-%s' % (category.parent_id.related_code, category.category_code)
        
    @api.onchange('category_code')
    def onchange_category_code(self):
        for category in self:
            category.related_code = '%s-%s' % (category.parent_id.related_code, category.category_code)