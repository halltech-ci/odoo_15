# -*- coding: utf-8 -*-

from odoo import SUPERUSER_ID, api

def pre_init_product_category_code(cr):
    """
    This post-init-hook will update all existing category assigning them the
    corresponding default category_code.
    """
    
    cr.execute("ALTER TABLE product_category " "ADD COLUMN category_code character varying;")
    cr.execute("UPDATE product_category " "SET category_code = id;")
    
def post_init_product_category_code(cr, registry):
    """
    This post-init-hook will update all existing task assigning them the
    corresponding sequence code.
    """
    env = api.Environment(cr, SUPERUSER_ID, dict())
    category_obj = env["product.category"]
    sequence_obj = env["ir.sequence"]
    categories = env["product.category"].search([], order="id")
    for category_id in categories.ids:
        cr.execute(
            "UPDATE product_category " "SET category_code = %s " "WHERE id = %s;",
            (sequence_obj.next_by_code("product.category.code"), category_id),
        )