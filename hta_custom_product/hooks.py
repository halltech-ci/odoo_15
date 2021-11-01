# -*- coding: utf-8 -*-

def pre_init_hook(cr, registry):
    """
    This post-init-hook will update all existing category assigning them the
    corresponding default category_code.
    """
    env = api.Environment(cr, SUPERUSER_ID, dict())
    category_obj = env["product.category"]
    categories = category_obj.search([], order="id")
    for category_id in categories.ids:
        cr.execute(
            "UPDATE product_category SET category_code = %s WHERE id = %s;", (category_id, category_id,),
        )