# -*- coding: utf-8 -*-

from odoo import models, fields, api,  tools
import logging
_logger = logging.getLogger(__name__)

class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    state_id = fields.Many2one("res.country.state", string='State')
    price_subtotal_currency = fields.Float(string='Untaxed Total-customer', readonly=True)

    def _select(self):
        return super()._select() + """
        , COALESCE(partner.state_id, commercial_partner.state_id) AS state_id,
        CASE WHEN move.move_type IN ('in_invoice','out_refund','in_receipt') THEN -line.price_subtotal ELSE line.price_subtotal END AS price_subtotal_currency
        """
