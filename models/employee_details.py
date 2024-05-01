import re
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class EmployeeDetails(models.Model):
    """This class creates a model 'employee.details' and added fields """
    _name = 'employee.details'
    _description = "Employee Details"

    name = fields.Char(string='Name', required=True,
                       help="Name of the employee")
    user_id = fields.Many2one(
        'res.users', string='Related Employee', copy=False,
        help="Related Employee")
    sex = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        help="Select the sex of the employee")
    phone = fields.Char(string='Phone Number', help="Phone number of employee",
                        required=True)
    currency_id = fields.Many2one(
        'res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id.id,
        help="Select the currency")
    insurance_ids = fields.One2many('insurance.details',
                                    'employee_id',
                                    string='Last Details', readonly=True,
                                    help="Insurance details created "
                                         "by employee")
    note_field = fields.Html(string='Comment',
                             help="Give notes,if any")
    invoice_id = fields.Many2one(
        'account.move', string='Last payment', copy=False,
        readonly=True,
        help="Invoice of last payment")

    @api.constrains('phone')
    def check_phone(self):
        """ Make sure phone contains either 9 or 10 digits """
        for rec in self:
            if not re.match('^[0-9]{9,10}$', rec.phone):
                raise ValidationError(
                    _('Phone number should contain either 9 or 10 digits and only '
                      'numbers are allowed'))
