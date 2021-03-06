# -*- coding: utf-8 -*-
{
    'name': 'Argentina - Base para los Web Services del AFIP',
    'active': False,
    'author': 'OpenERP - Team de Localizaci\xc3\xb3n Argentina',
    'category': 'Localization/Argentina',
    'demo_xml': [],
    'depends': ['crypto', 'l10n_ar_invoice'],
    'license': 'AGPL-3',
    'data': ['data/wsafip_sequence.xml',
             'data/wsafip_server.xml',
             'data/wsafip_menuitem.xml',
             'data/wsafip_config.xml',
             'views/wsafip_server_view.xml',
             'views/wsafip_error_view.xml',
             'views/wsafip_connection_view.xml',
             'security/wsafip_security.xml',
             'security/ir.model.access.csv'],
    'demo': ['data/keys.yml',
             'data/wsafip_service.yml'],
    'test': ['test/test_mime_signer.yml',
             'test/test_wsafip_service.yml'],
    'version': '8.0.3.0',
    'website': 'https://launchpad.net/~openerp-l10n-ar-localization',
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
