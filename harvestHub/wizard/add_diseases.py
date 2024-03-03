from odoo import models, fields


class AddDiseaseWizard(models.TransientModel):
    _name = "harvest.adddisease.wizard"
    _description = "wizard for adding disease to one or more crops"

    name= fields.Char(string='Diseases Cure Name',required=True)
    detail= fields.Char(string='Detail')
    
    def action_add_disease(self):
        print("hello")
        crops= self.env["harvest.crop"].browse(self._context.get("active_ids", []))

        for record in crops:
            self.env["harvest.disease"].create(
                {
                    "name": self.name,
                    "detail": self.detail,
                    "crop_id":record.id
                }
            )
