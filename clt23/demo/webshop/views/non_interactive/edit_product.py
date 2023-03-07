from lona_picocss.html import HTML, Div, H1, InlineButton
from lona import View, RedirectResponse

from webshop.forms import ProductForm
from webshop.models import Product


class EditProductView(View):
    def cancel(self, input_event):
        return RedirectResponse(
            self.server.reverse('non-interactive__list_products'),
        )

    def save(self, input_event):
        self.form.save()

        return RedirectResponse(
            self.server.reverse('non-interactive__list_products'),
        )

    def handle_request(self, request):
        product_id = request.match_info.get('id', None)

        # edit
        if product_id:
            title = H1('Edit Product')

            self.form = ProductForm(
                product=Product.objects.get(int(product_id)),
            )

        # add
        else:
            title = H1('Add Product')
            self.form = ProductForm()

        return HTML(
            title,
            self.form,

            Div(
                InlineButton(
                    'Cancel',
                    secondary=True,
                    handle_click=self.cancel,
                ),
                ' ',
                InlineButton(
                    'Save',
                    handle_click=self.save,
                ),
                style={
                    'text-align': 'right',
                },
            ),
        )
