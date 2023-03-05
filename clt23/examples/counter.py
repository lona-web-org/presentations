from lona.html import Button, Span, HTML, Div, H1
from lona import View, App

app = App(__file__)


@app.route('/')
class Index(View):
    def decrease(self, input_event):
        with self.html.lock:
            self.counter.set_text(
                int(self.counter.get_text()) - 1,
            )

    def increase(self, input_event):
        with self.html.lock:
            self.counter.set_text(
                int(self.counter.get_text()) + 1,
            )

    def handle_request(self, request):
        self.counter = Span('10', style={'font-size': '2em'})

        self.html = HTML(
            H1('Counter'),
            Div(
                Button('Decrease', handle_click=self.decrease),
                ' ',
                self.counter,
                ' ',
                Button('Increase', handle_click=self.increase),
            ),
        )

        return self.html


app.run()
