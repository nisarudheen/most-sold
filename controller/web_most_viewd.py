import itertools
import operator

from odoo import http
from odoo.http import request


class Sales(http.Controller):
    @http.route(['/total_product_sold'], type="json", auth="public")
    def sold_total(self):
        values = {}
        vals = []
        new_list = []
        for i in request.env['product.template'].sudo().search([]):
            values.update({
                  i: i.sales_count,
            })
        sorted_d = dict(sorted(values.items(), key=operator.itemgetter(1), reverse=True))
        limit = dict(itertools.islice(sorted_d.items(), 25))
        for i in limit:
            vals.append([
                i.name, i.id,
            ])
        for i in range(0, len(vals), 4):
            new_list.append(vals[i:i+4])
        return new_list

    @http.route(['/total_viewed_product'], type="json", auth="public")
    def most_viewed(self):
        product_ids = request.env['product.product'].sudo().search([])
        vals = product_ids.product_tmpl_id
        most_viewed = []
        filtered_list= []
        for i in request.env['website.track'].sudo().search([]):
            for rec in vals:
                if rec.id == i.product_id.id:
                    most_viewed.append([
                        rec.name, rec.id,
                    ])
        for i in range(0, len(most_viewed), 4):
            filtered_list.append(most_viewed[i:i + 4])
        return filtered_list


