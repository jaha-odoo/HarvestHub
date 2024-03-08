from odoo import api,models,fields,_

class HarvestLocation(models.Model):
    _name="harvest.location"
    _description="farm's location records"
    _inherit="mail.thread"


    name= fields.Char(string='Name',required=True,tracking=True)
    address= fields.Char(string='Address',tracking=True)
    farmer=fields.Many2one('harvest.farmer',string="Farmer",tracking=True)
    animal_id=fields.Many2many('harvest.animal',string="Animal",tracking=True)
    ref=fields.Char(string='Reference',default=lambda self:_('New'))

    # _('New'): This is a call to the _() function, which is used for translating strings. The _() function is a convention in Odoo for marking strings that need to be translated into different languages. In this case, 'New' is the string to be translated.
    
    @api.model_create_multi
    def create(self,vals_list):  #self is the reference to the current instance of the class.  vals_list is the dictionary holding the key-value pairs. using that we initialize the new value.

        for vals in vals_list:
            vals['ref']=self.env['ir.sequence'].next_by_code('harvest.location')
        return super(HarvestLocation,self).create(vals_list)    
