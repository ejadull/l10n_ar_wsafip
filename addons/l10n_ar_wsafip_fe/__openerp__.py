# -*- coding: utf-8 -*-
{
    'name': 'Argentina - Web Services de Factura Electrónica del AFIP',
    'active': False,
    'author': 'OpenERP - Team de Localización Argentina',
    'category': 'Localization/Argentina',
    'depends': ['l10n_ar_wsafip', 'l10n_ar_invoice'],
    'license': 'AGPL-3',
    'data': ['data/wsafip_server.xml',
             'data/invoice_workflow.xml',
             'data/reports.xml',
             'data/wsafip_server_actions.xml',
             'data/report_invoice.xml',
             'data/wsafip.error.csv',
             'views/wsafip_fe_config.xml',
             'views/invoice_view.xml',
             'views/journal_view.xml',
             'views/res_config_view.xml',
             'views/query_invoices_view.xml',
             'security/wsafip_fe_security.xml',
             'security/ir.model.access.csv'],
    'demo': ['data/journal.yml',
             ],
    'test': ['test/journal_online.yml',
             'test/query_invoices.yml',
             'test/invoice.yml',
             'test/inv_2iva.yml',
             'test/inv_2prod.yml',
             'test/delayed.yml'],
    'version': '8.0.3.0',
    'website': 'https://launchpad.net/~openerp-l10n-ar-localization',
    'installable': True,
    'external_dependencies': {'python': ['openupgradelib']},
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
