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

import pdb

class hr_contract_view(orm.Model):
    _inherit = 'hr.contract'

    def write(cr, uid, ids, vals, context=None):
        super(hr_contract, self).write(cr, uid, ids, vals, context=context)
        self.pool.get("resource.global.contractcalendar").update_test(self, cr, uid, ids)
        
        return True
        

    def get_end_date(self, cr, uid, ids, fieldname, args, context=None):
        res = {}
        for contract in self.browse(cr, uid, ids, context):
            if contract.date_end:
                res[contract.id] = str(contract.date_end)
            else:
                res[contract.id] = str(datetime.date.today() +relativedelta(years=+1))
        return res
        
    # def fields_view_get(self, cr, user, view_id=None, view_type='calendar', 
                        # context=None, toolbar=False, submenu=False): 
        # res = super(hr_contract, self).fields_view_get( 
            # cr, user, view_id, view_type, context, toolbar, submenu) 
        # pdb.set_trace()
        # return res

    _columns = {
        'date_futur': fields.function(get_end_date, store=True, type='date')
#        'date_futur': fields.function(get_end_date,store=False)
    }

class resource_global_contract_calendar(orm.Model):
    _name = "resource.calendar.globalattendance"
    _description = "Global Attendance Calendar"
    _columns = {
        'name' : fields.char("Name", size=64),
        'company_id' : fields.related('calendar_id','company_id',
        type='many2one',relation='res.company',string="Company", 
        store=True, readonly=True),
        'calendar_id' : fields.many2one("resource.calendar", "Global Attendance Calendar"),
        'date_from' : fields.datetime('Start Date', required=True),
        'date_to' : fields.datetime('End Date', required=True),
        'resource_id' : fields.many2one("resource.resource", "Resource", help="",required=True),
    }

    def _get_week_days(year, week):
        d = date(2014,1,1)
        d = d - timedelta(days=(d.isoweekday()-1))
        dlt = timedelta(days = (week)*7)
        return d + dlt,  d + dlt + timedelta(days=6)    
    def update_test(self, cr, uid, ids):
        de=datetime.datetime(2014,10,8,17,0)
        ds=datetime.datetime(2014,10,8,7,0)
        self.create(cr, uid,{'date_from': str(ds),'resource_id': ids[0],'date_to': str(de),'name': "hell0"});
        
    def update_global_calendar(self, cr, uid, ids, fieldname, args,period_start=datetime.date(2014,1,1), period_end=datetime.date(2014,12,31), context=None):
        #iter over each contract
        for contract in self.browse(cr, uid, ids, context):
            date_cr=contract.date_start
            date_stop=contract.date_end
            if contract.date_start<period_start:
                date_cr=period_start
            if contract.date_end<period_end:
                date_stop=period_end
                i=int(date_cr.strftime("%W"))
                #iter over each week of the contract period
                while(i<=int(date_stop.strftime("%W"))):
                    print "Week "+str(i)
                    j,k=_get_week_days(int(date_cr.strftime("%Y")), i)
                    if date_cr<j: 
                        date_cr=j
                    #iter over each day of the week
                    while date_cr <= k:
                        print date_cr
                        date_cr += timedelta(days=1)
                    i+=1
                
        return True
    
    # def check_dates(self, cr, uid, ids, context=None):
         # leave = self.read(cr, uid, ids[0], ['date_from', 'date_to'])
         # if leave['date_from'] and leave['date_to']:
             # if leave['date_from'] > leave['date_to']:
                 # return False
         # return True

    # _constraints = [
        # (check_dates, 'Error! leave start-date must be lower then leave end-date.', ['date_from', 'date_to'])
    # ]

    # def onchange_resource(self, cr, uid, ids, resource, context=None):
        # result = {}
        # if resource:
            # resource_pool = self.pool.get('resource.resource')
            # result['calendar_id'] = resource_pool.browse(cr, uid, resource, context=context).calendar_id.id
            # return {'value': result}
        # return {'value': {'calendar_id': []}}

resource_global_contract_calendar()

