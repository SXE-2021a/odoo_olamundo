# -*- coding: utf-8 -*-
# from odoo import http


# class OdooOlamundo(http.Controller):
#     @http.route('/odoo_olamundo/odoo_olamundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_olamundo/odoo_olamundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_olamundo.listing', {
#             'root': '/odoo_olamundo/odoo_olamundo',
#             'objects': http.request.env['odoo_olamundo.odoo_olamundo'].search([]),
#         })

#     @http.route('/odoo_olamundo/odoo_olamundo/objects/<model("odoo_olamundo.odoo_olamundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_olamundo.object', {
#             'object': obj
#         })
