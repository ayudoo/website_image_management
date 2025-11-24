Website Image Management
========================

.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

**This is the Odoo 18 branch.**

Configure your shop list main images by product eCommerce extra media, add mouseover
images and decide, which images are to be show in the product's detail view.


**Table of contents**

.. contents::
   :local:


Usage
-----

This app allows for the odoo default behavior, where the product image
in the admin backend corresponds to the image in the shop page, but also, to customize
this.

Open the product template form, switch to the `eCommerce` tab. In the `List View Images`
section, check ``Use Extra Media``. Now, add your images as `Extra Product Media` and
decide whether it is a ``Main Image``, a ``Mouseover Image`` and its
``Use in details view``.


Overview over all Product Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For convenience, there is a new menu in the `Sales` app, `Products` -> `Extra Media`.
There you find all the extra media you added.


Limitations
^^^^^^^^^^^

Note, that after changing the ``Main Image`` of the product template, the product
variants form will show this one instead of the default product template image. This
has no effect on the shop view and you can still set an explicit variant image. However,
if you have a use case that conflicts with this display peculiarity, please let us know.


Bug Tracker
-----------

Bugs are tracked on `GitHub Issues <https://github.com/ayudoo/website_image_management>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ayudoo/website_image_management/issues/new**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
-------

Authors
^^^^^^^

* Michael Jurke
* Ayudoo Ltd <support@ayudoo.bg>
