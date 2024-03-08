from odoo import models, Command


class harvestCrop(models.Model):
    _inherit = "harvest.crop"

    def action_crop_sold(self):
        print("override action sold property called --------------------")
        moves = self.env["account.move"].create(
            {
                "partner_id": self.buyer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [
                    Command.create(
                        {
                            "name": self.name,
                            "quantity":self.quantity,
                            "price_unit":self.price
                        }
                    ),
                ],
            }
        )
        return super().action_crop_sold()
