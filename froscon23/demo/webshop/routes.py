from lona import Route


routes = [

    # interactive
    Route(
        '/interactive/products/',
        'views/interactive/list_products.py::ListProductsView',
        name='interactive__list_products',
    ),

    # non-interactive
    Route(
        '/non-interactive/products/add/',
        'views/non_interactive/edit_product.py::EditProductView',
        name='non-interactive__add_product',
    ),

    Route(
        '/non-interactive/products/<id>/delete/',
        'views/non_interactive/delete_product.py::DeleteProductView',
        name='non-interactive__delete_product',
    ),

    Route(
        '/non-interactive/products/<id>/',
        'views/non_interactive/edit_product.py::EditProductView',
        name='non-interactive__edit_product',
    ),

    Route(
        '/non-interactive/products/',
        'views/non_interactive/list_products.py::ListProductsView',
        name='non-interactive__list_products',
    ),

    # index
    Route(
        '/',
        'views/index.py::IndexView',
        name='index',
    ),

    Route(
        '/_picocss/settings(/)',
        'lona_picocss.views.settings.SettingsView',
        name='picocss__settings',
    ),
]
