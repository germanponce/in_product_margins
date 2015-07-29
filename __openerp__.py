# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to Odoo Management Solution
#
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################
#
##############################################################################
{
    'name': 'Margenes en Productos',
    'version': '1',
    "author" : "Integra",
    "category" : "Productos",
    'description': """
            
            Este modulo permite visualizar en el listado de productos, los margenes en monto y procentaje, de acuerdo a sus precios de Costo y Venta.
            """,
    "website" : "http://avalos.integra.co",
    "license" : "AGPL-3",
    "depends" : ["sale"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    'product.xml',
                    ],
    "installable" : True,
    "active" : False,
}
