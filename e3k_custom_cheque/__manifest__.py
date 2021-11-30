# -*- coding: utf-8 -*-

{
  "name" : "e3k Custom Payment Cheque",
  "summary" : "",
  "description" : """

e3k Custom Payment Cheque
=========================

    """,
  "category" : "Account",
  "author" : "e3k Solutions",
  "license" : "Other proprietary",
  "website" : "https://e3k.co",
  "sequence" : 1,
  "version" : "15.0.1.0.0",
  "depends" : [
    'account',
    'l10n_ca_check_printing',
  ],
  "data" : [
    'views/company.xml',
    'report/print_check_top.xml',
  ],
  "qweb" : [
    'static/src/xml/*.xml',
  ],
  "assets" : {
    'web.report_assets_common': [
      'e3k_custom_cheque/static/**/*',
    ],
  },
  "images" : [],
  "application" : False,
  "installable" : True,
  "auto_install" : False,
  "pre_init_hook" : "pre_init_check",
}
