from odoo import models,fields

class harvestAnimal(models.Model):
    _name="harvest.animal"
    _description="farm's animal records"

    name= fields.Char(string='Name',required=True)
