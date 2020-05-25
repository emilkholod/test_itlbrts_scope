# -*- coding: utf-8 -*-
from odoo import http


class CurrencyConverter(http.Controller):
    @http.route('/wow/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/currencies/', auth='public', website=True)
    def currencies(self, **kw):
        return {
            'type': 'ir.actions.act_url',
            'url': '/eur/',
            'target': 'self',
            'res_id': self.id,
        }

    @http.route('/currencies/eur/', auth='public', website=True)
    def currencies(self, **kw):
        return "Hello world"

#     @http.route('/currency_converter/currency_converter/objects/<model("currency_converter.currency_converter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('currency_converter.object', {
#             'object': obj
#         })
