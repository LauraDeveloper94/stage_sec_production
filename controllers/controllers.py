# -*- coding: utf-8 -*-
# from odoo import http


# class StageSecProduction(http.Controller):
#     @http.route('/stage_sec_production/stage_sec_production/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stage_sec_production/stage_sec_production/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stage_sec_production.listing', {
#             'root': '/stage_sec_production/stage_sec_production',
#             'objects': http.request.env['stage_sec_production.stage_sec_production'].search([]),
#         })

#     @http.route('/stage_sec_production/stage_sec_production/objects/<model("stage_sec_production.stage_sec_production"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stage_sec_production.object', {
#             'object': obj
#         })
