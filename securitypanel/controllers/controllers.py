# -*- coding: utf-8 -*-
from odoo import http

# class Securitypanel(http.Controller):
#     @http.route('/securitypanel/securitypanel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/securitypanel/securitypanel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('securitypanel.listing', {
#             'root': '/securitypanel/securitypanel',
#             'objects': http.request.env['securitypanel.securitypanel'].search([]),
#         })

#     @http.route('/securitypanel/securitypanel/objects/<model("securitypanel.securitypanel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('securitypanel.object', {
#             'object': obj
#         })