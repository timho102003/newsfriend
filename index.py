from dash import Dash, dcc, html

from app import app, server
from components.cards import card_layout
from components.navigation_bar import nav_bar

from config import adsense_code

app.layout = html.Div([nav_bar, html.Div([*card_layout], className="pad-row")])

footer = html.Div([dcc.Markdown(adsense_code, dangerously_allow_html=True)])
app.layout.children.append(footer)

if __name__ == "__main__":
    app.run_server(debug=False)
