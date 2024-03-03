from odoo import models, fields


class harvestProcess(models.Model):
    _name = "harvest.process"
    _description = "crop's process records"
    _inherit = "mail.thread"

    name = fields.Char(string="Task Of Processes", required=True, tracking=True)
    description = fields.Char(string="description", required=True, tracking=True)
    category = fields.Selection(
        [
            ("Preparation", "Preparation"),
            ("Planting", "Planting"),
            ("Growing", "Growing"),
            ("Harvesting", "Harvesting"),
            ("Post-Harvest", "Post-Harvest"),

        ],
        string="Category",
        tracking=True,
    )
    crop_id = fields.Many2one("harvest.crop", required=True)

    def action_done(self):
        for record in self:
            category = record._context.get("default_category")
            if category:
                record.category = category
                record.crop_id.state = category
        return True
      