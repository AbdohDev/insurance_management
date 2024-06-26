{
    'name': 'Insurance Management',
    'version': '17.0.1.0.0',
    'category': 'HR',
    'summary': """Insurance Management & Operations of the  and manage
     the insurance claims .""",
    'description': """Insurance and Claims Management based on policies that
	 allows the user to create insurance policies, manage insurance claims,
	 and create invoices for the insurance policies.""",
    'author': 'Abdullah Adel Al-Hadhrami',
    'maintainer': 'Abdullah Adel Al-Hadhrami',
    'website': 'https://www.AbdullahDev.com',
    'depends': ['account', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/payment_type_data.xml',
        'data/insurance_details_data.xml',
        'data/claim_details_data.xml',
        'views/claim_details_views.xml',
        'views/employee_details_views.xml',
        'views/insurance_details_views.xml',
        'views/policy_details_views.xml',
        'views/insurance_management_menus.xml',
        'views/policy_type_views.xml',
        'views/payment_type_views.xml',
        'views/account_move_views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}