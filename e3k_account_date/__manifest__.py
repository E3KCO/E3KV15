# -*- coding: utf-8 -*-

{
  "name" : "e3k Account Date",
  "summary" : "Modifie la \"Date comptable\" lors de la validation des factures.",
  "description" : """

e3k Account Date
================
- En modifiant la "Date de facturation" d'une facture, sa "Date comptable" devient égale à cette dernière.
- En confirmant une facture, la date des "Écritures comptables" sont modifiées à la "Date de facturation".

    """,
  "category" : "Account",
  "author" : "e3k Solutions",
  "license" : "Other proprietary",
  "website" : "https://e3k.co",
  "sequence" : 1,
  "version" : "15.0.1.0.0",
  "depends" : [
    'account',
  ],
  "data" : [],
  "qweb" : [
    'static/src/xml/*.xml',
  ],
  "images" : [],
  "application" : False,
  "installable" : True,
  "auto_install" : False,
  "pre_init_hook" : "pre_init_check",
}