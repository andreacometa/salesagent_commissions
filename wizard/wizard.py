# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields,osv

# ---------------------------------------------------------------
#	CALCOLATE COMISSION FROM FIX EARNING
# ---------------------------------------------------------------
class wzd_percentage_calcolate(osv.osv_memory):

	_name = "wzd.percentage_calcolate"

	_columns = {
		'product_price' : fields.float('Product Price'),
		'fix_commission' : fields.float('Fix Salesagent Commission'),
		'percentage' : fields.float('Percentage'),
		}

	def percentage_calcolate(self, cr, uid, ids, context={}):
		wizard_obj = self.browse(cr,uid,ids[0])
		percentage = wizard_obj.fix_commission / wizard_obj.product_price
		self.write(cr, uid, ids, {'percentage':percentage})
		return True

wzd_percentage_calcolate()


# ---------------------------------------------------------------
#	MANAGE THE COMMISSIONS PAYMENT
# ---------------------------------------------------------------
class wzd_commissions_payment(osv.osv_memory):

	_name = "wzd.commissions_payment"

	_columns = {
		'payment_date' : fields.date('Payment Date'),
		'payment_commission_note' : fields.char('Notes', size=128),
		}

	def pagamento_provvigioni(self, cr, uid, ids, context={}):
		if not 'active_ids' in context:
			raise osv.except_osv(_('Invalid Operation!'), _('Select at least one line!'))
		# ----- Seleziona l'oggetto in base al modello attivo e ne segnala il pagamento
		wizard_obj = self.browse(cr,uid,ids[0])
		line_obj = self.pool.get(context['active_model'])
		lines = line_obj.browse(cr, uid, context['active_ids'])
		for line in lines:
			# ----- Scrive il pagamento
			line_obj.write(cr, uid, [line.id,], {
				'payment_commission_date' : wizard_obj.payment_date,
				'paid_commission' : True,
				'paid_commission_value' : line.commission,
				'paid_commission_percentage_value' : line.commission_percentage,
				'payment_commission_note':wizard_obj.payment_commission_note})
		return {'type': 'ir.actions.act_window_close'}

wzd_commissions_payment()


# ---------------------------------------------------------------
#	DELETE COMMISSIONS PAYMENT
# ---------------------------------------------------------------
class wzd_payment_cancellation(osv.osv_memory):

	_name = "wzd.payment_cancellation"

	_columns = {
		'note_cancellation' : fields.boolean('Delete Notes'),
		}

	def annulla_pagamento(self, cr, uid, ids, context={}):
		if not 'active_ids' in context:
			raise osv.except_osv(_('Invalid Operation!'), _('Select at least one line!'))
		# ----- Seleziona l'oggetto in base al modello attivo e ne segnala il pagamento
		wizard_obj = self.browse(cr,uid,ids[0])
		line_obj = self.pool.get(context['active_model'])
		# ----- Scrive il pagamento
		args = {'payment_commission_date' : False,
			'paid_commission' : False,
			'paid_commission_value' : 0.0,
			'paid_commission_percentage_value':0.0}
		if wizard_obj.note_cancellation:
			args['payment_commission_note'] = ''
		line_obj.write(cr, uid, context['active_ids'], args)
		return {'type': 'ir.actions.act_window_close'}

wzd_payment_cancellation()
