from copy import deepcopy
import random

from lona_picocss.html import InlineButton, HTML, H1, Br
from lona_picocss import install_picocss
from lona_chartjs.html import Chart

from lona import View, App

app = App(__file__)
app.settings.STOP_DAEMON_WHEN_VIEW_FINISHES = False

install_picocss(app, debug=True)

CHART_DATA = {
    'type': 'line',
    'data': {
        'labels': ['', '', '', '', '', ''],
        'datasets': [{
            'label': 'Random Points',
            'data': [12, 19, 3, 5, 2, 3],
            'borderWidth': 2,
            'borderColor': 'rgba(255, 99, 132, 1)',
        }]
    },
    'options': {
        'animation': True,
        'responsive': True,
    }
}


@app.route('/')
class MyLonaView(View):
    def add_point(self, input_event):
        with self.html.lock:
            self.chart.data['data']['labels'].append('')
            self.chart.data['data']['datasets'][0]['data'].append(random.choice(range(20)))

    def handle_request(self, request):
        self.is_daemon = True

        self.chart = Chart(
            data=deepcopy(CHART_DATA),
        )

        self.chart.style['background-color'] = 'white'

        self.html = HTML(
            H1('Chart.js'),
            self.chart,
            Br(),
            InlineButton('Add Point', handle_click=self.add_point),
        )

        return self.html


app.run()
