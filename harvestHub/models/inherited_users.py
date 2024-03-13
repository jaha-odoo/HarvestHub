from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    crop_order_ids = fields.One2many("harvest.crop.order", "owner_id")
    
