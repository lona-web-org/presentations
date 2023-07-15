from lona_picocss.html import InlineButton, TextArea, HTML, H1, Pre
from lona_picocss import install_picocss

from lona import View, App

app = App(__file__)
app.settings.STOP_DAEMON_WHEN_VIEW_FINISHES = False

install_picocss(app, debug=True)


@app.route('/')
class Index(View):
    def send(self, input_event):
        with self.html.lock:
            self.pre.write_line(self.text_area.value)
            self.text_area.value = ''

    def handle_request(self, request):
        self.pre = Pre()
        self.text_area = TextArea()

        self.is_daemon = True

        self.html = HTML(
            H1('Chat'),
            self.pre,
            self.text_area,
            InlineButton('Send', handle_click=self.send),
        )

        return self.html


app.run()
