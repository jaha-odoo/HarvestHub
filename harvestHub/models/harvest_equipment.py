from odoo import models,fields

class HarvestEquipment(models.Model):
    _name="harvest.equipment"
    _description="farm's equipments records"
   

    name= fields.Char(string='Name',required=True)
    description=fields.Char(string='Description')
    owner_id=fields.Many2one('res.partner',string="Owner")
    date=fields.Date(string='Alloted Date')
    process_id = fields.Many2one("harvest.process",required=True)
