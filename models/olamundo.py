# -*- coding: utf-8 -*-

from odoo import models, fields, api


class olamundo(models.Model):
     _name = 'odoo_olamundo.olamundo'
     _description = 'Exemplo OlaMundo'

     name = fields.Char("Ola Mundo:")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
