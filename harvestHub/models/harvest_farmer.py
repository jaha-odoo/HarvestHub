from odoo import api,models,fields,_
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class HarvestFarmer(models.Model):
    _name="harvest.farmer"
    _description="farmers records"
    _inherit="mail.thread"
    # attribute in an Odoo model indicates that the model will inherit the behavior of the mail.thread model. In Odoo, the mail.thread model provides functionality related to communication and tracking, such as the ability to send messages, track activities, and manage followers.

    name= fields.Char(string='Name',required=True,tracking=True)
    address= fields.Char(string='Address',tracking=True)
    phone= fields.Char(string='Phone',tracking=True)
    email= fields.Char(string='Email',tracking=True)
    farmer_photo = fields.Image(string='Farmer Photo')
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender',tracking=True)
    date_of_birth=fields.Date(string='Date of Birth',tracking=True)
    age= fields.Integer(string='Age',tracking=True,compute="_compute_age",store=True,inverse="_inverse_age")
    isold=fields.Boolean(string='Isold ?',tracking=True)
    ref=fields.Char(string='Reference',default=lambda self:_('New'))
    vehicle_id = fields.Many2many("fleet.vehicle", string="Vehicles",tracking=True)

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            # if we want to make modification do here
            vals['ref']=self.env['ir.sequence'].next_by_code('harvest.farmer')
        return super(HarvestFarmer,self).create(vals_list)    
         
    @api.depends('date_of_birth')
    def _compute_age(self):
      for rec in self:
        if rec.date_of_birth:
            age = relativedelta(fields.Date.today(),rec.date_of_birth).years
            rec.age = age
   
    @api.depends('age')
    def _inverse_age(self):
        for rec in self:
            if rec.age:
                rec.date_of_birth = fields.Date.today() - relativedelta(years=rec.age)

   
    @api.onchange('age')
    def onchange_age(self):
        if self.age >=58:
            self.isold=True
        else:
            self.isold=False  

    @api.constrains('isold','age')
    def _check_is_old(self):
        for rec in self:
            if rec.isold and rec.age==0:
                raise ValidationError("age has to be recorded")
