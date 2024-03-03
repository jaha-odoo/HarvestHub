from odoo import api, models, fields, _
from odoo.exceptions import UserError


class harvestCrop(models.Model):
    _name = "harvest.crop"
    _description = "farm's crop records"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", required=True, tracking=True)
    season = fields.Selection(
        [("winter", "Winter"), ("summer", "Summer"), ("monsoon", "Monsoon")],
        string="Season",
        tracking=True,
    )
    state = fields.Selection(
        [
            ("Preparation", "Preparation"),
            ("Planting", "Planting"),
            ("Growing", "Growing"),
            ("Harvesting", "Harvesting"),
            ("Post-Harvest", "Post-Harvest"),
            ("Sold", "Sold"),
        ],
        string="State",
        tracking=True,
    )
    description = fields.Char(string="Description", tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _("New"))
    disease_ids = fields.One2many("harvest.disease", "crop_id")
    process_ids = fields.One2many("harvest.process", "crop_id")
    buyer_id = fields.Many2one("res.partner", copy=False, string="Buyer")
    farmer_id = fields.Many2one("harvesthub.farmers", string="Farmer", tracking=True)
    location_id = fields.Many2one("harvest.locations", string="Location", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # if we want to make modification do here
            vals["ref"] = self.env["ir.sequence"].next_by_code("harvest.crop")
        return super(harvestCrop, self).create(vals_list)

    def action_sold(self):
        for rec in self:
            if rec.state != "Post-Harvest":
                raise UserError("Only post-Harvest crops can be sold")
            else:
                rec.state = "Sold"
        return True
