import dash
import dash_core_components as dcc
import dash_html_components as html
from components.cards import form_layout
from dash.dependencies import Input, Output
from config import MAINPAGE_ARTICLE_CARD_CONFIG

language = "eng"

dash.register_page(__name__, path="/", order=0)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='page-store', data=1),
    html.Div(id='card-layout')
])

@dash.callback(Output('card-layout', 'children'),
              [Input('url', 'pathname'), Input('page-store', 'data')])
def display_page(pathname, page):
    if page is None:
        page = 1
    card_layout = form_layout(
        row_style=MAINPAGE_ARTICLE_CARD_CONFIG["row_style"],
        lang=language,
        page=page
    )
    return html.Div([*card_layout], className="pad-row")

@dash.callback(Output('page-store', 'data'),
              [Input('pagination', 'active_page')])
def update_page(active_page):
    return active_page