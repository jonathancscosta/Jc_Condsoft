# -*- coding: utf-8 -*-
{
    'name': "Gestão dos módulos Jc Costa de Tecnologia",

    'summary': """
        Acesso aos módulos de controle de Jc Costa Tecnologia""",

    'description': """
        Módulos para controle das unidades AC-1000, AC-2500 da Jc Costa de Tecnologia
    """,

    'author': "Jonathan César Costa",
    'website': "https://github.com/jonathancscosta",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module
    # /module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '15.0.0.0',

    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'oc_base', ],

    # always loaded
    'data': [
            'security/oc_virdi_security.xml',
            'security/ir.model.access.csv',
            'views/occ_controle_acesso_veiculos_tag.xml',
            'views/occ_controle_acesso_veiculos_manual.xml',
            'views/occ_controle_acesso_prestserv.xml',
            'views/occ_controle_acesso_visitante.xml',
            'views/occ_virdi.xml',
            'data/motivos_abertura_manual_cancela.xml',
    ],
}
