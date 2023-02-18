import random
import dash_bootstrap_components as dbc
from dash import html

from config import COUNTRY_LIST, NO_IMG_URL
from global_var import article_database

MAX_COLS = 4


def form_card(title, imgsrc, ori_link, lang, id):
    country = list(filter(lambda x: x[1] == lang, COUNTRY_LIST))[0][0]
    card_img = dbc.CardImg(
        src=imgsrc, top=True, style={"height": "300px", "object-fit": "cover", "borderTopLeftRadius": "40px", "borderTopRightRadius": "40px"}
    )
    card_body = dbc.CardBody(
        [
            html.H6(title, className="card-title"),
        ],
        style={"height": "150px", "object-fit": "cover", "borderRadius": "40px"},
    )
    ori_article = dbc.Button(
        "Original Article",
        color="secondary",
        external_link=True,
        href=ori_link,
        target="_blank",
        class_name="p-1 me-3 mx-auto"
    )
    read_more = dbc.Button(
        "Read More",
        color="primary",
        external_link=True,
        href=f"{country}/news_id_{id}",
        target="_blank",
        class_name="p-1 me-3 mx-auto"
    )
    card_footer = dbc.CardFooter(children=[ori_article, read_more], style={"height": "75px", "borderRadius": "0px 0px 40px 40px", "position": "absolute", "bottom": "0", "left": "0px", "right": "0px"})
    return card_img, card_body, card_footer


def form_layout(row_style="p-2", lang=""):
    card_list = []
    articles = article_database.retrieve_article(lang=lang)
    for a_i, article in enumerate(articles):
        card_img, card_body, card_footer = form_card(
            title=article["title"],
            imgsrc=article["image"] if article["image"] is not None else NO_IMG_URL.format(random.randint(6, 10)),
            ori_link=article["url"],
            lang=lang,
            id=article["_id"],
        )
        card_style = {"height": "650px", "width": "500px", "borderRadius": "50px", "overflow": "hidden"}
        if a_i // MAX_COLS == 0:
            card_style.update({"marginTop": "30px"})
        card = dbc.Card(
            [card_img, card_body, card_footer],
            style=card_style,
            className="h-25 w-100 mb-3",
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
                )
            )
            row_ = []
        row_.append(dbc.Col(card_list[article_idx]))
        article_idx += 1
    card_layout.append(dbc.Row(row_, align="center", justify="center"))
    return card_layout


__all__ = ["card_layout", "form_layout"]
