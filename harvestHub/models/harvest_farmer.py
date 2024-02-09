from odoo import models,fields

class harvestFarmer(models.Model):
    _name="harvesthub.farmers"
    _description="farmers records"

    name= fields.Char(string='Name',required=True)
    address= fields.Char(string='Address')
    phone= fields.Char(string='Phone')
    email= fields.Char(string='Email')
    gender=fields.Selection([('Male','Male'),('FeMale','FeMale')],string='Gender')
    taxId=fields.Char(string='TaxId')
