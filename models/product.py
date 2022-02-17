from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_images(self):
        self.ensure_one()
        if self.website_use_main_extra_image:
            return list(
                self.product_variant_image_ids
            ) + self.product_tmpl_id._get_images(details_view=True)
        variant_images = list(self.product_variant_image_ids)
        if self.image_variant_1920:
            variant_images = [self] + variant_images
        else:
            variant_images = variant_images + [self]
        return variant_images + self.product_tmpl_id._get_images(details_view=True)[1:]

    def _compute_image_1920(self):
        for record in self:
            if record.image_variant_1920:
                record.image_1920 = record.image_variant_1920
            elif record.product_tmpl_id.website_use_main_extra_image:
                if not record.product_tmpl_id.website_product_image_id:
                    record.product_tmpl_id._compute_website_product_image_id()
                if record.product_tmpl_id.website_product_image_id:
                    record.image_1920 = (
                        record.product_tmpl_id.website_product_image_id.image_1920
                    )
            else:
                record.image_1920 = record.product_tmpl_id.image_1920

    def _compute_image_1024(self):
        for record in self:
            if record.image_variant_1024:
                record.image_1024 = record.image_variant_1024
            elif record.product_tmpl_id.website_use_main_extra_image:
                if not record.product_tmpl_id.website_product_image_id:
                    record.product_tmpl_id._compute_website_product_image_id()
                if record.product_tmpl_id.website_product_image_id:
                    record.image_1024 = (
                        record.product_tmpl_id.website_product_image_id.image_1024
                    )
            else:
                record.image_1024 = record.product_tmpl_id.image_1024

    def _compute_image_512(self):
        for record in self:
            if record.image_variant_512:
                record.image_512 = record.image_variant_512
            elif record.product_tmpl_id.website_use_main_extra_image:
                if not record.product_tmpl_id.website_product_image_id:
                    record.product_tmpl_id._compute_website_product_image_id()
                if record.product_tmpl_id.website_product_image_id:
                    record.image_512 = (
                        record.product_tmpl_id.website_product_image_id.image_512
                    )
            else:
                record.image_512 = record.product_tmpl_id.image_512

    def _compute_image_256(self):
        for record in self:
            if record.image_variant_256:
                record.image_256 = record.image_variant_256
            elif record.product_tmpl_id.website_use_main_extra_image:
                if not record.product_tmpl_id.website_product_image_id:
                    record.product_tmpl_id._compute_website_product_image_id()
                if record.product_tmpl_id.website_product_image_id:
                    record.image_256 = (
                        record.product_tmpl_id.website_product_image_id.image_256
                    )
            else:
                record.image_256 = record.product_tmpl_id.image_256

    def _compute_image_128(self):
        for record in self:
            if record.image_variant_128:
                record.image_128 = record.image_variant_128
            elif record.product_tmpl_id.website_use_main_extra_image:
                if not record.product_tmpl_id.website_product_image_id:
                    record.product_tmpl_id._compute_website_product_image_id()
                if record.product_tmpl_id.website_product_image_id:
                    record.image_128 = (
                        record.product_tmpl_id.website_product_image_id.image_128
                    )
            else:
                record.image_128 = record.product_tmpl_id.image_128

    def _compute_can_image_1024_be_zoomed(self):
        for record in self:
            record.can_image_1024_be_zoomed = (
                record.can_image_variant_1024_be_zoomed
                if record.image_variant_1920
                else record.product_tmpl_id.can_image_1024_be_zoomed
            )
