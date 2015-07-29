# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################


from openerp import SUPERUSER_ID
from openerp import tools
from openerp.osv import osv, fields, expression
from openerp.tools.translate import _

class product_template(osv.osv):
    _name = 'product.template'
    _inherit ='product.template'


    def _get_margin_cost(self, cr, uid, ids, field_name, arg, context=None):
        result={
            }
        costo = 0.0
        margin_percent = 0.0
        margin = 0.0
        for rec in self.browse(cr, uid, ids, context=None):
            if rec.standard_price == 0.0:
                margin = rec.list_price
                margin_percent = 100
            else:
                if rec.standard_price:
                    costo = rec.standard_price
                if costo > 0.0 and rec.list_price > 0.0:
                    margin = rec.list_price - costo
                    margin_percent = margin / rec.list_price * 100
            result[rec.id] = {'margin_percent' : margin_percent,
                              'margin' : margin,
                              }
        return result
    _columns = {
        'margin_percent': fields.function(_get_margin_cost, string="Margen %", method=True, type='float', digits=(14,2), store=True, readonly=True, help='Indica el Porcentaje del precio de Venta - Costo Compra', multi="margen"),
        'margin': fields.function(_get_margin_cost, string="Margen $", method=True, type='float', digits=(14,2), store=True, readonly=True, help='Indica el Margen del precio de Venta - Costo Compra', multi="margen"),
        }

    _default = {
        }
product_template()
