from odoo import models, fields


class HarvestProcess(models.Model):
    _name = "harvest.process"
    _description = "crop's process records"
    _inherit = "mail.thread"

    name = fields.Char(string="Task Of Processes", required=True, tracking=True)
    description = fields.Char(string="description", required=True, tracking=True)
    category = fields.Selection(
        [
            ("preparation", "Preparation"),
            ("planting", "Planting"),
            ("growing", "Growing"),
            ("harvesting", "Harvesting"),
            ("post_harvest", "Post Harvest"),
            ("sold","sold")
        ],
        string="Category",
        tracking=True,
    )
    crop_id = fields.Many2one("harvest.crop", required=True)

    def action_process_done(self):
        for record in self:
            category = record._context.get("default_category")
            if category:
                record.category = category
                record.crop_id.state = category
        return True
      