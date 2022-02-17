from odoo import fields, models


class ProductImage(models.Model):
    _inherit = "product.image"

    main_image = fields.Boolean(
        string="Main Image",
        help=(
            "Show this image first in details view, and as product image in grid view"
            + " if activated."
        ),
        default=False,
    )
    mouseover_image = fields.Boolean(
        string="Mouseover Image",
        help="Show this image on mouse hover in list view.",
        default=False,
    )
    use_in_details_view = fields.Boolean(
        string="Use in details view",
        default=True,
    )
