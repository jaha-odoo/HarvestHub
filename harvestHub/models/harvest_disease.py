from odoo import api,models,fields

class HarvestDisease(models.Model):
    _name="harvest.disease"
    _description="crop's diseases records"
    _inherit="mail.thread"


    name= fields.Char(string='Diseases Cure Name',required=True,tracking=True)
    detail= fields.Char(string='Detail',tracking=True)
    symptoms= fields.Char(string='Symptoms',tracking=True)
    condition= fields.Char(string='Suitable Condition',tracking=True)
    precaustions= fields.Char(string='Precaustions',tracking=True)
    medications= fields.Char(string='Medications',tracking=True)
    crop_id = fields.Many2one("harvest.crop", required=True,tracking=True)


    @api.model
    def create(self, vals):
        print(vals)
        crop_object=self.env["harvest.crop"].browse(vals["crop_id"])
       
        return super(HarvestDisease, self).create(vals)


