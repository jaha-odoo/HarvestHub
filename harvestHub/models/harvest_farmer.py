from odoo import api,models,fields,_
from odoo.exceptions import ValidationError


class harvestFarmer(models.Model):
    _name="harvesthub.farmers"
    _description="farmers records"
    _inherit="mail.thread"
    # attribute in an Odoo model indicates that the model will inherit the behavior of the mail.thread model. In Odoo, the mail.thread model provides functionality related to communication and tracking, such as the ability to send messages, track activities, and manage followers.

    name= fields.Char(string='Name',required=True,tracking=True)
    address= fields.Char(string='Address',tracking=True)
    phone= fields.Char(string='Phone',tracking=True)
    email= fields.Char(string='Email',tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender',tracking=True)
    age= fields.Integer(string='Age',tracking=True)
    taxId=fields.Char(string='TaxId' ,readonly=True,tracking=True)
    isold=fields.Boolean(string='IsOld ?',tracking=True)
    ref=fields.Char(string='Reference',default=lambda self:_('New'))
    capitalize_name= fields.Char(string='Capitalize Name',compute='_compute_capitalize_name',store=True)

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            # if we want to make modification do here
            vals['ref']=self.env['ir.sequence'].next_by_code('harvesthub.farmers')
        return super(harvestFarmer,self).create(vals_list)    

    @api.constrains('isold','age')
    def check_is_old(self):
        for rec in self:
            if rec.isold and rec.age==0:
                raise ValidationError(_("age has to be recorded"))

    @api.depends('name')
    def _compute_capitalize_name(self):
        for rec in self:
            if rec.name:
                rec.capitalize_name=rec.name.upper()
            else:
                rec.capitalize_name=''    
    
    @api.onchange('age')
    def onchange_age(self):
        if self.age >=58:
            self.isold=True
        else:
            self.isold=False    
