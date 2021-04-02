# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Iran - Accounting',
    'version': '1.1',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the accounting chart for Iran in Odoo.
==============================================================================

Install some generic chart of accounts.
    """,
    'depends': [
        'account',
    ],
    'data': [
        'data/l10n_ir.xml',
        'data/account.account.template.csv',
        'data/l10n_ir_post.xml',
    ],
    'demo': [
        'demo/account_bank_statement_demo.xml',
        'demo/account_invoice_demo.xml',
        'demo/account_reconcile_model.xml',
    ],
    'uninstall_hook': 'uninstall_hook',
}
