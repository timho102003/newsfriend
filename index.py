from app import app
from app import server
from dash import Dash, html, dcc
from components.navigation_bar import nav_bar
from components.cards import card_layout

app.layout = html.Div([
    nav_bar,
    html.Div([*card_layout])
])

if __name__ == '__main__':
    app.run_server(debug=True)