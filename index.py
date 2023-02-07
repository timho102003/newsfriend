from dash import Dash, dcc, html

from app import app, server
from components.cards import card_layout
from components.navigation_bar import nav_bar

app.layout = html.Div([nav_bar, html.Div([*card_layout])])

if __name__ == "__main__":
    app.run_server(debug=True)
