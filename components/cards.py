import math
import random

import dash_bootstrap_components as dbc
from dash import html

from config import COUNTRY_LIST, NO_IMG_URL
from global_var import article_database

MAX_COLS = 4
CARDS_PER_PAGE = 28


def form_card(title, imgsrc, ori_link, lang, id):
    country = list(filter(lambda x: x[1] == lang, COUNTRY_LIST))[0][0]
    card_img = dbc.CardImg(
        src=imgsrc,
        top=True,
        style={
            "height": "300px",
            "object-fit": "cover",
            "borderTopLeftRadius": "40px",
            "borderTopRightRadius": "40px",
        },
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
        class_name="p-1 me-3 mx-auto",
    )
    read_more = dbc.Button(
        "Read More",
        color="primary",
        external_link=True,
        href=f"{country}/news_id_{id}",
        target="_blank",
        class_name="p-1 me-3 mx-auto",
    )
    card_footer = dbc.CardFooter(
        children=[ori_article, read_more],
        style={
            "height": "75px",
            "borderRadius": "0px 0px 40px 40px",
            "position": "absolute",
            "bottom": "0",
            "left": "0px",
            "right": "0px",
        },
    )
    return card_img, card_body, card_footer


def form_layout(page=1, row_style="p-2", lang=""):
    start_idx = (page - 1) * CARDS_PER_PAGE
    end_idx = page * CARDS_PER_PAGE
    card_list = []
    articles = article_database.retrieve_article(lang=lang)
    for a_i, article in enumerate(articles[start_idx:end_idx]):
        card_img, card_body, card_footer = form_card(
            title=article["title"],
            imgsrc=article["image"]
            if article["image"] is not None
            else NO_IMG_URL.format(random.randint(6, 10)),
            ori_link=article["url"],
            lang=lang,
            id=article["_id"],
        )
        card_style = {
            "height": "650px",
            "width": "500px",
            "borderRadius": "50px",
            "overflow": "hidden",
        }
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
        col_style = {}
        if article_idx % MAX_COLS == 0:
            col_style ={"marginLeft": "100px"}
        if article_idx % MAX_COLS == MAX_COLS-1:
            col_style ={"marginRight": "100px"}
        row_.append(dbc.Col(card_list[article_idx], style=col_style))
        article_idx += 1
    
    # Add pagination
    total_pages = int((len(articles) - 1) / CARDS_PER_PAGE) + 1  # Calculate total number of pages
    pagination_layout = dbc.Pagination(
        id='pagination',
        step=1,
        active_page=page,
        max_value=total_pages,
        first_last=True,
        previous_next=True,
        fully_expanded=False,
        className="my-4",
        style={"justify-content": "center"}
    )
    card_layout.append(dbc.Row(row_, align="center", justify="center"))
    card_layout.append(dbc.Row(dbc.Col(pagination_layout)))
    return card_layout



__all__ = ["card_layout", "form_layout"]
