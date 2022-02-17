from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    website_use_main_extra_image = fields.Boolean(
        string="Use extra media as shop image",
        help="Use the extra media instead of the product image in the website."
        + " Mark the checkbox 'Main image' of the desired extra media attachment.",
        default=False,
    )

    @api.depends("website_use_main_extra_image", "product_template_image_ids")
    def _compute_website_image_ids(self):
        for record in self:
            main_image = False
            mouseover_image = False
            if record.website_use_main_extra_image:
                for pti in record.product_template_image_ids:
                    if not main_image and pti.main_image:
                        main_image = pti
                    if not mouseover_image and pti.mouseover_image:
                        mouseover_image = pti
                    if main_image and mouseover_image:
                        break

            if main_image:
                record.website_product_image_id = main_image[0]
            else:
                record.website_product_image_id = False
            if mouseover_image:
                record.website_mouseover_image_id = mouseover_image[0]
            else:
                record.website_mouseover_image_id = False

    website_product_image_id = fields.One2many(
        "product.image", string="Main Image", compute=_compute_website_image_ids
    )

    website_mouseover_image_id = fields.One2many(
        "product.image", string="Mouseover Image", compute=_compute_website_image_ids
    )

    def _get_images(self, details_view=False):
        self.ensure_one()
        if details_view:
            images = list(
                self.product_template_image_ids.filtered(
                    lambda pti: pti.use_in_details_view
                )
            )
        else:
            images = list(self.product_template_image_ids)

        if self.website_use_main_extra_image:
            return images
        else:
            return [self] + images

    def _get_image_holder(self):
        self.ensure_one()
        if self.website_use_main_extra_image and self.website_product_image_id:
            return self.website_product_image_id
        if not isinstance(self.id, models.NewId):
            return super()._get_image_holder()
        return None
