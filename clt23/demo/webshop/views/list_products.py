from lona_picocss.html import (
    InlineButton,
    Progress,
    Table,
    THead,
    TBody,
    CLICK,
    Modal,
    HTML,
    Icon,
    Div,
    H1,
    H3,
    Tr,
    Th,
    Td,
    A,
    P,
)

from lona import View

from webshop.forms import ProductForm
from webshop.models import Product


class ListProductsView(View):
    def save(self, input_event):
        with self.html.lock:
            self.form.save()
            self.modal.close()
            self.update_table()

    def open_form(self, input_event):
        with self.html.lock:
            if input_event.node is self.add_button:
                product = None

            else:
                tr = input_event.node.closest('tr')
                product = Product.objects.get(tr.state['id'])

            self.form = ProductForm(product)

            self.modal.get_body().nodes = self.form

            self.modal.get_footer().nodes = [
                InlineButton(
                    'Cancel',
                    secondary=True,
                    handle_click=lambda i: self.modal.close(),
                ),
                InlineButton(
                    'Save',
                    handle_click=self.save,
                ),
            ]

            self.modal.open()

    def delete(self, input_event):
        self.product.delete()
        self.modal.close()
        self.update_table()

    def open_delete_confirmation(self, input_event):
        with self.html.lock:
            tr = input_event.node.closest('tr')
            self.product = Product.objects.get(tr.state['id'])

            self.modal.get_body().nodes = [
                f'Are you sure you want to delete "{self.product.name}"?',
            ]

            self.modal.get_footer().nodes = [
                InlineButton(
                    'Cancel',
                    secondary=True,
                    handle_click=lambda i: self.modal.close(),
                ),
                InlineButton(
                    'Delete',
                    handle_click=self.delete,
                ),
            ]

            self.modal.open()

    def load_from_backup(self, input_event):
        progress = Progress(value=0)

        with self.html.lock:
            self.modal.closable = False

            self.modal.get_body().nodes = [
                H3('Load From Backup'),
                P('Loading products from backup...'),
                progress,
            ]

            self.modal.get_footer().clear()
            self.modal.open()

        Product.objects.load_from_backup()

        for i in range(0, 10):
            progress.value = (i + 1) * 10
            self.show()
            self.sleep(0.5)

        with self.html.lock:
            self.update_table()
            self.modal.closable = True
            self.modal.close()

        self.show()

    def update_table(self):
        with self.html.lock:
            tbody = self.table.query_selector('tbody')

            tbody.clear()

            for product in Product.objects.all():
                tbody.append(
                    Tr(
                        Td(
                            A(
                                product.name,
                                href='#',
                                events=[CLICK],
                                handle_click=self.open_form,
                            ),
                        ),
                        Td(product.price),
                        Td(
                            InlineButton(
                                Icon('trash'),
                                title='Delete',
                                handle_click=self.open_delete_confirmation,
                            ),
                        ),
                        state={
                            'id': product.id,
                        },
                    ),
                )

    def handle_request(self, request):
        self.table = Table(
            THead(
                Tr(
                    Th('Name'),
                    Th('Price'),
                    Th('Actions', width='5em'),
                ),
            ),
            TBody(),
        )

        self.add_button = InlineButton(
            'Add Product',
            handle_click=self.open_form,
        )

        self.load_from_backup_button = InlineButton(
            'Load From Backup',
            secondary=True,
            handle_click=self.load_from_backup,
        )

        self.modal = Modal()

        self.html = HTML(
            H1('Products'),
            Div(
                self.load_from_backup_button,
                ' ',
                self.add_button,
                style={
                    'text-align': 'right',
                    'margin-bottom': '1em',
                },
            ),
            self.table,
            self.modal,
        )

        self.update_table()

        return self.html
