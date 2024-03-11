from odoo import api, models, fields, _
from odoo.exceptions import UserError


class HarvestCrop(models.Model):
    _name = "harvest.crop"
    _description = "farm's crop records"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", required=True, tracking=True)
    state = fields.Selection(
        [
            ("preparation", "Preparation"),
            ("planting", "Planting"),
            ("growing", "Growing"),
            ("harvesting", "Harvesting"),
            ("post_harvest", "Post Harvest"),
            ("sold", "Sold"),
        ],
        string="State",
        tracking=True,
    )
    price=fields.Integer(string="Unit Price",tracking=True)
    description = fields.Char(string="Description", tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _("New"))
    quantity = fields.Float(string="Quantity(kg)", tracking=True)
    disease_ids = fields.One2many("harvest.disease", "crop_id")
    process_ids = fields.One2many("harvest.process", "crop_id")
    buyer_id = fields.Many2one("res.partner", copy=False, string="Buyer")
    farmer_id = fields.Many2one("harvest.farmer", string="Farmer", tracking=True)
    location_id = fields.Many2one("harvest.location", string="Location", tracking=True)
    warehouse_id=fields.Many2one("stock.warehouse",string="Crop Warehouse",tracking=True)
    product_id = fields.Many2one('product.product', string='Agriculture Crop',tracking=True)
    material_id=fields.Many2many("product.product",string="Raw Material",tracking=True)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # if we want to make modification do here
            vals["ref"] = self.env["ir.sequence"].next_by_code("harvest.crop")
        return super(HarvestCrop, self).create(vals_list)

    def action_crop_sold(self):
        for rec in self:
            if rec.state != "post_harvest":
                raise UserError("Only post_harvest crops can be sold")
            else:
                rec.state = "sold"
        return True
