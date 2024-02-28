from odoo import models,fields

class harvestVehicle(models.Model):
    _name="harvest.vehicle"
    _description="farm's vehicle records"


    name= fields.Char(string='Vehicle Name',required=True)
    quantity= fields.Integer(string='quantity',required=True)
    farmer_id=fields.Many2one('harvesthub.farmers',required=True)
  