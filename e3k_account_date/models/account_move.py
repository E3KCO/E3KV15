# -*- coding: utf-8 -*-

from odoo import api, models

class AccountMove(models.Model):
  _inherit = 'account.move'

  @api.onchange('invoice_date')
  def _onchange_invoice_date(self):
    if self.invoice_date:
      self.date = self.invoice_date

  def _post(self, soft=True):
    for move in self:
      move.date = move.invoice_date or move.date
      move.invoice_line_ids.sudo().write({'date': move.date})
    return super(AccountMove, self)._post(soft)