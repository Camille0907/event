import logging

from odoo import _, http
from odoo.http import request

import odoo.addons.website_sale.controllers.main as website_sale

_logger = logging.getLogger(__name__)


class WebsiteSale(website_sale.WebsiteSale):
    @http.route(
        ["/shop/check_before_payment"], type="json", auth="public", website=True
    )
    def check_before_payment(self):
        order = request.website.sale_get_order()
        if order:
            if order.state == "cancel":
                return {
                    "valid": False,
                    "message": request.env.company.cancelled_order_message,
                }
        return {"valid": True}
