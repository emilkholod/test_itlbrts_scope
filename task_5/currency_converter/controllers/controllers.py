# -*- coding: utf-8 -*-
from odoo import http
import json


class CurrencyConverter(http.Controller):
    @http.route('/wow/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/currencies/', auth='public', website=True)
    def redirect_to_eur(self, **kw):
        return http.request.redirect('/currencies/eur/')

    @http.route('/currencies/eur/', auth='public', website=True)
    def currencies(self, **kw):
        CurrencyRate = http.request.env['res.currency.rate']
        currency_rate = CurrencyRate.search([])
        # print(currency_rate.read(['id', 'currency_id', 'rate']))
        # return json.dumps(currency_rate.read(['id', 'currency_id', 'rate']))
        return http.request.render('currency_converter.index',
                                   {'currency_rates': currency_rate})


#     @http.route('/currency_converter/currency_converter/objects/<model("currency_converter.currency_converter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('currency_converter.object', {
#             'object': obj
#         })
