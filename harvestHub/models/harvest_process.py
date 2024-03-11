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
        ],
        string="Category",
        tracking=True,
    )
    crop_id = fields.Many2one("harvest.crop", required=True,string="Crop Order",tracking=True)
    animal_id=fields.Many2many('harvest.animal',string="Animal",tracking=True)
    vehicle_id = fields.Many2many("fleet.vehicle", string="Vehicles",tracking=True)


    def action_process_done(self):
        for record in self:
            category = record._context.get("default_category")
            if category:
                record.category = category
                record.crop_id.state = category
        return True
      