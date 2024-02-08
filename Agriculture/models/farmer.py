from odoo import models,fields

class estateProperty(models.Model):
    _name="agriculture.farmer"
    _description="farmer records"

    name= fields.Char(string='Name',required=True)
    address= fields.Text(string='Description')
    email= fields.Char(string='Email')
    phone= fields.Char(string='Phone')
    mobile= fields.Char(string='Mobile')
    gender=fields.Selection([('male','male'),('female','female')],string='Gender')
    age=fields.Integer(string='Age')
    


    
