from lona import View, RedirectResponse

from webshop.models import Product


class DeleteProductView(View):
    def handle_request(self, request):
        product = Product.objects.get(int(request.match_info['id']))

        product.delete()

        return RedirectResponse(
            self.server.reverse('non-interactive__list_products'),
        )