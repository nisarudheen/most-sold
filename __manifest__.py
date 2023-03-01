{'name': 'Most Viewd&Sold Web',
 'version': '16.0.1.0.0',
 'sequence': -1,
 'website': 'https://www.odoo.com/page/travel_management',
 'category': 'Sales',
 'installable': True,
 'application': True,
 'auto_install': False,
 'depends': ['base', 'sale','website',],
 'data': [
     'views/most_sold.xml',
     'views/web_snippet.xml',
 ],
 'assets':{
     'web.assets_frontend': [
         'web_most_viewd/static/src/js/snippet.js',
         'web_most_viewd/static/src/xml/web_snippet_views.xml',
         'web_most_viewd/static/src/css/snippet.scss'
     ]
     }
 }