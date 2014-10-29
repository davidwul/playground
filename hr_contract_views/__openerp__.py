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


{
    'name': 'Employee Contracts views',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
Add calendar and gantt views on the contracts.
=============================================================

You can see availabilty of employee display on gantt or calendar.
    """,
    'author': 'David Wulliamoz',
    'website': 'http://www.compassion.ch',
    'images': ['images/hr_contract.jpeg'],
    'depends': ['hr_contract'],
    'data': [
        'hr_contract_view.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
