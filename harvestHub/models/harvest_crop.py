from odoo import api,models,fields

class harvestCrop(models.Model):
    _name="harvest.crop"
    _description="farm's crop records"
    _inherit="mail.thread"


    name= fields.Char(string='Name',required=True,tracking=True)
    durations= fields.Integer(string='Crop Duration(days)',tracking=True)
    season=fields.Selection([('winter','Winter'),('summer','Summer'),('monsoon','Monsoon')],string='Season',tracking=True)
    state=fields.Selection([('Preparation','Preparation'),('Planting','Planting'),('Growing','Growing'),('Harvesting','Harvesting'),('Post-Harvest','Post-Harvest')],string='State',tracking=True)
    description=fields.Char(string='Description',tracking=True)
