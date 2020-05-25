# -*- coding: utf-8 -*-
from odoo import http


class CurrencyConverter(http.Controller):
    @http.route('/currency_converter/currency_converter/', auth='public')
    def index(self, **kw):
        return "Hello, world"


#     @http.route('/currency_converter/currency_converter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('currency_converter.listing', {
#             'root': '/currency_converter/currency_converter',
#             'objects': http.request.env['currency_converter.currency_converter'].search([]),
#         })

#     @http.route('/currency_converter/currency_converter/objects/<model("currency_converter.currency_converter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('currency_converter.object', {
#             'object': obj
#         })
