# Copyright 2016-2018 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrdersToInvoiceWizard(models.TransientModel):
    _name = "sale.orders.to.invoices.wizard"
    _description = "Wizard - Create invoices"

    def create_invoices(self):
        self.ensure_one()
        active_ids = self._context.get('active_ids')
        orders = self.env['sale.order'].browse(active_ids)
        orders.sale_orders.action_invoice_create(grouped=True, final=True)
