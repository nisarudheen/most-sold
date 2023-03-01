odoo.define('web_most_viewd.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core =  require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
           var self = this;
           rpc.query({
               route: '/total_product_sold',
               params: {},
           }).then(function (result) {
           var name = result;
           name[0].set_active=true;
           $('.qweb_most_sold').append(Qweb.render('web_most_viewd.product_snippet',{name}));
           });
            rpc.query({
               route: '/total_viewed_product',
               params: {},
           }).then(function (result) {
           var viewed = result;
           viewed[0].set_active=true;
           $('.qweb_most_sold').append(Qweb.render('web_most_viewd.product_snippet2',{viewed}));
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});