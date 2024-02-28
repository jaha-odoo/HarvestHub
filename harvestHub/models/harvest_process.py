from odoo import models,fields

class harvestProcess(models.Model):
    _name="harvest.process"
    _description="crop's process records"
    _inherit="mail.thread"

    name= fields.Char(string='Task Of Processes',required=True,tracking=True)
    description=fields.Char(string='description',required=True,tracking=True)
