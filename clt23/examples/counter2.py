from lona_picocss.html import InlineButton, Span, Icon, HTML, Div, H1
from lona_picocss import install_picocss

from lona import View, App

app = App(__file__)
app.settings.STOP_DAEMON_WHEN_VIEW_FINISHES = False

install_picocss(app, debug=True)


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
                InlineButton(Icon('minus-circle'), handle_click=self.decrease),
                ' ',
                self.counter,
                ' ',
                InlineButton(Icon('plus-circle'), handle_click=self.increase),
            ),
        )

        return self.html


app.run()
