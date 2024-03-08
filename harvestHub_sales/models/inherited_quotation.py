from odoo import models,fields,_


class Quotation(models.Model):
    _inherit = "sale.order"


    farmer_id = fields.Many2one("harvest.farmer", string="Farmer", tracking=True)

    def action_create_crop_request(self):
        harvest_crop_order_obj = self.env["harvest.crop.order"]
        for order in self:
            crop_order_vals = {
                "ref": _("New"),
                "state": "new",
                "farmer_id":order.farmer_id.id,
                "buyer_id":order.partner_id.id,
                "quantity":order.order_line[0].product_uom_qty,
                "price":order.order_line[0].price_total,
                "product_id":order.order_line[0].product_template_id.id,
            }
            harvest_crop_order_obj.create(crop_order_vals)
        return True
        
