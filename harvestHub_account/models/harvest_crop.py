from odoo import models, Command


class harvestCrop(models.Model):
    _inherit = "harvest.crop"

    def action_sold(self):
        print("override action sold property called --------------------")
        moves = self.env["account.move"].create(
            {
                "partner_id": self.buyer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [
                    Command.create(
                        {
                            "name": "Administrative fees",
                            "quantity": 1,
                            "price_unit": 100.00,
                        }
                    ),
                ],
            }
        )
        return super().action_sold()
