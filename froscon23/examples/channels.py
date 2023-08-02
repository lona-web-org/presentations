from datetime import datetime

from lona_picocss.html import HTML, H1, Div, ScrollerPre, TextArea, InlineButton
from lona_picocss import install_picocss

from lona import View, App, Channel

app = App(__file__)

install_picocss(app)


@app.route('/api/<channel>(/)', interactive=False)
class Api(View):
    def handle_request(self, request):
        channel_name = request.match_info.get('channel')
        message = request.GET.get('message', '')

        Channel(channel_name).send(message)


@app.route('/<channel>(/)')
class index(View):
    def handle_channel_message(self, message):
        self.scroller.append(
            Div(f'{datetime.now()}: {message.topic}: {str(message.data)}'),
        )

    def handle_click(self, input_event):
        with self.html.lock:
            self.channel.send(
                self.text_input.value,
            )

            self.text_input.value = ''

    def handle_request(self, request):
        self.channel_name = request.match_info.get('channel')

        self.scroller = ScrollerPre(
            height='300px',
            style='padding: 0.5em',
        )

        self.text_input = TextArea(
            placeholder='Say something nice',
        )

        self.channel = self.subscribe(
            self.channel_name,
            self.handle_channel_message,
        )

        self.html = HTML(
            H1(f'Messages for "{self.channel_name}"'),
            self.scroller,
            self.text_input,
            InlineButton('Send', handle_click=self.handle_click),
        )

        return self.html


app.run()
