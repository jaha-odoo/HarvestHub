from odoo import models,fields

class HarvestIncident(models.Model):
    _name="harvest.incident"
    _description="incident details of crops"
    _inherit="mail.thread"

    name= fields.Char(string='Name',required=True,tracking=True)
    description=fields.Char(string='Description',required=True,tracking=True)
    date=fields.Date(string='Incident Date',tracking=True)
    location_ids=fields.Many2many('harvest.location',tracking=True)
