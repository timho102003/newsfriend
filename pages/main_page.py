import dash
from components.cards import card_layout

dash.register_page(__name__, path="/")

layout = dash.html.Div([*card_layout], className="pad-row")
