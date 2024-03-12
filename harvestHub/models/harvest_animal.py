from odoo import models,fields

class HarvestAnimal(models.Model):
    _name="harvest.animal"
    _description="farm's animal records"
    _inherit="mail.thread"

    name= fields.Char(string='Name',required=True,tracking=True)
    count= fields.Integer(string='Count',required=True,tracking=True)
    description=fields.Char(string='Description',tracking=True)
    process_id = fields.Many2one("harvest.process",required=True,tracking=True)
