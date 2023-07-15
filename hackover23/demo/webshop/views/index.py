from lona.html import HTML, H1, Ul, Li, A
from lona import View


class IndexView(View):
    def handle_request(self, request):
        return HTML(
            H1('Webshop'),
            Ul(
                Li(
                    A(
                        'Interactive',
                        href=self.server.reverse('interactive__list_products'),
                    ),
                ),
                Li(
                    A(
                        'Non-Interactive',
                        href=self.server.reverse('non-interactive__list_products'),
                    ),
                ),
                Li(
                    A(
                        'Settings',
                        href=self.server.reverse('picocss__settings'),
                    ),
                ),
            ),
        )
