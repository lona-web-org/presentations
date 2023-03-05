from lona import Route


routes = [
    Route('/', 'views/list_products.py::ListProductsView',
          name='products__list'),
]
