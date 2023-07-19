from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    cancelled_order_message = fields.Char(
        related="company_id.cancelled_order_message", readonly=False
    )
