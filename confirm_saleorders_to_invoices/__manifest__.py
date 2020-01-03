# Copyright 2016-2018 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Orders To  Invoices',
    'summary': 'Create several invoices from several confirm sale orders',
    'author': 'Onestein',
    'license': 'AGPL-3',
    'website': 'http://www.digitom.fr',
    'category': 'Sales',
    'version': '13.0.0.1.0',
    'depends': [
        'sale',
        'invoice'
    ],
    'data': [
        'wizard/sale_orders_to_invoices.xml',
    ],
    'installable': True,
}
