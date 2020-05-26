{
    'name':
    "currency_converter",
    'summary':
    """
        Конвертер валют""",
    'description':
    """
        Данный модуль зависим от следующих приложений:
            • website
    """,
    'author':
    "Emil",
    'website':
    "http://www.vk.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':
    'Uncategorized',
    'version':
    '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'views/template.xml',
    ]
}
