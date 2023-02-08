import dash_bootstrap_components as dbc
from dash import html

from config import MAINPAGE_ARTICLE_CARD_CONFIG, TEST_NEWS

MAX_COLS = 4


def form_card(title, imgsrc, ori_link):
    card_img = dbc.CardImg(src=imgsrc, top=True)
    card_body = dbc.CardBody(
        [
            html.H6(title, className="card-title"),
            dbc.Button(
                "Original Article",
                color="primary",
                external_link=True,
                href=ori_link,
                target="_blank",
            ),
        ]
    )
    return card_img, card_body


def form_layout(row_style="p-2"):
    card_list = []
    for i in range(len(TEST_NEWS)):
        article = TEST_NEWS.iloc[i, :]
        card_img, card_body = form_card(
            title=article["title"], imgsrc=article["imgname"], ori_link=article["link"]
        )
        card = dbc.Card(
            [card_img, card_body],
        )
        card_list.append(card)

    card_layout = []
    row_ = []
    article_idx = 0
    while article_idx < len(card_list):
        if article_idx % MAX_COLS == 0 and article_idx != 0:
            card_layout.append(
                dbc.Row(
                    row_,
                    align="center",
                    justify="center",
                    class_name=row_style,
                )
            )
            row_ = []
        row_.append(dbc.Col(card_list[article_idx]))
        article_idx += 1
    card_layout.append(
        dbc.Row(row_, align="center", justify="center", class_name=row_style)
    )
    return card_layout


card_layout = form_layout(row_style=MAINPAGE_ARTICLE_CARD_CONFIG["row_style"])

__all__ = ["card_layout"]
