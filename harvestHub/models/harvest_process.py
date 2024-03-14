from odoo import models, fields,api


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
    start_date = fields.Datetime(string="Start Date", tracking=True)
    end_date = fields.Datetime(string="End  Date", tracking=True)
    date_difference = fields.Integer(string="Total Hours", compute='compute_date_difference', store=True)
    crop_id = fields.Many2one(
        "harvest.crop", required=True, string="Crop Order", tracking=True
    )
    animal_ids = fields.One2many("harvest.animal", "process_id", tracking=True)
    equipment_ids = fields.One2many("harvest.equipment", "process_id", tracking=True)
    vehicle_id = fields.Many2many("fleet.vehicle", string="Vehicles", tracking=True)
    farmer_id = fields.Many2many("harvest.farmer", string="Farmers", tracking=True)


    def action_process_done(self):
        for record in self:
            category = record._context.get("default_category")
            if category:
                record.category = category
                record.crop_id.state = category
        return True

    @api.depends("start_date", "end_date")
    def compute_date_difference(self):
        for record in self:
            start_date = fields.Datetime.to_datetime(record.start_date)
            end_date = fields.Datetime.to_datetime(record.end_date)
            if start_date and end_date:
                date_difference = (
                    end_date - start_date
                ).total_seconds() / 3600  # Difference in hours
                record.date_difference = int(date_difference)
