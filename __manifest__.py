# Copyright 2022 <mj@ayudoo.bg>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    'author': 'Michael Jurke, Ayudoo Ltd',
    'name': 'Website Image Management',
    'version': '0.1',
    'summary': "Use extra media for shop and mouseover images",
    'description': """
        Use your extra media as main and mouseover images in your shop's product list.
    """,
    "license": "LGPL-3",
    "category": "Sales/Sales",
    'support': 'support@ayudoo.bg',
    'depends': [
        'base',
        'website_sale',
    ],
    'data': [
        'views/product_image_views.xml',
        'views/product_template_views.xml',
        'views/templates.xml',
    ],
    "assets": {
        "web.assets_frontend": [
            "website_image_management/static/src/scss/frontend.scss",
        ],
    },
}
