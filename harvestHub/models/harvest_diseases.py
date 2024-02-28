from odoo import api,models,fields

class harvestDiseases(models.Model):
    _name="harvest.disease"
    _description="crop's diseases records"
    _inherit="mail.thread"


    name= fields.Char(string='Diseases Cure Name',required=True,tracking=True)
    detail= fields.Char(string='Detail',tracking=True)
    symptoms= fields.Char(string='Symptoms',tracking=True)
    condition= fields.Char(string='Suitable Condition',tracking=True)
    precaustions= fields.Char(string='Precaustions',tracking=True)
    medications= fields.Char(string='Medications',tracking=True)

