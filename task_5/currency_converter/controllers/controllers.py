# -*- coding: utf-8 -*-
from odoo import http


class CurrencyConverter(http.Controller):
    @http.route('/wow/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/currencies/', auth='public', website=True)
    def redirect_to_eur(self, **kw):
        return http.request.redirect('/currencies/eur/')

    @http.route('/currencies/eur/', auth='public', website=True)
    def currencies(self, **kw):
        TableOfCosts = http.request.env['res.currency']
        print('Hello world!!!')
        print(TableOfCosts.search([]))
        return "Hello world2"

#     @http.route('/currency_converter/currency_converter/objects/<model("currency_converter.currency_converter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('currency_converter.object', {
#             'object': obj
#         })
