# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
import datetime
from dateutil.relativedelta import *


from openerp.osv import fields, orm


class hr_contract(orm.Model):
    _inherit = 'hr.contract'

    def get_end_date(self, cr, uid, ids, fieldname, args, context=None):
        res = {}
        for contract in self.browse(cr, uid, ids, context):
            if contract.date_end:
                res[contract.id] = str(contract.date_end)
            else:
                res[contract.id] = str(datetime.date.today() +relativedelta(years=+1))
        return res

    _columns = {
        'date_futur': fields.function(get_end_date, store=True, type='date')
#        'date_futur': fields.function(get_end_date,store=False)
    }
    
