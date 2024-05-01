from odoo import models, fields


class AccountMove(models.Model):
    """This class inherits 'account.move' and added fields insurance_id
     and claim_id. In addition, it also edits some strings from the original Odoo model"""
    _inherit = 'account.move'

    insurance_id = fields.Many2one('insurance.details',
                                   string='Insurance',
                                   help="Give the insurance details in invoice")
    claim_id = fields.Many2one('claim.details', string='Insurance Claim',
                               help="Give the claim details")

    invoice_user_id = fields.Many2one(
        string='Employee in Charge',  # Changed the string attribute to 'Employee'
        comodel_name='res.users',
        copy=False,
        tracking=True,
        compute='_compute_invoice_default_sale_person',
        store=True,
        readonly=False,
    )
