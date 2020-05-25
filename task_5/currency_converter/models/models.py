# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TableOfCosts(models.Model):
    _name = 'currency_converter.table_of_costs'

    from_currency_id = fields.Many2one('res.currency', string='From currency')
    to_currency_id = fields.Many2one('res.currency', string='To currency')
    price = fields.Monetary('Price', currency_field='to_currency_id')
