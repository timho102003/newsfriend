import dash

from components.cards import form_layout
from config import MAINPAGE_ARTICLE_CARD_CONFIG

language = "zho"

dash.register_page(__name__, path="/taiwan&china")
card_layout = form_layout(
    row_style=MAINPAGE_ARTICLE_CARD_CONFIG["row_style"], lang=language
)
layout = dash.html.Div([*card_layout], className="pad-row")
