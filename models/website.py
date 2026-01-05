from odoo import api, fields, models


class Website(models.Model):
    _inherit = "website"

    @api.model
    def image_url(self, record, field, size=None):
        if record._name == "product.template":
            record = record.sudo().website_product_image_id
        return super().image_url(record, field, size=size)
