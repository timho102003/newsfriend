import dash
from components.cards import card_layout

dash.register_page(__name__, path="/", order=0)

layout = dash.html.Div([*card_layout], className="pad-row")
