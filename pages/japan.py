import dash
import dash_core_components as dcc
import dash_html_components as html
from components.cards import form_layout
from dash.dependencies import Input, Output
from config import MAINPAGE_ARTICLE_CARD_CONFIG

language = "jpn"

dash.register_page(__name__, path="/japan")

layout = html.Div([
    dcc.Location(id='jp-url', refresh=False),
    dcc.Store(id='jp-page-store', data=1),
    html.Div(id='jp-card-layout')
])

@dash.callback(Output('jp-card-layout', 'children'),
              [Input('jp-url', 'pathname'), Input('jp-page-store', 'data')])
def display_page(pathname, page):
    if page is None:
        page = 1
    card_layout = form_layout(
        row_style=MAINPAGE_ARTICLE_CARD_CONFIG["row_style"],
        lang=language,
        page=page
    )
    return html.Div([*card_layout], className="pad-row")

@dash.callback(Output('jp-page-store', 'data'),
              [Input('pagination', 'active_page')])
def update_page(active_page):
    return active_page

