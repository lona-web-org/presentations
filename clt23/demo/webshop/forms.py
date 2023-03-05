from webshop.models import Product

from lona_picocss.html import (
    NumberInput,
    TextInput,
    TextArea,
    Label,
    Div,
)


class ProductForm(Div):
    def __init__(self, product=None):
        super().__init__()

        self.name_field = TextInput()
        self.price_field = NumberInput()
        self.description_field = TextArea()

        self.product = product

        if self.product:
            self.name_field.value = self.product.name
            self.price_field.value = self.product.price
            self.description_field.value = self.product.description

        self.nodes = [
            Label(
                'Name',
                self.name_field,
            ),
            Label(
                'Price',
                self.price_field,
            ),
            Label(
                'Description',
                self.description_field,
            ),
        ]

    def save(self):
        with self.lock:
            if self.product:
                self.product.name = self.name_field.value
                self.product.price = self.price_field.value
                self.product.description = self.description_field.value

            else:
                Product.objects.create(
                    name=self.name_field.value,
                    price=self.price_field.value,
                    description=self.description_field.value,
                )
