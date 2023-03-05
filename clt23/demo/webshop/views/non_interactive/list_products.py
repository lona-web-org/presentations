from lona import View

from lona_picocss.html import (
    InlineButton,
    THead,
    TBody,
    Table,
    HTML,
    Icon,
    Div,
    H1,
    Tr,
    Th,
    Td,
    A,
)

from webshop.models import Product


class ListProductsView(View):
    def handle_request(self, request):
        tbody = TBody()

        for product in Product.objects.all():
            tbody.append(
                Tr(
                    Td(
                        A(
                            str(product.name),
                            href=self.server.reverse(
                                'non-interactive__edit_product',
                                id=product.id,
                            ),
                        ),
                    ),
                    Td(str(product.price)),
                    Td(
                        A(
                            Icon('trash'),
                            title='Delete',
                            role='button',
                            href=self.server.reverse(
                                'non-interactive__delete_product',
                                id=product.id,
                            ),
                        ),
                    ),
                ),
            )

        return HTML(
            H1('Products'),
            Div(
                A(
                    'Add Product',
                    role='button',
                    href=self.server.reverse(
                        'non-interactive__add_product',
                    ),
                ),
                style={
                    'text-align': 'right',
                    'margin-bottom': '1em',
                },
            ),
            Table(
                THead(
                    Tr(
                        Th('Name'),
                        Th('Price'),
                        Th('Actions', width='5em'),
                    ),
                ),
                tbody,
            )
        )