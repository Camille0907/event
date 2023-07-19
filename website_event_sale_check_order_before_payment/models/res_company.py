# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    cancelled_order_message = fields.Char(
        help="Message displayed, if order is cancel before the payment process.",
        default="Your order has been cancelled, before the payment processed. Please "
        "go back to our event page to register again.",
        translate=True,
    )
