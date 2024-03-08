from odoo import api, models, fields, _


class HarvestCropOrder(models.Model):
    _name = "harvest.crop.order"
    _description = "crop's order records"
    _inherit = "mail.thread"

    ref = fields.Char(string="Reference", default=lambda self: _("New"))
    quantity = fields.Float(string="Estimated Quantity(kg)", tracking=True)
    price=fields.Integer(string="Price",tracking=True)
    start_date = fields.Date(string="Start Date", tracking=True)
    end_date = fields.Date(string="End Date", tracking=True)
    buyer_id = fields.Many2one("res.partner", copy=False, string="Buyer")
    farmer_id = fields.Many2one("harvest.farmer", string="Farmer", tracking=True)
    product_id = fields.Many2one('product.product', string='Agriculture Crop',tracking=True)

    state = fields.Selection(
        [
            ("new", "New"),
            ("confirmed", "Confirmed"),
            ("process", "In Process"),
            ("done", "Done"),
        ],
        string="State",
        default="new",
        tracking=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # if we want to make modification do here
            vals["ref"] = self.env["ir.sequence"].next_by_code("harvest.crop.order")
        return super(HarvestCropOrder, self).create(vals_list)

    def action_crop_order_confirmed(self):
        for rec in self:
            rec.state = "confirmed"
        return True

    def action_crop_order_process(self):
        for rec in self:
            rec.state = "process"
        return True

    def action_crop_order_done(self):
        for rec in self:
            rec.state = "done"
        return True
