from odoo import models,fields

class harvestFarmer(models.Model):
    _name="harvesthub.farmers"
    _description="farmers records"
    _inherit="mail.thread"

    name= fields.Char(string='Name',required=True,tracking=True)
    address= fields.Char(string='Address',tracking=True)
    phone= fields.Char(string='Phone',tracking=True)
    email= fields.Char(string='Email',tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender',tracking=True)
    age= fields.Integer(string='Age',tracking=True)
    taxId=fields.Char(string='TaxId' ,readonly=True,tracking=True)
    isold=fields.Boolean(string='IsOld ?',tracking=True)
   
   