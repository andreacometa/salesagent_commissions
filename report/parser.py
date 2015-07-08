# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Domsense s.r.l. (<http://www.domsense.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

import time
from report import report_sxw
from tools.translate import _

class printed_cards(report_sxw.rml_parse):
    _name = 'parser.printed_cards'
    
    def cards_by_club(self, printed_cards):
        res = {}
        for partner in printed_cards.partner_ids:
            key = (partner.club_id.id, partner.club_id.ref)
            if key not in res:
                res[key] = 0
            res[key] +=1
        return res
    
    def __init__(self, cr, uid, name, context=None):
        if context is None:
            context = {}
        super(printed_cards, self).__init__(cr, uid, name, context=context)
        self.localcontext.update( {
            'time': time,
            'cards_by_club': self.cards_by_club,
        })
        self.context = context

report_sxw.report_sxw('report.printed_cards',
                      'asi.export.printing.cards',
                      'addons/asi_base/report/printed_cards.mako',
                      parser=printed_cards)


