# -*- coding: utf-8 -*-
from collections import OrderedDict

from odoo import http


class CurrencyConverter(http.Controller):
    @http.route('/hello/', auth='public')
    def index(self, **kw):
        return "Hello, world!"

    @http.route('/currencies/', auth='public', website=True)
    def redirect_to_eur(self, **kw):
        return http.request.redirect('/currencies/eur/')

    @http.route('/currencies/<new_base_curr_name>/',
                auth='public',
                website=True)
    def currencies(self, new_base_curr_name, **kw):
        CurrencyRate = http.request.env['res.currency.rate']
        list_of_curr_rates = CurrencyRate.search([]).read(
            ['id', 'currency_id', 'rate'])

        out = {}
        for curr_rate in list_of_curr_rates:
            out[curr_rate['currency_id'][1]] = curr_rate['rate']

        for k, v in out.items():
            out[k] = v / out[new_base_curr_name.upper()]

        sorted_out = OrderedDict(sorted(out.items(), key=lambda x: x[0]))
        return http.request.render(
            'currency_converter.currency_converter_table',
            {'currency_rates': sorted_out},
        )
