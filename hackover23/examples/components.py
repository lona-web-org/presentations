from lona_picocss.html import InlineButton, Span, Icon, HTML, Div, H1
from lona_picocss import install_picocss

from lona import View, App

app = App(__file__)

install_picocss(app, debug=True)


class Counter(Div):
    def __init__(self, value=0):
        super().__init__()

        self.counter = Span('10', style={'font-size': '2em'})

        self.nodes = [
            InlineButton(Icon('minus-circle'), handle_click=self.decrease),
            ' ',
            self.counter,
            ' ',
            InlineButton(Icon('plus-circle'), handle_click=self.increase),
        ]

    def decrease(self, input_event):
        with self.lock:
            self.counter.set_text(
                int(self.counter.get_text()) - 1,
            )

    def increase(self, input_event):
        with self.lock:
            self.counter.set_text(
                int(self.counter.get_text()) + 1,
            )


@app.route('/')
class Index(View):
    def handle_request(self, request):
        self.html = HTML(
            H1('Counter'),

            Counter(10),
            Counter(20),
            Counter(30),
        )

        return self.html


app.run()
