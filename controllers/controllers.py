# -*- coding: utf-8 -*-
# from odoo import http


# class TutorialBlock(http.Controller):
#     @http.route('/tutorial_block/tutorial_block', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_block/tutorial_block/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_block.listing', {
#             'root': '/tutorial_block/tutorial_block',
#             'objects': http.request.env['tutorial_block.tutorial_block'].search([]),
#         })

#     @http.route('/tutorial_block/tutorial_block/objects/<model("tutorial_block.tutorial_block"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_block.object', {
#             'object': obj
#         })
