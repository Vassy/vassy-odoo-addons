# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    (c) 2016-2018 Prodax Ltd. - Vassil Toumbev (support@openerp.bg)
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
    'name': 'Invoice Amount Text',
    'version': '10.0.1.0',
    'author': Prodax Ltd. - Odoo Bulgaria - Vassil Toumbev',
    'website': 'http://www.openerp.bg',
    'category': 'Accounting & Finance',
    'depends': [
        'account',
    ],
    'data': [

	'account_invoice_view.xml',
        'views/report_invoice.xml',

    ],

    'installable': False,
    'auto_install': False,
}

