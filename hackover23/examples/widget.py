from lona_picocss.html import Switch, Label, HTML, Grid, Div, H1, Br
from lona_picocss import install_picocss
from lona.static_files import Script
from lona import View, App

app = App(__file__)

install_picocss(app, debug=True)


class RotatingContainer(Div):
    WIDGET = 'RotatingContainer'

    STATIC_FILES = [
        Script(
            name='rotating-container',
            path='rotating-container.js',
        ),
    ]

    STYLE = {
        'display': 'inline-block',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widget_data = {
            'animation_running': True,
        }

    def set_animation_running(self, running):
        self.widget_data['animation_running'] = running


@app.route('/')
class Index(View):
    def set_animation_running(self, input_event):
        self.rotating_container.set_animation_running(input_event.node.value)

    def handle_request(self, request):
        self.rotating_container = RotatingContainer('Weeeeee!')

        return HTML(
            H1('Rotating Container'),

            Grid(
                Div(
                    self.rotating_container,
                    Br(),
                    Br(),
                    Br(),
                    Br(),
                    Br(),
                ),
                Div(
                    Label(
                        Switch(
                            value=True,
                            handle_change=self.set_animation_running,
                        ),
                        'Animation',
                    ),
                )
            ),
        )


app.run()