from odoo import models,fields

class HarvestAnimal(models.Model):
    _name="harvest.animal"
    _description="farm's animal records"
    _inherit="mail.thread"

    name= fields.Char(string='Name',required=True,tracking=True)
